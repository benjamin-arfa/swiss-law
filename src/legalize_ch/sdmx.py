"""SDMX artefacts for the data page (api/sdmx/).

Agency ``SLC`` (Swiss Law Collection), version 1.0.  Generates, with the
standard library only:

- ``structures.xml`` — SDMX-ML 2.1 Structure message: codelists
  (CL_CANTON, CL_DOMAIN, CL_INSTRUMENT_TYPE), concept scheme CS_SLC, the
  DSDs ``DSD_LAWS`` / ``DSD_CONCORDATS`` and dataflows ``DF_LAWS`` /
  ``DF_CONCORDATS``.
- per-flow data in SDMX-CSV 1.0 (``data/df_*.sdmx.csv``) and SDMX-ML 2.1
  GenericData (``data/df_*.xml``).
"""
from __future__ import annotations

import logging
from pathlib import Path
from xml.sax.saxutils import escape

from .categories import CATEGORY_TYPE_LABELS
from .stats import ALL_CANTON_CODES, CONCORDAT_DOMAINS, TYPE_SLUGS

logger = logging.getLogger(__name__)

AGENCY = "SLC"
VERSION = "1.0"

_NS = ('xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message" '
       'xmlns:str="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure" '
       'xmlns:com="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common"')

_HEADER = """  <mes:Header>
    <mes:ID>{msg_id}</mes:ID>
    <mes:Test>false</mes:Test>
    <mes:Prepared>{prepared}</mes:Prepared>
    <mes:Sender id="SLC"/>
  </mes:Header>"""

# Canton display names (official French short names)
_CANTON_NAMES = {
    "AG": "Argovie", "AI": "Appenzell Rhodes-Intérieures",
    "AR": "Appenzell Rhodes-Extérieures", "BE": "Berne",
    "BL": "Bâle-Campagne", "BS": "Bâle-Ville", "FR": "Fribourg",
    "GE": "Genève", "GL": "Glaris", "GR": "Grisons", "JU": "Jura",
    "LU": "Lucerne", "NE": "Neuchâtel", "NW": "Nidwald", "OW": "Obwald",
    "SG": "Saint-Gall", "SH": "Schaffhouse", "SO": "Soleure",
    "SZ": "Schwytz", "TG": "Thurgovie", "TI": "Tessin", "UR": "Uri",
    "VD": "Vaud", "VS": "Valais", "ZG": "Zoug", "ZH": "Zurich",
}


def _codelist(cl_id: str, name: str, codes: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f'        <str:Code id="{escape(cid, {'"': "&quot;"})}">'
        f'<com:Name xml:lang="fr">{escape(label)}</com:Name></str:Code>'
        for cid, label in codes)
    return (f'      <str:Codelist id="{cl_id}" agencyID="{AGENCY}" version="{VERSION}">\n'
            f'        <com:Name xml:lang="en">{escape(name)}</com:Name>\n'
            f'{items}\n      </str:Codelist>')


