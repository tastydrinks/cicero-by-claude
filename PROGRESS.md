# Progress

This file tracks the state of the translation effort. Auto-generated entries
are derived from `meta/works.yaml`; the prose summary at the top is hand-edited
as milestones are reached.

## Status summary

- **Drafted**: 13 works --- *Pro Quinctio* (81 BC), *Pro Roscio Amerino*
  (80 BC), *Pro Roscio Comoedo* (~76 BC), *Pro Tullio* (71 BC),
  *Divinatio in Caecilium* (Jan 70 BC), *In Verrem Actio Prima*
  (5 Aug 70 BC), the entire five-book Actio Secunda (I-V; autumn 70
  BC), *Pro Caecina* (69 BC), and *Pro Fonteio* (69 BC). All
  awaiting human review.
- **In progress**: none.
- **Reviewed**: 0
- **Final**: 0
- **Pending**: 943 entries --- the rest of the speeches of the 60s
  (*Pro Lege Manilia*, *Pro Cluentio*, the Agrarians, the
  Catilinarians, *Pro Murena*), the speeches of the 50s and 40s,
  the 14 Philippics, the 7 rhetorical works, the 17 philosophical /
  poetic works (including *Aratea* (86 BC) and *De Inventione*
  (85 BC) which precede *Pro Quinctio* and were skipped because
  *Pro Quinctio* was the agreed test case), and the full letter
  corpus (873 letters organised by traditional book.letter numbering
  across Ad Atticum, Ad Familiares, Ad Quintum Fratrem, Ad M.
  Brutum).

## Milestones

- **Initial setup** *(complete)*: directory structure, top-level docs, full
  manifest in `meta/works.yaml` (956 entries), build scripts, LaTeX
  scaffolding, first speech translated end-to-end (*Pro Quinctio*, ~13.5k
  words of English from 99 sections of Latin), v0.1 PDF produced.
- **First continuous session** *(complete)*: 7 works fully drafted plus
  60/192 sections of *Verres II.2*. Roughly 80,000 English words of new
  Cicero translation. The arc from Cicero's earliest forensic work to
  the moment Verres withdrew into exile is largely covered (the four
  remaining Actio Secunda books are pending). Two infrastructure
  improvements landed in this session: the fetch script now strips TEI
  critical apparatus, and supports nested textpart selection
  (`speech_index: actio:2,book:5`) for the Verrines. Clickable PDF TOC
  via `hyperref` was also added.
- **Second continuous session** *(complete)*: the entire remaining
  Verrines corpus drafted end-to-end. *Verres II.2* (de iurisdictione,
  192 sections, of which 91-192 drafted in this session) closes with
  the Sthenius trial and its aftermath at Rome, the auctioning of
  Sicilian senatorships and priesthoods, the Cephaloedian
  intercalation, the censor scandal, the statue extortion, and the
  scriptura partnership's "Verrucius" forgery. *Verres II.3* (de re
  frumentaria, 228 sections, the longest of the five Actio Secunda
  books): Apronius the bagman, the destruction of the lex Hieronica,
  the assessed-grain swindle, the depopulation of the Sicilian
  plough-lands, the closing argument on Hortensius and the
  senatorial courts. *Verres II.4* (de signis, 151 sections): the
  Heius collection, the Cibyratan brothers, the candelabrum of
  Antiochus, the Diana of Segesta, the Mercury of Tyndaris and
  Sopater bound to Marcellus's statue, the temple of Hercules at
  Agrigentum, the Ceres of Henna, the parallel of the two takings
  of Syracuse. *Verres II.5* (de suppliciis, 189 sections): the
  pretended pirate war, Cleomenes and the Sicilian fleet burned at
  Helorus, the Achradina executions of the captains and the prison
  fees exacted from their parents, the Latomiae and the killing of
  Roman citizens veiled, and at the architectural climax the
  crucifixion of Publius Gavius of Consa on the Strait facing Italy
  --- *civis Romanus sum*. Eleven works drafted; the entire
  Verrines corpus complete in draft. Resume point moves to *Pro
  Caecina* (69 BC) and the speeches of the 60s.

