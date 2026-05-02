#!/usr/bin/env python3
"""Generate the initial meta/works.yaml from canonical lists.

This is a one-off seeding script. The truth lives in meta/works.yaml after it
is generated; the lists below are committed only for reproducibility and to
make corrections (e.g. dating fixes) easy to apply.

Date format: ISO-like, with negative year for BC. e.g. -063-11-08 = 8 Nov 63 BC.
date_precision: day | month | year | year_range
For year-precision the date is set to YYYY-07-01 (mid-year sentinel).
For month-precision the date is set to YYYY-MM-15.
year_range entries also fill date_range_end.

Letter dating: Shackleton Bailey's chronological numbering (Att, Fam, QFr, Brut)
is canonical. The dates below are best-effort approximations sufficient to
order the corpus; precise day-dates should be refined against SB's commentary
in subsequent passes. Each letter entry has notes flagging the precision.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any
import sys

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required: pip install pyyaml\n")
    raise

REPO = Path(__file__).resolve().parent.parent
WORKS_YAML = REPO / "meta" / "works.yaml"


def bc(year: int) -> int:
    """Convert a positive BC year to the negative integer used in ISO dates."""
    return -year


def fmt_date(year: int, month: int | None = None, day: int | None = None) -> str:
    """Return a YYYY-MM-DD date string with negative year for BC."""
    y = f"{year:05d}" if year < 0 else f"{year:04d}"
    m = f"{(month or 7):02d}"
    d = f"{(day or 1):02d}"
    return f"{y}-{m}-{d}"


def file_paths(category: str, year: int, work_id: str) -> dict[str, str]:
    yr = abs(year)
    era = "bc" if year < 0 else "ad"
    stem = f"{yr:03d}{era}-{work_id}"
    return {
        "latin_file": f"latin/{category}/{stem}.tex",
        "english_file": f"english/{category}/{stem}.tex",
        "headnote_file": f"headnotes/{category}/{stem}.tex",
    }


def perseus_url(phi_work: str) -> str:
    """Canonical Perseus CTS XML URL on GitHub for Cicero (PHI 0474).

    The phi_work argument is the three-digit Perseus work id (e.g. "001"
    for Pro Quinctio). Returns the raw GitHub URL to the Latin TEI XML.
    """
    return (
        "https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/master/"
        f"data/phi0474/phi{phi_work}/phi0474.phi{phi_work}.perseus-lat2.xml"
    )


def latin_library_url(slug: str) -> str:
    return f"https://www.thelatinlibrary.com/cicero/{slug}.shtml"


# ---------------------------------------------------------------------------
# SPEECHES — 58 surviving (counting In Verrem as 7 separate works: Divinatio,
# Actio Prima, plus Actio Secunda books 1–5; counting all 14 Philippics).
# Dates are well-attested; day-precision where the speech was delivered on a
# known date.
# ---------------------------------------------------------------------------
SPEECHES: list[dict[str, Any]] = [
    {"id": "pro-quinctio", "title_latin": "Pro Quinctio",
     "title_english": "For Publius Quinctius",
     "year": 81, "month": None, "day": None, "precision": "year",
     "phi": "001", "ll_slug": "quinct",
     "location": "Rome",
     "notes": "Cicero's first surviving speech; civil case against Sextus Naevius.\nThe opening of the speech is lost."},

    {"id": "pro-roscio-amerino", "title_latin": "Pro Sex. Roscio Amerino",
     "title_english": "For Sextus Roscius of Ameria",
     "year": 80, "month": None, "day": None, "precision": "year",
     "phi": "002", "ll_slug": "rosccom",
     "location": "Rome",
     "notes": "Defence of Roscius on a charge of parricide; a case implicating Sulla's freedman Chrysogonus."},

    {"id": "pro-roscio-comoedo", "title_latin": "Pro Q. Roscio Comoedo",
     "title_english": "For Quintus Roscius the Comic Actor",
     "year": 76, "month": None, "day": None, "precision": "year_range",
     "year_end": 71,
     "phi": "003", "ll_slug": "rosca",
     "location": "Rome",
     "notes": "Civil suit on a partnership; date disputed (between c. 76 and 66 BC). The speech survives incomplete."},

    {"id": "divinatio-in-caecilium", "title_latin": "Divinatio in Caecilium",
     "title_english": "Against Caecilius (Divinatio)",
     "year": 70, "month": 1, "day": None, "precision": "month",
     "phi": "004", "ll_slug": "verres.div",
     "location": "Rome",
     "notes": "Preliminary hearing to determine who would prosecute Verres; delivered early 70 BC."},

    {"id": "in-verrem-actio-prima", "title_latin": "In C. Verrem Actio Prima",
     "title_english": "Against Verres, First Hearing",
     "year": 70, "month": 8, "day": 5, "precision": "day",
     "phi": "005", "speech_index": "1", "ll_slug": "verres.1",
     "location": "Rome",
     "notes": "First action of the trial of C. Verres for extortion in Sicily; Verres withdrew into exile after this speech."},

    {"id": "in-verrem-2-1", "title_latin": "In C. Verrem Actio Secunda I",
     "title_english": "Against Verres, Second Hearing, Book I",
     "year": 70, "month": 11, "day": 1, "precision": "month",
     "phi": "005", "speech_index": "2", "ll_slug": "verres.2.1",
     "location": "Rome",
     "notes": "The Second Action was never delivered (Verres had already gone into exile) but published as a written prosecution in autumn 70 BC. Book I treats Verres' early career."},

    {"id": "in-verrem-2-2", "title_latin": "In C. Verrem Actio Secunda II",
     "title_english": "Against Verres, Second Hearing, Book II",
     "year": 70, "month": 11, "day": 2, "precision": "month",
     "phi": "005", "speech_index": "3", "ll_slug": "verres.2.2",
     "location": "Rome",
     "notes": "Verres' jurisdiction (de iurisdictione) in Sicily."},

    {"id": "in-verrem-2-3", "title_latin": "In C. Verrem Actio Secunda III",
     "title_english": "Against Verres, Second Hearing, Book III",
     "year": 70, "month": 11, "day": 3, "precision": "month",
     "phi": "005", "speech_index": "4", "ll_slug": "verres.2.3",
     "location": "Rome",
     "notes": "On Verres' grain extortions (de re frumentaria)."},

    {"id": "in-verrem-2-4", "title_latin": "In C. Verrem Actio Secunda IV",
     "title_english": "Against Verres, Second Hearing, Book IV",
     "year": 70, "month": 11, "day": 4, "precision": "month",
     "phi": "005", "speech_index": "5", "ll_slug": "verres.2.4",
     "location": "Rome",
     "notes": "On Verres' plundering of works of art (de signis)."},

    {"id": "in-verrem-2-5", "title_latin": "In C. Verrem Actio Secunda V",
     "title_english": "Against Verres, Second Hearing, Book V",
     "year": 70, "month": 11, "day": 5, "precision": "month",
     "phi": "005", "speech_index": "6", "ll_slug": "verres.2.5",
     "location": "Rome",
     "notes": "On Verres' military conduct and crucifixion of Roman citizens (de suppliciis)."},

    {"id": "pro-tullio", "title_latin": "Pro M. Tullio",
     "title_english": "For Marcus Tullius",
     "year": 71, "month": None, "day": None, "precision": "year",
     "phi": "006", "ll_slug": "tullio",
     "location": "Rome",
     "notes": "Civil case on a violent dispossession; the speech survives only in fragments."},

    {"id": "pro-fonteio", "title_latin": "Pro M. Fonteio",
     "title_english": "For Marcus Fonteius",
     "year": 69, "month": None, "day": None, "precision": "year",
     "phi": "007", "ll_slug": "fonteio",
     "location": "Rome",
     "notes": "Defence of M. Fonteius on extortion charges from his governorship of Transalpine Gaul; survives in part."},

    {"id": "pro-caecina", "title_latin": "Pro A. Caecina",
     "title_english": "For Aulus Caecina",
     "year": 69, "month": None, "day": None, "precision": "year_range",
     "year_end": 68,
     "phi": "008", "ll_slug": "caecina",
     "location": "Rome",
     "notes": "Civil case on disputed inheritance and the right of armed possession; date c. 69-68 BC."},

    {"id": "pro-lege-manilia", "title_latin": "Pro Lege Manilia (De Imperio Cn. Pompei)",
     "title_english": "On the Manilian Law (On the Command of Pompey)",
     "year": 66, "month": None, "day": None, "precision": "year",
     "phi": "009", "ll_slug": "leg.man",
     "location": "Rome",
     "notes": "Cicero's first political speech, supporting the lex Manilia granting Pompey command against Mithridates. Cicero was praetor."},

    {"id": "pro-cluentio", "title_latin": "Pro A. Cluentio",
     "title_english": "For Aulus Cluentius",
     "year": 66, "month": None, "day": None, "precision": "year",
     "phi": "010", "ll_slug": "cluentio",
     "location": "Rome",
     "notes": "A celebrated and complex defence on a charge of poisoning. The longest of Cicero's surviving forensic speeches."},

    {"id": "de-lege-agraria-1", "title_latin": "De Lege Agraria I",
     "title_english": "On the Agrarian Law, First Speech",
     "year": 63, "month": 1, "day": 1, "precision": "month",
     "phi": "011", "speech_index": "1", "ll_slug": "leg.agr.1",
     "location": "Rome",
     "notes": "Delivered in the Senate against Rullus' agrarian bill on Cicero's first day as consul. Survives in fragments only."},

    {"id": "de-lege-agraria-2", "title_latin": "De Lege Agraria II",
     "title_english": "On the Agrarian Law, Second Speech",
     "year": 63, "month": 1, "day": 4, "precision": "month",
     "phi": "011", "speech_index": "2", "ll_slug": "leg.agr.2",
     "location": "Rome",
     "notes": "Delivered before the people (contio) against Rullus' agrarian bill, January 63 BC."},

    {"id": "de-lege-agraria-3", "title_latin": "De Lege Agraria III",
     "title_english": "On the Agrarian Law, Third Speech",
     "year": 63, "month": 1, "day": None, "precision": "month",
     "phi": "011", "speech_index": "3", "ll_slug": "leg.agr.3",
     "location": "Rome",
     "notes": "A second contio speech against Rullus' bill. Survives in part."},

    {"id": "pro-rabirio-perduellionis", "title_latin": "Pro C. Rabirio Perduellionis Reo",
     "title_english": "For Gaius Rabirius on a Charge of High Treason",
     "year": 63, "month": None, "day": None, "precision": "year",
     "phi": "012", "ll_slug": "rab.perd",
     "location": "Rome",
     "notes": "Defence of the aged Rabirius prosecuted by Labienus for the killing of Saturninus in 100 BC."},

    {"id": "in-catilinam-1", "title_latin": "In Catilinam I",
     "title_english": "Against Catiline, First Speech",
     "year": 63, "month": 11, "day": 8, "precision": "day",
     "phi": "013", "speech_index": "1", "ll_slug": "cat1",
     "location": "Rome",
     "notes": "Delivered in the Temple of Jupiter Stator with Catiline present in the Senate. The first of four speeches against the conspiracy."},

    {"id": "in-catilinam-2", "title_latin": "In Catilinam II",
     "title_english": "Against Catiline, Second Speech",
     "year": 63, "month": 11, "day": 9, "precision": "day",
     "phi": "013", "speech_index": "2", "ll_slug": "cat2",
     "location": "Rome",
     "notes": "Delivered to the people in the Forum the day after the First Catilinarian, after Catiline had fled the city."},

    {"id": "in-catilinam-3", "title_latin": "In Catilinam III",
     "title_english": "Against Catiline, Third Speech",
     "year": 63, "month": 12, "day": 3, "precision": "day",
     "phi": "013", "speech_index": "3", "ll_slug": "cat3",
     "location": "Rome",
     "notes": "Delivered to the people announcing the arrest of the conspirators in the city after the seizure of evidence at the Mulvian Bridge."},

    {"id": "in-catilinam-4", "title_latin": "In Catilinam IV",
     "title_english": "Against Catiline, Fourth Speech",
     "year": 63, "month": 12, "day": 5, "precision": "day",
     "phi": "013", "speech_index": "4", "ll_slug": "cat4",
     "location": "Rome",
     "notes": "Delivered in the Senate during the debate on the punishment of the conspirators; the day Cato spoke for execution and the conspirators were put to death."},

    {"id": "pro-murena", "title_latin": "Pro L. Murena",
     "title_english": "For Lucius Murena",
     "year": 63, "month": 11, "day": None, "precision": "month",
     "phi": "014", "ll_slug": "murena",
     "location": "Rome",
     "notes": "Defence of consul-elect Murena against electoral bribery charges; delivered while Cicero was still prosecuting Catiline."},

    {"id": "pro-sulla", "title_latin": "Pro P. Sulla",
     "title_english": "For Publius Sulla",
     "year": 62, "month": None, "day": None, "precision": "year",
     "phi": "015", "ll_slug": "sulla",
     "location": "Rome",
     "notes": "Defence of P. Cornelius Sulla on a charge of complicity in the Catilinarian conspiracy."},

    {"id": "pro-archia", "title_latin": "Pro A. Licinio Archia Poeta",
     "title_english": "For the Poet Aulus Licinius Archias",
     "year": 62, "month": None, "day": None, "precision": "year",
     "phi": "016", "ll_slug": "arch",
     "location": "Rome",
     "notes": "Defence of the Greek poet Archias against a charge of falsely claiming Roman citizenship; famous for its defence of literary studies."},

    {"id": "pro-flacco", "title_latin": "Pro L. Flacco",
     "title_english": "For Lucius Flaccus",
     "year": 59, "month": None, "day": None, "precision": "year",
     "phi": "017", "ll_slug": "flacco",
     "location": "Rome",
     "notes": "Defence of L. Valerius Flaccus on extortion charges from his governorship of Asia."},

    {"id": "post-reditum-in-senatu", "title_latin": "Post Reditum in Senatu",
     "title_english": "On His Return: To the Senate",
     "year": 57, "month": 9, "day": 5, "precision": "day",
     "phi": "019", "ll_slug": "redsen",
     "location": "Rome",
     "notes": "Delivered the day after Cicero's return from exile; thanks to the Senate."},

    {"id": "post-reditum-ad-quirites", "title_latin": "Post Reditum ad Quirites",
     "title_english": "On His Return: To the Citizens",
     "year": 57, "month": 9, "day": 7, "precision": "day",
     "phi": "018", "ll_slug": "redquir",
     "location": "Rome",
     "notes": "Delivered to the people in the Forum two days after the speech to the Senate."},

    {"id": "de-domo-sua", "title_latin": "De Domo Sua",
     "title_english": "On His House",
     "year": 57, "month": 9, "day": 29, "precision": "day",
     "phi": "020", "ll_slug": "domo",
     "location": "Rome",
     "notes": "Before the college of pontiffs, arguing that Clodius' consecration of his house site was invalid. Cicero's house was restored."},

    {"id": "de-haruspicum-responsis", "title_latin": "De Haruspicum Responsis",
     "title_english": "On the Responses of the Haruspices",
     "year": 56, "month": None, "day": None, "precision": "year",
     "phi": "021", "ll_slug": "haruspic",
     "location": "Rome",
     "notes": "Reply to Clodius' use of an haruspical response against Cicero."},

    {"id": "pro-sestio", "title_latin": "Pro P. Sestio",
     "title_english": "For Publius Sestius",
     "year": 56, "month": 3, "day": None, "precision": "month",
     "phi": "022", "ll_slug": "sest",
     "location": "Rome",
     "notes": "Defence of Sestius on a charge of public violence; contains the famous statement of the optimate-popularis distinction."},

    {"id": "in-vatinium", "title_latin": "In Vatinium",
     "title_english": "Against Vatinius",
     "year": 56, "month": 3, "day": None, "precision": "month",
     "phi": "023", "ll_slug": "vatin",
     "location": "Rome",
     "notes": "Examination of the prosecution witness Vatinius during the Sestius trial."},

    {"id": "pro-caelio", "title_latin": "Pro M. Caelio",
     "title_english": "For Marcus Caelius",
     "year": 56, "month": 4, "day": 4, "precision": "day",
     "phi": "024", "ll_slug": "cael",
     "location": "Rome",
     "notes": "Defence of Caelius Rufus on multiple charges; the speech famously paints Clodia (\"Lesbia\") in scathing terms."},

    {"id": "de-provinciis-consularibus", "title_latin": "De Provinciis Consularibus",
     "title_english": "On the Consular Provinces",
     "year": 56, "month": 6, "day": None, "precision": "month",
     "phi": "025", "ll_slug": "prov",
     "location": "Rome",
     "notes": "Senatorial speech supporting the extension of Caesar's command in Gaul."},

    {"id": "pro-balbo", "title_latin": "Pro L. Cornelio Balbo",
     "title_english": "For Lucius Cornelius Balbus",
     "year": 56, "month": None, "day": None, "precision": "year",
     "phi": "026", "ll_slug": "balbo",
     "location": "Rome",
     "notes": "Defence of Balbus on a challenge to his Roman citizenship; alongside Pompey and Crassus."},

    {"id": "in-pisonem", "title_latin": "In Pisonem",
     "title_english": "Against Piso",
     "year": 55, "month": None, "day": None, "precision": "year",
     "phi": "027", "ll_slug": "pis",
     "location": "Rome",
     "notes": "Invective against L. Calpurnius Piso, consul of 58 BC and one of the architects of Cicero's exile."},

    {"id": "pro-plancio", "title_latin": "Pro Cn. Plancio",
     "title_english": "For Gnaeus Plancius",
     "year": 54, "month": None, "day": None, "precision": "year",
     "phi": "028", "ll_slug": "planc",
     "location": "Rome",
     "notes": "Defence of Plancius on electoral bribery charges; warm thanks to Plancius for sheltering Cicero in exile."},

    {"id": "pro-scauro", "title_latin": "Pro M. Aemilio Scauro",
     "title_english": "For Marcus Aemilius Scaurus",
     "year": 54, "month": None, "day": None, "precision": "year",
     "phi": "029", "ll_slug": "scaur",
     "location": "Rome",
     "notes": "Defence of Scaurus on extortion charges from Sardinia. Survives only in fragments."},

    {"id": "pro-rabirio-postumo", "title_latin": "Pro C. Rabirio Postumo",
     "title_english": "For Gaius Rabirius Postumus",
     "year": 54, "month": None, "day": None, "precision": "year_range",
     "year_end": 53,
     "phi": "030", "ll_slug": "rab.post",
     "location": "Rome",
     "notes": "Defence of Rabirius on a charge under the lex Iulia de repetundis arising from Ptolemy Auletes' restoration."},

    {"id": "pro-milone", "title_latin": "Pro T. Annio Milone",
     "title_english": "For Titus Annius Milo",
     "year": 52, "month": 4, "day": None, "precision": "month",
     "phi": "031", "ll_slug": "milo",
     "location": "Rome",
     "notes": "Defence of Milo for the killing of Clodius on the Appian Way. The published version differs from what Cicero managed to deliver."},

    {"id": "pro-marcello", "title_latin": "Pro M. Marcello",
     "title_english": "For Marcus Marcellus",
     "year": 46, "month": 9, "day": None, "precision": "month",
     "phi": "032", "ll_slug": "marc",
     "location": "Rome",
     "notes": "Speech of thanks to Caesar for pardoning M. Marcellus. The first of the three \"Caesarian\" speeches."},

    {"id": "pro-ligario", "title_latin": "Pro Q. Ligario",
     "title_english": "For Quintus Ligarius",
     "year": 46, "month": 11, "day": None, "precision": "month",
     "phi": "033", "ll_slug": "lig",
     "location": "Rome",
     "notes": "Plea before Caesar for the pardon of Q. Ligarius, charged with Pompeian sympathies."},

    {"id": "pro-rege-deiotaro", "title_latin": "Pro Rege Deiotaro",
     "title_english": "For King Deiotarus",
     "year": 45, "month": 11, "day": None, "precision": "month",
     "phi": "034", "ll_slug": "deio",
     "location": "Rome",
     "notes": "Defence before Caesar of King Deiotarus of Galatia against a charge of attempted assassination."},

    {"id": "philippic-1", "title_latin": "Philippica I",
     "title_english": "First Philippic",
     "year": 44, "month": 9, "day": 2, "precision": "day",
     "phi": "035", "speech_index": "1", "ll_slug": "phil1",
     "location": "Rome",
     "notes": "Senate speech criticising Antony's measures since the Ides of March."},

    {"id": "philippic-2", "title_latin": "Philippica II",
     "title_english": "Second Philippic",
     "year": 44, "month": 10, "day": None, "precision": "month",
     "phi": "035", "speech_index": "2", "ll_slug": "phil2",
     "location": "Rome",
     "notes": "Cicero's most famous invective; written and circulated in October–November 44 BC but never delivered."},

    {"id": "philippic-3", "title_latin": "Philippica III",
     "title_english": "Third Philippic",
     "year": 44, "month": 12, "day": 20, "precision": "day",
     "phi": "035", "speech_index": "3", "ll_slug": "phil3",
     "location": "Rome",
     "notes": "Senate speech approving the resistance of Octavian and Decimus Brutus to Antony."},

    {"id": "philippic-4", "title_latin": "Philippica IV",
     "title_english": "Fourth Philippic",
     "year": 44, "month": 12, "day": 20, "precision": "day",
     "phi": "035", "speech_index": "4", "ll_slug": "phil4",
     "location": "Rome",
     "notes": "Speech to the people the same day as the Third Philippic."},

    {"id": "philippic-5", "title_latin": "Philippica V",
     "title_english": "Fifth Philippic",
     "year": 43, "month": 1, "day": 1, "precision": "day",
     "phi": "035", "speech_index": "5", "ll_slug": "phil5",
     "location": "Rome",
     "notes": "Senate speech against negotiation with Antony, urging war."},

    {"id": "philippic-6", "title_latin": "Philippica VI",
     "title_english": "Sixth Philippic",
     "year": 43, "month": 1, "day": 4, "precision": "day",
     "phi": "035", "speech_index": "6", "ll_slug": "phil6",
     "location": "Rome",
     "notes": "Speech to the people reporting on the embassy to Antony."},

    {"id": "philippic-7", "title_latin": "Philippica VII",
     "title_english": "Seventh Philippic",
     "year": 43, "month": 1, "day": None, "precision": "month",
     "phi": "035", "speech_index": "7", "ll_slug": "phil7",
     "location": "Rome",
     "notes": "Senate speech in mid-January 43 BC against any peace with Antony."},

    {"id": "philippic-8", "title_latin": "Philippica VIII",
     "title_english": "Eighth Philippic",
     "year": 43, "month": 2, "day": 3, "precision": "day",
     "phi": "035", "speech_index": "8", "ll_slug": "phil8",
     "location": "Rome",
     "notes": "Senate speech distinguishing between civil war and a war against a public enemy."},

    {"id": "philippic-9", "title_latin": "Philippica IX",
     "title_english": "Ninth Philippic",
     "year": 43, "month": 2, "day": 4, "precision": "day",
     "phi": "035", "speech_index": "9", "ll_slug": "phil9",
     "location": "Rome",
     "notes": "Senate speech proposing public honours for the slain ambassador Servius Sulpicius Rufus."},

    {"id": "philippic-10", "title_latin": "Philippica X",
     "title_english": "Tenth Philippic",
     "year": 43, "month": 2, "day": None, "precision": "month",
     "phi": "035", "speech_index": "10", "ll_slug": "phil10",
     "location": "Rome",
     "notes": "Senate speech in support of M. Brutus' command in Macedonia."},

    {"id": "philippic-11", "title_latin": "Philippica XI",
     "title_english": "Eleventh Philippic",
     "year": 43, "month": 3, "day": None, "precision": "month",
     "phi": "035", "speech_index": "11", "ll_slug": "phil11",
     "location": "Rome",
     "notes": "Senate speech on the killing of Trebonius by Dolabella; proposes Cassius for a Syrian command."},

    {"id": "philippic-12", "title_latin": "Philippica XII",
     "title_english": "Twelfth Philippic",
     "year": 43, "month": 3, "day": None, "precision": "month",
     "phi": "035", "speech_index": "12", "ll_slug": "phil12",
     "location": "Rome",
     "notes": "Senate speech withdrawing Cicero's earlier offer to serve on a second embassy to Antony."},

    {"id": "philippic-13", "title_latin": "Philippica XIII",
     "title_english": "Thirteenth Philippic",
     "year": 43, "month": 3, "day": 20, "precision": "day",
     "phi": "035", "speech_index": "13", "ll_slug": "phil13",
     "location": "Rome",
     "notes": "Senate speech responding line by line to a letter from Antony to Hirtius and Octavian."},

    {"id": "philippic-14", "title_latin": "Philippica XIV",
     "title_english": "Philippica XIV",
     "year": 43, "month": 4, "day": 21, "precision": "day",
     "phi": "035", "speech_index": "14", "ll_slug": "phil14",
     "location": "Rome",
     "notes": "Senate speech after the news of the victory at Forum Gallorum; the last surviving speech."},
]


# ---------------------------------------------------------------------------
# RHETORICAL WORKS — 7 surviving (counting De Oratore as a single work).
# ---------------------------------------------------------------------------
RHETORIC: list[dict[str, Any]] = [
    {"id": "de-inventione", "title_latin": "De Inventione",
     "title_english": "On Invention",
     "year": 85, "month": None, "day": None, "precision": "year_range",
     "year_end": 84,
     "phi": "036", "ll_slug": "inventione",
     "location": "Rome",
     "notes": "Cicero's earliest surviving work; a youthful rhetorical handbook in two books, which he later disowned."},

    {"id": "de-oratore", "title_latin": "De Oratore",
     "title_english": "On the Orator",
     "year": 55, "month": None, "day": None, "precision": "year",
     "phi": "037", "ll_slug": "oratore",
     "location": "Rome / Tusculum",
     "notes": "Three-book dialogue on the ideal orator, set in 91 BC; Cicero's mature rhetorical theory."},

    {"id": "partitiones-oratoriae", "title_latin": "Partitiones Oratoriae",
     "title_english": "The Subdivisions of Oratory",
     "year": 54, "month": None, "day": None, "precision": "year_range",
     "year_end": 46,
     "phi": "038", "ll_slug": "partitione",
     "location": "Rome",
     "notes": "Catechistic dialogue with his son on rhetorical theory; date disputed (somewhere between c. 54 and 46 BC)."},

    {"id": "brutus", "title_latin": "Brutus",
     "title_english": "Brutus",
     "year": 46, "month": 4, "day": None, "precision": "month",
     "phi": "039", "ll_slug": "brut",
     "location": "Rome",
     "notes": "Dialogue tracing the history of Roman oratory from its origins to Cicero's own day."},

    {"id": "orator", "title_latin": "Orator ad M. Brutum",
     "title_english": "Orator: To Marcus Brutus",
     "year": 46, "month": 9, "day": None, "precision": "month",
     "phi": "040", "ll_slug": "orator",
     "location": "Rome",
     "notes": "Treatise on the ideal orator and prose rhythm, addressed to M. Brutus."},

    {"id": "de-optimo-genere-oratorum", "title_latin": "De Optimo Genere Oratorum",
     "title_english": "On the Best Kind of Orators",
     "year": 46, "month": None, "day": None, "precision": "year",
     "phi": "041", "ll_slug": "opt.gen",
     "location": "Rome",
     "notes": "Preface to Cicero's now-lost translations of Demosthenes' and Aeschines' speeches On the Crown."},

    {"id": "topica", "title_latin": "Topica ad C. Trebatium",
     "title_english": "Topics: To Gaius Trebatius",
     "year": 44, "month": 7, "day": None, "precision": "month",
     "phi": "042", "ll_slug": "topica",
     "location": "Rhegium / shipboard",
     "notes": "Treatise on the loci of argumentation, written from memory en route to Greece in summer 44 BC."},
]


# ---------------------------------------------------------------------------
# PHILOSOPHICAL WORKS — 18 entries (15 prose treatises plus 3 poetic /
# fragmentary works classified here for shelving). Several survive only in
# fragments. Multi-book treatises (De Re Publica, De Legibus, Academica,
# De Finibus, Tusculanae Disputationes, De Natura Deorum, De Divinatione,
# De Officiis) get one entry; book divisions live inside the file.
# ---------------------------------------------------------------------------
PHILOSOPHY: list[dict[str, Any]] = [
    {"id": "aratea", "title_latin": "Aratea",
     "title_english": "Aratea (Translation of Aratus' Phaenomena)",
     "year": 86, "month": None, "day": None, "precision": "year_range",
     "year_end": 84,
     "phi": "", "no_perseus": True, "ll_slug": "aratea",
     "location": "Rome",
     "notes": "Cicero's youthful Latin verse translation of Aratus' Phaenomena; surviving in extensive fragments. Dated to his teens or early twenties."},

    {"id": "de-re-publica", "title_latin": "De Re Publica",
     "title_english": "On the Commonwealth",
     "year": 54, "month": None, "day": None, "precision": "year_range",
     "year_end": 51,
     "phi": "043", "ll_slug": "repub",
     "location": "Cumae / Rome",
     "notes": "Six-book dialogue on the ideal state, surviving in fragments and the famous Somnium Scipionis. Composed 54-51 BC, published 51 BC."},

    {"id": "de-consulatu-suo", "title_latin": "De Consulatu Suo",
     "title_english": "On His Consulship",
     "year": 60, "month": None, "day": None, "precision": "year",
     "phi": "", "no_perseus": True, "ll_slug": "cons.suo",
     "location": "Rome",
     "notes": "Autobiographical poem in three books on Cicero's consulship; survives in fragments quoted by Cicero himself."},

    {"id": "de-temporibus-suis", "title_latin": "De Temporibus Suis",
     "title_english": "On His Times",
     "year": 54, "month": None, "day": None, "precision": "year",
     "phi": "", "no_perseus": True, "ll_slug": "temp.suo",
     "location": "Rome",
     "notes": "Poem in three books on Cicero's exile and return; survives only in a few fragments."},

    {"id": "de-legibus", "title_latin": "De Legibus",
     "title_english": "On the Laws",
     "year": 52, "month": None, "day": None, "precision": "year_range",
     "year_end": 43,
     "phi": "044", "ll_slug": "leg",
     "location": "Arpinum / Rome",
     "notes": "Three-book dialogue on legal philosophy, begun c. 52 BC; left unfinished. Probably not published in Cicero's lifetime."},

    {"id": "paradoxa-stoicorum", "title_latin": "Paradoxa Stoicorum",
     "title_english": "Stoic Paradoxes",
     "year": 46, "month": None, "day": None, "precision": "year",
     "phi": "047", "ll_slug": "para",
     "location": "Rome",
     "notes": "Six brief essays expounding Stoic paradoxes for a Roman audience; dedicated to Brutus."},

    {"id": "consolatio", "title_latin": "Consolatio",
     "title_english": "Consolation",
     "year": 45, "month": 3, "day": None, "precision": "month",
     "phi": "", "no_perseus": True, "ll_slug": "consol",
     "location": "Astura",
     "notes": "Self-consolation written after the death of his daughter Tullia in February 45 BC; survives only in fragments."},

    {"id": "hortensius", "title_latin": "Hortensius",
     "title_english": "Hortensius",
     "year": 45, "month": None, "day": None, "precision": "year",
     "phi": "", "no_perseus": True, "ll_slug": "hort",
     "location": "Rome",
     "notes": "Protreptic dialogue on philosophy; survives only in fragments. Famously inspired Augustine's conversion to philosophy."},

    {"id": "academica", "title_latin": "Academica",
     "title_english": "Academica",
     "year": 45, "month": 5, "day": None, "precision": "month",
     "phi": "045", "ll_slug": "academ",
     "location": "Tusculum / Rome",
     "notes": "Dialogue on epistemology in two redactions: the 'Academica Posteriora' (Books I-II of the Lucullus / Catulus pair) and the 'Academica Priora' (Books I-IV of the Varro pair). Both survive in part."},

    {"id": "de-finibus", "title_latin": "De Finibus Bonorum et Malorum",
     "title_english": "On the Ends of Good and Evil",
     "year": 45, "month": 6, "day": None, "precision": "month",
     "phi": "048", "ll_slug": "fin",
     "location": "Tusculum / Rome",
     "notes": "Five-book dialogue presenting the chief Greek schools on the highest good. Dedicated to Brutus."},

    {"id": "tusculanae-disputationes", "title_latin": "Tusculanae Disputationes",
     "title_english": "Tusculan Disputations",
     "year": 45, "month": 8, "day": None, "precision": "month",
     "phi": "049", "ll_slug": "tusc",
     "location": "Tusculum",
     "notes": "Five-book treatise on death, pain, distress, the passions, and whether virtue suffices for happiness. Dedicated to Brutus."},

    {"id": "de-natura-deorum", "title_latin": "De Natura Deorum",
     "title_english": "On the Nature of the Gods",
     "year": 45, "month": 8, "day": None, "precision": "month",
     "phi": "050", "ll_slug": "nd",
     "location": "Rome",
     "notes": "Three-book dialogue presenting Epicurean, Stoic, and Academic theology; dedicated to Brutus."},

    {"id": "timaeus", "title_latin": "Timaeus",
     "title_english": "Timaeus (Latin translation)",
     "year": 45, "month": None, "day": None, "precision": "year",
     "phi": "072", "ll_slug": "timaeus",
     "location": "Rome",
     "notes": "Cicero's partial Latin translation of Plato's Timaeus; survives only in fragments."},

    {"id": "cato-maior-de-senectute", "title_latin": "Cato Maior de Senectute",
     "title_english": "Cato the Elder, On Old Age",
     "year": 44, "month": 4, "day": None, "precision": "month",
     "phi": "051", "ll_slug": "senec",
     "location": "Rome",
     "notes": "Dialogue on old age, set in 150 BC with Cato the Elder as principal speaker. Dedicated to Atticus."},

    {"id": "de-divinatione", "title_latin": "De Divinatione",
     "title_english": "On Divination",
     "year": 44, "month": 4, "day": None, "precision": "month",
     "phi": "053", "ll_slug": "div",
     "location": "Rome",
     "notes": "Two-book dialogue between Cicero and his brother Quintus on whether divination is a real art. Begun before, finished after, the Ides of March."},

    {"id": "de-fato", "title_latin": "De Fato",
     "title_english": "On Fate",
     "year": 44, "month": 5, "day": None, "precision": "month",
     "phi": "054", "ll_slug": "fato",
     "location": "Puteoli",
     "notes": "Dialogue on causation and free will; survives in part."},

    {"id": "laelius-de-amicitia", "title_latin": "Laelius de Amicitia",
     "title_english": "Laelius, On Friendship",
     "year": 44, "month": 7, "day": None, "precision": "month",
     "phi": "052", "ll_slug": "amic",
     "location": "Rome",
     "notes": "Dialogue on friendship, set in 129 BC after the death of Scipio Aemilianus. Dedicated to Atticus."},

    {"id": "de-officiis", "title_latin": "De Officiis",
     "title_english": "On Duties",
     "year": 44, "month": 11, "day": None, "precision": "month",
     "phi": "055", "ll_slug": "off",
     "location": "Puteoli / Tusculum",
     "notes": "Three-book ethical treatise addressed to his son Marcus; Cicero's last completed prose work."},
]


# ---------------------------------------------------------------------------
# LETTERS — generated programmatically by traditional book.letter numbering.
#
# The four collections (Ad Atticum, Ad Familiares, Ad Quintum Fratrem, Ad M.
# Brutum) total roughly 900 surviving letters. Traditional numbering is what
# scholars cite; Shackleton Bailey's chronological renumbering is recorded as
# a cross-reference in `notes` once verified.
#
# Dates assigned here are book-level approximations sufficient to order the
# corpus chronologically. Every letter entry carries `date_precision: year`
# (or `year_range`) and a uniform note flagging that exact dating requires
# refinement against SB's commentary or another standard chronological table.
#
# Tuple format: (collection, book, n_letters, year_start, year_end,
#                book_summary)
# ---------------------------------------------------------------------------

ATTICUM_BOOKS: list[tuple[int, int, int, int, str]] = [
    (1, 20, -68, -65, "Early letters: 68-65 BC, before the consulship."),
    (2, 25, -60, -59, "Letters of 60-59 BC: after the consulship; the early triumvirate."),
    (3, 27, -58, -57, "Exile correspondence: April 58 BC to August 57 BC."),
    (4, 19, -57, -54, "Letters of 57-54 BC: return from exile and political adjustment."),
    (5, 21, -51, -51, "Letters of 51 BC: departure for and journey to the governorship of Cilicia."),
    (6, 9, -50, -50, "Letters of 50 BC: end of the Cilician governorship and return to Italy."),
    (7, 26, -50, -49, "Letters of late 50 to early 49 BC: the approach to civil war."),
    (8, 16, -49, -49, "Letters of January-March 49 BC: outbreak of the civil war."),
    (9, 19, -49, -49, "Letters of March-April 49 BC: indecision over joining Pompey."),
    (10, 18, -49, -49, "Letters of May-June 49 BC: leaving Italy for Pompey's camp."),
    (11, 25, -48, -47, "Letters of 48-47 BC: from after Pharsalus through Cicero's stay at Brundisium."),
    (12, 53, -46, -45, "Letters of 46-45 BC, especially after the death of Tullia in February 45 BC."),
    (13, 52, -45, -45, "Letters of 45 BC, mostly from Tusculum during composition of the philosophical works."),
    (14, 22, -44, -44, "Letters of April-May 44 BC: the weeks after the Ides of March."),
    (15, 29, -44, -44, "Letters of May-July 44 BC."),
    (16, 16, -44, -44, "Letters of July-November 44 BC, the last of the Atticus correspondence."),
]

FAMILIARES_BOOKS: list[tuple[int, int, int, int, str]] = [
    (1, 10, -56, -54, "Correspondence with P. Lentulus Spinther, mostly on the Ptolemy Auletes affair."),
    (2, 19, -53, -50, "Various correspondents: C. Curio, M. Caelius Rufus, Appius Pulcher; touching the run-up to civil war."),
    (3, 13, -53, -50, "Correspondence with Appius Claudius Pulcher on the Cilician handover."),
    (4, 15, -46, -43, "Various, including the consolatory letter of Servius Sulpicius Rufus and Cicero's reply."),
    (5, 21, -62, -44, "Various correspondents: Pompey, Antony, Vatinius, Lucceius, Cato, M. Marius."),
    (6, 22, -47, -45, "Letters to Caesarian and Pompeian friends after Pharsalus."),
    (7, 33, -54, -44, "Letters chiefly to C. Trebatius Testa, M. Marius, M. Fabius Gallus."),
    (8, 17, -51, -50, "Letters of M. Caelius Rufus to Cicero in Cilicia: Roman political news."),
    (9, 26, -46, -44, "Letters chiefly to L. Papirius Paetus and M. Terentius Varro."),
    (10, 35, -44, -43, "Correspondence with L. Munatius Plancus, governor of Transalpine Gaul."),
    (11, 29, -43, -43, "Correspondence with Decimus Brutus during the war of Mutina."),
    (12, 30, -44, -43, "Letters to and from Cassius, M. Brutus, Trebonius, Cornificius, after the Ides."),
    (13, 79, -54, -44, "Letters of recommendation, scattered across many years."),
    (14, 24, -58, -47, "Letters to Terentia, Tullia, and the family."),
    (15, 21, -54, -43, "Various: Cato, Lentulus, Cassius, Hirtius, Pansa."),
    (16, 27, -54, -44, "Letters to and concerning Tiro."),
]

QUINTUM_BOOKS: list[tuple[int, int, int, int, str]] = [
    (1, 4, -60, -59, "Letters to Quintus, propraetor in Asia."),
    (2, 16, -56, -54, "Letters during Quintus' service in Sardinia and Gaul."),
    (3, 9, -54, -54, "Letters to Quintus serving on Caesar's staff in Gaul."),
]

BRUTUM_BOOKS: list[tuple[int, int, int, int, str]] = [
    (1, 18, -43, -43, "Correspondence between Cicero and M. Brutus, April–July 43 BC."),
    (2, 8, -43, -43, "Further correspondence with Brutus, spring 43 BC. Several letters in Book II are lost; surviving total across both books is about 26."),
]

LETTER_NOTE = (
    "Date assigned at book-level precision; exact dating to be refined against "
    "Shackleton Bailey's chronological commentary or another standard reference."
)


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def _speech_entry(s: dict[str, Any]) -> dict[str, Any]:
    year = bc(s["year"])
    paths = file_paths("speeches", year, s["id"])
    src_url = perseus_url(s["phi"]) if s["phi"] and not s.get("no_perseus") else None
    entry: dict[str, Any] = {
        "id": s["id"],
        "title_latin": s["title_latin"],
        "title_english": s["title_english"],
        "category": "speeches",
        "date": fmt_date(year, s.get("month"), s.get("day")),
        "date_precision": s["precision"],
        "location_written": s.get("location", "Rome"),
        "latin_source_url": src_url,
        "latin_source_url_fallback": latin_library_url(s["ll_slug"]),
        **paths,
        "status": "pending",
        "notes": s["notes"],
    }
    if s.get("speech_index"):
        entry["speech_index"] = s["speech_index"]
    if s["precision"] == "year_range" and s.get("year_end"):
        entry["date_range_end"] = fmt_date(bc(s["year_end"]), 12, 31)
    return entry


def _treatise_entry(s: dict[str, Any], category: str) -> dict[str, Any]:
    year = bc(s["year"])
    paths = file_paths(category, year, s["id"])
    src_url = perseus_url(s["phi"]) if s["phi"] and not s.get("no_perseus") else None
    entry: dict[str, Any] = {
        "id": s["id"],
        "title_latin": s["title_latin"],
        "title_english": s["title_english"],
        "category": category,
        "date": fmt_date(year, s.get("month"), s.get("day")),
        "date_precision": s["precision"],
        "location_written": s.get("location", "Rome"),
        "latin_source_url": src_url,
        "latin_source_url_fallback": latin_library_url(s["ll_slug"]),
        **paths,
        "status": "pending",
        "notes": s["notes"],
    }
    if s.get("speech_index"):
        entry["speech_index"] = s["speech_index"]
    if s["precision"] == "year_range" and s.get("year_end"):
        entry["date_range_end"] = fmt_date(bc(s["year_end"]), 12, 31)
    return entry


def _letter_entries(
    collection_slug: str,
    collection_title: str,
    books: list[tuple[int, int, int, int, str]],
    ll_root: str,
) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for book, n, year_start, year_end, summary in books:
        for letter in range(1, n + 1):
            work_id = f"{collection_slug}-{book:02d}-{letter:02d}"
            # Use the earlier year for sorting; year_range carried in metadata.
            sort_year = year_start
            paths = file_paths("letters", sort_year, work_id)
            precision = "year" if year_start == year_end else "year_range"
            entry: dict[str, Any] = {
                "id": work_id,
                "title_latin": f"{collection_title} {book}.{letter}",
                "title_english": f"{collection_title} {book}.{letter}",
                "category": "letters",
                "date": fmt_date(sort_year),
                "date_precision": precision,
                "location_written": None,
                "recipient": None,
                "latin_source_url": latin_library_url(f"{ll_root}{book}"),
                "latin_source_url_fallback": latin_library_url(f"{ll_root}{book}"),
                **paths,
                "status": "pending",
                "notes": f"{summary} {LETTER_NOTE}",
            }
            if precision == "year_range":
                entry["date_range_end"] = fmt_date(year_end, 12, 31)
            entries.append(entry)
    return entries


def build_corpus() -> list[dict[str, Any]]:
    works: list[dict[str, Any]] = []

    for s in SPEECHES:
        works.append(_speech_entry(s))

    for s in RHETORIC:
        works.append(_treatise_entry(s, "rhetoric"))

    for s in PHILOSOPHY:
        works.append(_treatise_entry(s, "philosophy"))

    works.extend(_letter_entries(
        collection_slug="ad-atticum",
        collection_title="Ad Atticum",
        books=ATTICUM_BOOKS,
        ll_root="att",
    ))
    works.extend(_letter_entries(
        collection_slug="ad-familiares",
        collection_title="Ad Familiares",
        books=FAMILIARES_BOOKS,
        ll_root="fam",
    ))
    works.extend(_letter_entries(
        collection_slug="ad-quintum-fratrem",
        collection_title="Ad Quintum Fratrem",
        books=QUINTUM_BOOKS,
        ll_root="qfr",
    ))
    works.extend(_letter_entries(
        collection_slug="ad-brutum",
        collection_title="Ad M. Brutum",
        books=BRUTUM_BOOKS,
        ll_root="brut",
    ))

    works.sort(key=_chronological_key)
    return works


def _chronological_key(w: dict[str, Any]) -> tuple[int, int, int, str]:
    """Return a (year, month, day, id) tuple that orders BC → AD correctly.

    Lexicographic sorting on the ISO-with-negative-year strings puts -0043
    before -0081 because "4" < "8". We need to parse the year as a signed int.
    """
    date_str: str = w["date"]
    if date_str.startswith("-"):
        year_part, rest = date_str[1:].split("-", 1)
        year = -int(year_part)
    else:
        year_part, rest = date_str.split("-", 1)
        year = int(year_part)
    month_str, day_str = rest.split("-")
    return (year, int(month_str), int(day_str), w["id"])


def main() -> int:
    works = build_corpus()
    WORKS_YAML.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# meta/works.yaml — chronological master index for cicero-by-claude.\n"
        "# Generated by scripts/seed_works.py. Hand-edit freely after generation;\n"
        "# the seed script is intended for the initial population only.\n"
        "#\n"
        "# date format: ISO-like with negative year for BC.\n"
        "# date_precision: day | month | year | year_range\n"
        "# Letter dates are book-level approximations and should be refined.\n"
        "\n"
    )
    yaml_text = yaml.safe_dump(works, sort_keys=False, allow_unicode=True, width=100)
    WORKS_YAML.write_text(header + yaml_text, encoding="utf-8")
    print(f"Wrote {len(works)} works to {WORKS_YAML.relative_to(REPO)}")

    by_cat: dict[str, int] = {}
    for w in works:
        by_cat[w["category"]] = by_cat.get(w["category"], 0) + 1
    for cat, n in sorted(by_cat.items()):
        print(f"  {cat:12s} {n:4d}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