def _dsd(dsd_id: str, name: str, dims: list[tuple[str, str | None]],
         annotation: str | None = None) -> str:
    """dims: (concept_id, codelist_id or None). TIME_PERIOD added automatically."""
    ann = ""
    if annotation:
        ann = ('        <com:Annotations><com:Annotation>'
               f'<com:AnnotationType>METHODOLOGY</com:AnnotationType>'
               f'<com:AnnotationText xml:lang="en">{escape(annotation)}</com:AnnotationText>'
               '</com:Annotation></com:Annotations>\n')
    dim_xml = []
    for i, (cid, cl) in enumerate(dims, start=1):
        rep = (f'<str:LocalRepresentation><str:Enumeration>'
               f'<Ref id="{cl}" agencyID="{AGENCY}" version="{VERSION}" package="codelist" class="Codelist"/>'
               f'</str:Enumeration></str:LocalRepresentation>') if cl else ""
        dim_xml.append(
            f'            <str:Dimension id="{cid}" position="{i}">'
            f'<str:ConceptIdentity><Ref id="{cid}" maintainableParentID="CS_SLC" '
            f'agencyID="{AGENCY}" maintainableParentVersion="{VERSION}" '
            f'package="conceptscheme" class="Concept"/></str:ConceptIdentity>{rep}'
            f'</str:Dimension>')
    time_pos = len(dims) + 1
    dim_xml.append(
        f'            <str:TimeDimension id="TIME_PERIOD" position="{time_pos}">'
        f'<str:ConceptIdentity><Ref id="TIME_PERIOD" maintainableParentID="CS_SLC" '
        f'agencyID="{AGENCY}" maintainableParentVersion="{VERSION}" '
        f'package="conceptscheme" class="Concept"/></str:ConceptIdentity>'
        f'</str:TimeDimension>')
    return (f'      <str:DataStructure id="{dsd_id}" agencyID="{AGENCY}" version="{VERSION}">\n'
            f'        <com:Name xml:lang="en">{escape(name)}</com:Name>\n{ann}'
            f'        <str:DataStructureComponents>\n'
            f'          <str:DimensionList id="DimensionDescriptor">\n'
            + "\n".join(dim_xml) + "\n"
            f'          </str:DimensionList>\n'
            f'          <str:MeasureList id="MeasureDescriptor">\n'
            f'            <str:PrimaryMeasure id="OBS_VALUE">'
            f'<str:ConceptIdentity><Ref id="OBS_VALUE" maintainableParentID="CS_SLC" '
            f'agencyID="{AGENCY}" maintainableParentVersion="{VERSION}" '
            f'package="conceptscheme" class="Concept"/></str:ConceptIdentity>'
            f'</str:PrimaryMeasure>\n'
            f'          </str:MeasureList>\n'
            f'        </str:DataStructureComponents>\n'
            f'      </str:DataStructure>')


def generate_structures() -> str:
    """SDMX-ML 2.1 Structure message with all SLC artefacts."""
    domains = [(d["key"], d["label_fr"]) for d in CONCORDAT_DOMAINS]
    types = []
    for label_de, slug in TYPE_SLUGS.items():
        label = CATEGORY_TYPE_LABELS.get(label_de, {})
        types.append((slug, label.get("fr") or label_de))
    concepts = "\n".join(
        f'        <str:Concept id="{cid}"><com:Name xml:lang="en">{escape(name)}</com:Name></str:Concept>'
        for cid, name in [
            ("INSTRUMENT_TYPE", "Instrument type"),
            ("CANTON", "Canton"),
            ("DOMAIN", "Legal domain (chstat/BADAC nomenclature)"),
            ("TIME_PERIOD", "Enactment year"),
            ("OBS_VALUE", "Count"),
        ])

    concordat_annotation = (
        "chstat/BADAC counting: one observation unit per signatory canton of an "
        "agreement (signatories = cantons publishing the text plus cantons named "
        "in titles). Observations with TIME_PERIOD <= 2003 are computed from the "
        "Swiss Law Collection's collections — no scaling, no external "
        "baseline. chstat.ch/BADAC's 2003 figure (2,522 memberships <= 2003) "
        "is an external comparison reference only; the computed value is "
        "lower because long-repealed agreements were delisted upstream. "
        "Aggregates use the SDMX reserved code _T (per-year canton totals, "
        "domain totals and grand total); totals across all years = sum over "
        "TIME_PERIOD.")

    total = [("_T", "Total")]   # SDMX reserved code for aggregates
    body = f"""<?xml version="1.0" encoding="UTF-8"?>
<mes:Structure {_NS}>
{_HEADER.format(msg_id="SLC_STRUCTURES", prepared="2026-08-03T00:00:00")}
  <mes:Structures>
    <str:Codelists>
{_codelist("CL_CANTON", "Swiss cantons", [(c, _CANTON_NAMES[c]) for c in ALL_CANTON_CODES] + total)}
{_codelist("CL_DOMAIN", "Legal domains (chstat/BADAC)", domains + total)}
{_codelist("CL_INSTRUMENT_TYPE", "Instrument types (LexFind)", types + total)}
    </str:Codelists>
    <str:Concepts>
      <str:ConceptScheme id="CS_SLC" agencyID="{AGENCY}" version="{VERSION}">
        <com:Name xml:lang="en">Swiss Law Collection concepts</com:Name>
{concepts}
      </str:ConceptScheme>
    </str:Concepts>
    <str:DataStructures>
{_dsd("DSD_LAWS", "Cantonal acts by instrument type, canton, legal domain and enactment year",
      [("INSTRUMENT_TYPE", "CL_INSTRUMENT_TYPE"), ("CANTON", "CL_CANTON"), ("DOMAIN", "CL_DOMAIN")])}
{_dsd("DSD_CONCORDATS", "Intercantonal agreement memberships (computed signatory counting)",
      [("CANTON", "CL_CANTON"), ("DOMAIN", "CL_DOMAIN")], concordat_annotation)}
    </str:DataStructures>
    <str:Dataflows>
      <str:Dataflow id="DF_LAWS" agencyID="{AGENCY}" version="{VERSION}">
        <com:Name xml:lang="en">Cantonal acts</com:Name>
        <str:Structure><Ref id="DSD_LAWS" agencyID="{AGENCY}" version="{VERSION}" package="datastructure" class="DataStructure"/></str:Structure>
      </str:Dataflow>
      <str:Dataflow id="DF_CONCORDATS" agencyID="{AGENCY}" version="{VERSION}">
        <com:Name xml:lang="en">Concordat memberships (chstat methodology)</com:Name>
        <str:Structure><Ref id="DSD_CONCORDATS" agencyID="{AGENCY}" version="{VERSION}" package="datastructure" class="DataStructure"/></str:Structure>
      </str:Dataflow>
    </str:Dataflows>
  </mes:Structures>
</mes:Structure>
"""
    return body