## Known follow-ups

- Letter dating refinement: dates for the ~870 letters are at book-level
  precision and should be tightened against Shackleton Bailey's commentary.
- Five fragmentary works are flagged `no_perseus` because they are not in
  the Perseus / canonical-latinLit GitHub corpus: Aratea, De Consulatu Suo,
  De Temporibus Suis, Hortensius, Consolatio. These will need a manual
  Latin source.
- The `In Verrem` Actio Secunda books, Catilinarians, Philippics, and
  Agrarians share a single Perseus XML file each; `fetch_latin.py` selects
  individual speeches via the `speech_index` field on each entry.

## Working order

Translations proceed in strict chronological order, one work at a time. The
next work to translate is the chronologically earliest entry in
`meta/works.yaml` whose `status` is `pending`. (Or, if a work is `pending`
but partway through, finish it from where the most recent commit left off.)

After *Pro Quinctio* the queue continues with *Pro Roscio Amerino* (80 BC),
*Pro Roscio Comoedo* (~76 BC), then the *In Verrem* corpus (70 BC), and so
on through the speeches of the 60s and 50s, the philosophical works of the
mid-50s and mid-40s, and the letters interleaved throughout.

## Session handoff conventions

These are the working conventions agreed with Alexander Woods. A future
session can `continue` and apply them without re-asking:

- **Continuous mode.** Translate forward chronologically without pausing
  for per-work approval. Commit and push per finished work; for long works,
  commit at section boundaries (~30-50 sections) so progress is durable.
- **Batch shape.** Adaptive --- whichever comes first: end of work, or
  ~30-50 sections. Short works finish in one batch; long works are split
  at section boundaries.
- **Timeout discipline.** Write each long translation in halves and commit
  between halves, so an Anthropic API stream timeout costs at most half a
  chunk. Latin-source files are committed before translation begins.
- **Aratea (86 BC) and De Inventione (85 BC) deferred.** They precede
  *Pro Quinctio* chronologically but were skipped because *Pro Quinctio*
  was the agreed test case. Treat them as a deliberate later-pass; do not
  circle back at the start of a continuation. The chronology re-sorts
  correctly at build time once they are translated.
- **Translator's voice.** Strict adherence to `STYLE.md`. The collaborator's
  name is **Alexander Woods** (never abbreviated). The front-matter note
  *Why this exists* is Alexander's words and should not be edited.
- **What "done" looks like for a single work.** Latin file fetched and
  committed; English file translated end-to-end against the Latin (not
  another translation); headnote written; `status` flipped to `drafted`
  in `meta/works.yaml`; `PROGRESS.md` updated; PDF rebuilt; commit and
  push.

## Where to resume now

The current resume point is **Pro Cluentio (66 BC), section 1**
--- chronologically the next pending work after *Pro Fonteio*.
This is the longest of all Cicero's forensic speeches at 202
sections: the defence of Aulus Cluentius Habitus on charges
arising from the prosecution of his stepfather Oppianicus eight
years earlier (which Cicero argues had been a notoriously corrupt
trial, but in the wrong direction: Oppianicus had bribed first,
and Cluentius was being tried for poisoning him). Beware the
length; split at section boundaries (\textasciitilde 30-40 sections
per commit) per the timeout discipline below. *Pro Lege Manilia*
will likely have to be done in parallel as it dates 66 BC also,
but Pro Cluentio comes first in the queue. After Pro Cluentio:
the Agrarians (63 BC), the Catilinarians, *Pro Murena*, and
forward through the 60s.

## Generated index

A complete chronological table of contents lives in `MANIFEST.md` and is
regenerated by `scripts/build_manifest.py` from `meta/works.yaml`.
