"""Tests for the SDMX artefacts and plain-CSV exports."""
from __future__ import annotations

import xml.etree.ElementTree as ET

from legalize_ch.data_exports import generate_csv_exports
from legalize_ch.sdmx import generate_sdmx_files
from legalize_ch.stats import (
    generate_concordats_extrapolated,
    generate_types_by_domain,
)


def _law(canton="GR", nr="1.1", lang="de", ctype="Gesetz",
         gc="4.10 Schule", enacted="1990-01-01", title="Schulgesetz"):
    return {"_scope": "cantonal", "canton": canton, "systematic_number": nr,
            "language": lang, "_path": f"ch/{canton.lower()}/{lang}/{nr}.md",
            "category_type": ctype, "global_category": gc,
            "enactment_date": enacted, "version_date": "2015-01-01",
            "title": title}


def _fixtures():
    entries = [
        _law(canton="ZH", nr="a", ctype="Gesetz", enacted="1990-01-01"),
        _law(canton="BE", nr="b", ctype="Verordnung", gc="6.10 Steuern",
             enacted="2001-01-01"),
        _law(canton="ZH", nr="c", ctype="Interkantonale Vereinbarung",
             title="Vereinbarung zwischen den Kantonen Zürich und Bern",
             enacted="2010-01-01"),
    ]
    return generate_types_by_domain(entries), generate_concordats_extrapolated(entries)


class TestCsvExports:
    def test_files_and_row_counts(self):
        type_tables, conc_ext = _fixtures()
        files = generate_csv_exports(type_tables, conc_ext)
        assert "laws_cube.csv" in files
        assert "gesetz_canton_year.csv" in files
        assert "concordats_memberships_since_1848.csv" in files
        assert "index.json" in files
        # cube counts sum to the number of laws (each in exactly one cell)
        cube = [l for l in files["laws_cube.csv"].splitlines()
                if l and not l.startswith("#") and not l.startswith("instrument_type")]
        assert sum(int(l.rsplit(",", 1)[1]) for l in cube) == 3
        # per-category file: ZH 1990 educ row present
        ges = files["gesetz_canton_year.csv"]
        assert any(l.startswith("ZH,1990,") for l in ges.splitlines())

    def test_concordats_csv_contains_baseline(self):
        _, conc_ext = _fixtures()
        files = generate_csv_exports(generate_types_by_domain([]), conc_ext)
        csv = files["concordats_memberships_since_1848.csv"]
        rows = [l for l in csv.splitlines() if l and not l.startswith("#")
                and not l.startswith("canton")]
        total = sum(int(r.rsplit(",", 1)[1]) for r in rows)
        assert total == conc_ext["total_memberships"]


class TestSdmx:
    def test_structures_parse_and_codelists(self):
        type_tables, conc_ext = _fixtures()
        files = generate_sdmx_files(type_tables, conc_ext)
        root = ET.fromstring(files["structures.xml"])
        ns = {"str": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure"}
        codelists = {cl.get("id"): len(cl.findall("str:Code", ns))
                     for cl in root.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}Codelist")}
        assert codelists["CL_CANTON"] == 26
        assert codelists["CL_DOMAIN"] == 7
        assert codelists["CL_INSTRUMENT_TYPE"] == 9
        dsds = [d.get("id") for d in root.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}DataStructure")]
        assert set(dsds) == {"DSD_LAWS", "DSD_CONCORDATS"}
        flows = [d.get("id") for d in root.iter("{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure}Dataflow")]
        assert set(flows) == {"DF_LAWS", "DF_CONCORDATS"}

    def test_data_files_parse_and_sum(self):
        type_tables, conc_ext = _fixtures()
        files = generate_sdmx_files(type_tables, conc_ext)
        gen_ns = "{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}"
        conc_root = ET.fromstring(files["data/df_concordats.xml"])
        values = [int(o.get("value"))
                  for o in conc_root.iter(f"{gen_ns}ObsValue")]
        assert sum(values) == conc_ext["total_memberships"]
        # SDMX-CSV rows match XML observations
        csv_rows = files["data/df_concordats.sdmx.csv"].strip().splitlines()[1:]
        assert len(csv_rows) == len(values)
        assert csv_rows[0].startswith("SLC:DF_CONCORDATS(1.0),")

    def test_laws_flow_matches_type_totals(self):
        type_tables, conc_ext = _fixtures()
        files = generate_sdmx_files(type_tables, conc_ext)
        csv_rows = files["data/df_laws.sdmx.csv"].strip().splitlines()[1:]
        total = sum(int(r.rsplit(",", 1)[1]) for r in csv_rows)
        dated_total = sum(t["total"] for t in type_tables["index"]["types"])
        assert total == dated_total  # all fixture laws are dated