def _laws_observations(type_tables: dict):
    """Yield (type_slug, canton, domain, year, value): detail rows plus the
    per-year marginal totals under the SDMX reserved code ``_T``:
    (type,_T,_T), (_T,canton,_T), (_T,_T,domain) and (_T,_T,_T)."""
    per_year: dict[str, dict] = {}
    for slug, tbl in sorted(type_tables["files"].items()):
        for year, cantons in tbl.get("by_year", {}).items():
            if year == "unknown":
                continue  # SDMX TIME_PERIOD must be a real period
            agg = per_year.setdefault(year, {"detail": [], "type": {},
                                             "canton": {}, "domain": {}, "all": 0})
            for canton in sorted(cantons):
                for dom, n in sorted(cantons[canton].items()):
                    if not n:
                        continue
                    agg["detail"].append((slug, canton, dom, year, n))
                    agg["type"][slug] = agg["type"].get(slug, 0) + n
                    agg["canton"][canton] = agg["canton"].get(canton, 0) + n
                    agg["domain"][dom] = agg["domain"].get(dom, 0) + n
                    agg["all"] += n
    for year in sorted(per_year):
        agg = per_year[year]
        yield from sorted(agg["detail"])
        for slug, n in sorted(agg["type"].items()):
            yield slug, "_T", "_T", year, n
        for canton, n in sorted(agg["canton"].items()):
            yield "_T", canton, "_T", year, n
        for dom, n in sorted(agg["domain"].items()):
            yield "_T", "_T", dom, year, n
        yield "_T", "_T", "_T", year, agg["all"]


def _concordat_observations(conc_sig: dict):
    """Yield (canton, domain, year, value): detail rows plus per-year ``_T``
    marginals — (canton,_T), (_T,domain) and the grand total (_T,_T)."""
    for year in sorted(conc_sig.get("by_year", {})):
        if year == "unknown":
            continue
        cantons = conc_sig["by_year"][year]
        canton_tot: dict[str, int] = {}
        domain_tot: dict[str, int] = {}
        total = 0
        for canton in sorted(cantons):
            for dom, n in sorted(cantons[canton].items()):
                if not n:
                    continue
                yield canton, dom, year, n
                canton_tot[canton] = canton_tot.get(canton, 0) + n
                domain_tot[dom] = domain_tot.get(dom, 0) + n
                total += n
        for canton, n in sorted(canton_tot.items()):
            yield canton, "_T", year, n
        for dom, n in sorted(domain_tot.items()):
            yield "_T", dom, year, n
        if total:
            yield "_T", "_T", year, total


def generate_sdmx_csv(flow_id: str, dims: list[str], observations) -> str:
    """SDMX-CSV 1.0: DATAFLOW,<dims...>,TIME_PERIOD,OBS_VALUE."""
    lines = [",".join(["DATAFLOW", *dims, "TIME_PERIOD", "OBS_VALUE"])]
    ref = f"{AGENCY}:{flow_id}({VERSION})"
    for obs in observations:
        *key, year, value = obs
        lines.append(",".join([ref, *key, year, str(value)]))
    return "\n".join(lines) + "\n"


def generate_generic_data(flow_id: str, dsd_id: str, dims: list[str],
                          observations) -> str:
    """SDMX-ML 2.1 GenericData message, flat (series-less) observations."""
    ns = ('xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message" '
          'xmlns:gen="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic" '
          'xmlns:com="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common"')
    obs_xml = []
    for obs in observations:
        *key, year, value = obs
        key_values = "".join(
            f'<gen:Value id="{d}" value="{escape(str(v), {'"': "&quot;"})}"/>'
            for d, v in zip(dims, key))
        key_values += f'<gen:Value id="TIME_PERIOD" value="{year}"/>'
        obs_xml.append(
            f'    <gen:Obs><gen:ObsKey>{key_values}</gen:ObsKey>'
            f'<gen:ObsValue value="{value}"/></gen:Obs>')
    header = f"""  <mes:Header>
    <mes:ID>{flow_id}_DATA</mes:ID>
    <mes:Test>false</mes:Test>
    <mes:Prepared>2026-08-03T00:00:00</mes:Prepared>
    <mes:Sender id="{AGENCY}"/>
    <mes:Structure structureID="{dsd_id}" dimensionAtObservation="AllDimensions">
      <com:Structure><Ref id="{dsd_id}" agencyID="{AGENCY}" version="{VERSION}" package="datastructure" class="DataStructure"/></com:Structure>
    </mes:Structure>
  </mes:Header>"""
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<mes:GenericData {ns}>\n{header}\n'
            f'  <mes:DataSet structureRef="{dsd_id}">\n'
            + "\n".join(obs_xml) +
            f'\n  </mes:DataSet>\n</mes:GenericData>\n')


def generate_sdmx_files(type_tables: dict, conc_sig: dict) -> dict[str, str]:
    """Return {relative_path: content} for api/sdmx/."""
    laws = list(_laws_observations(type_tables))
    conc = list(_concordat_observations(conc_sig))
    return {
        "structures.xml": generate_structures(),
        "data/df_laws.sdmx.csv": generate_sdmx_csv(
            "DF_LAWS", ["INSTRUMENT_TYPE", "CANTON", "DOMAIN"], laws),
        "data/df_laws.xml": generate_generic_data(
            "DF_LAWS", "DSD_LAWS", ["INSTRUMENT_TYPE", "CANTON", "DOMAIN"], laws),
        "data/df_concordats.sdmx.csv": generate_sdmx_csv(
            "DF_CONCORDATS", ["CANTON", "DOMAIN"], conc),
        "data/df_concordats.xml": generate_generic_data(
            "DF_CONCORDATS", "DSD_CONCORDATS", ["CANTON", "DOMAIN"], conc),
    }


def write_sdmx_files(files: dict[str, str], out_dir: str | Path) -> None:
    out = Path(out_dir)
    for rel, content in files.items():
        path = out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    logger.info("Wrote %d SDMX files to %s", len(files), out)
