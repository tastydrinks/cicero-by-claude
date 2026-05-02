# Progress

This file tracks the state of the translation effort. Auto-generated entries
are derived from `meta/works.yaml`; the prose summary at the top is hand-edited
as milestones are reached.

## Status summary

- **Drafted**: 24 works --- *Pro Quinctio* (81 BC), *Pro Roscio Amerino*
  (80 BC), *Pro Roscio Comoedo* (~76 BC), *Pro Tullio* (71 BC),
  *Divinatio in Caecilium* (Jan 70 BC), *In Verrem Actio Prima*
  (5 Aug 70 BC), the entire five-book Actio Secunda (I-V; autumn 70
  BC), *Pro Caecina* (69 BC), *Pro Fonteio* (69 BC), *Pro Lege
  Manilia* (66 BC), *Pro Cluentio* (66 BC, the longest forensic
  speech in the corpus), and the entire 63 BC consular corpus ---
  the three surviving *De Lege Agraria* (January 63 BC), *Pro
  Rabirio Perduellionis Reo* (early 63 BC), the four
  *Catilinarians* (8 Nov - 5 Dec 63 BC), and *Pro Murena*
  (late November 63 BC). All awaiting human review.
- **In progress**: none.
- **Reviewed**: 0
- **Final**: 0
- **Pending**: 932 entries --- *Pro Sulla* (62 BC), *Pro Archia*
  (62 BC), *Pro Flacco* (59 BC), the rest of the speeches of the
  50s and 40s, the 14 Philippics, the 7 rhetorical works, the 17
  philosophical / poetic works (including *Aratea* (86 BC) and
  *De Inventione* (85 BC) which precede *Pro Quinctio* and were
  skipped because *Pro Quinctio* was the agreed test case), and
  the full letter corpus (873 letters organised by traditional
  book.letter numbering across Ad Atticum, Ad Familiares, Ad
  Quintum Fratrem, Ad M. Brutum).

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
  --- *civis Romanus sum*. The session continued forward through
  the speeches of the 60s: *Pro Caecina* (104 sections, on the
  \textit{interdictum de vi armata}), *Pro Fonteio* (49 sections
  surviving from the mutilated text, defence of the former governor
  of Transalpine Gaul), *Pro Lege Manilia* (71 sections, Cicero's
  first political speech, supporting the Mithridatic command for
  Pompey), and *Pro Cluentio* (202 sections, the longest of the
  forensic speeches: the defence of Cluentius against poisoning
  charges and the eight-year shadow of the Junian trial; closing
  on the figure of his mother Sassia and the line ``in public
  meetings is the place of hatred, in trials of truth''). Fifteen
  works drafted. Resume point moves to the speeches of 63 BC ---
  the Agrarians, the Catilinarians, \textit{Pro Murena}.
- **Third continuous session** *(complete)*: the entire 63 BC
  consular corpus drafted end-to-end. *Pro Rabirio Perduellionis
  Reo* (38 sections, with textual lacunae in 31--35): the consul's
  defence of the elderly Rabirius against the revived perduellio
  charge for the killing of Saturninus in 100 BC --- a Caesarian
  assault not on one old senator but on the senatus consultum
  ultimum which Cicero would need within months. *De Lege
  Agraria I* (the surviving 27 sections plus four short fragments
  preserved by other authors): the senatorial speech against the
  Rullan agrarian bill on the Kalends of January, closing on the
  consul's renunciation of his province and the diagnosis
  *inclusum malum, intestinum ac domesticum*. *De Lege Agraria
  II* (103 sections): the principal contio speech, the new-man
  manifesto ``nothing so popular as peace, as liberty, as
  quiet,'' the decemviral imperium unfolded clause by clause as
  a kingship, and the great Capua digression on why our
  ancestors gutted from within the only three cities (Carthage,
  Corinth, Capua) capable of bearing the weight of empire.
  *De Lege Agraria III* (16 surviving sections of the speech, the
  second half lost): clause XL of the bill exposed --- the
  Marian/Carbo date is the consular dating of the year Sulla
  destroyed; the clause is a quiet amnesty more Sullan than
  Sulla, embracing even land merely *possessa* by force or
  stealth, with Rullus's father-in-law Valgius the prime
  beneficiary. The four **Catilinarians**: the first
  (8 November, in the temple of Jupiter Stator with Catiline
  present, opening *quo usque tandem* and turning on the two
  prosopopoeiae of the patria); the second (9 November, in the
  Forum, *abiit excessit evasit erupit* and the famous typology
  of the conspirators in six classes culminating in the
  ``praetorian cohort of harlots''); the third (3 December, in
  the Forum: the Mulvian Bridge ambush, Lentulus's seal,
  Cethegus's cache of swords, the new statue of Jupiter set up
  that very morning facing the Forum where the conspirators were
  marched in chains, the comparison with previous civil
  dissensions); the fourth (5 December, in the temple of
  Concord: the debate on the punishment of the conspirators in
  custody, with Cicero presiding as consul --- the analysis of
  Silanus's and Caesar's opinions, the roll-call of the orders,
  the catalogue of what the consul has refused for the city's
  sake, the commendation of his little son to the Senate). The
  conspirators were strangled in the Tullianum that night.
  *Pro Murena* (90 sections, late November 63 BC): the consul's
  defence of the consul-elect on canvassing charges brought
  under the consul's own bribery law, with the triptych on
  Murena's life, on soldiering and jurisprudence (the
  Sabine-farm dialogue, the joke that Cicero will declare
  himself a lawyer in three days), and on Cato's Stoicism (the
  parallel digression where Cicero with the most elaborate
  respect for Cato the man parodies Zenonian rigorism --- some
  study with Plato and Aristotle, he says, would have made Cato
  no better but a little gentler). Twenty-four works drafted.
  Resume point moves forward to *Pro Sulla* (62 BC) and *Pro
  Archia* (62 BC).

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

The current resume point is ***Pro Sulla*** (62 BC), the
defence of P. Cornelius Sulla (nephew of the dictator) on a
charge of involvement in the Catilinarian conspiracy --- a
case in which Cicero himself, having executed the conspirators
of December 63, must distinguish a man whose case is
defensible from those whose was not. Forward from there to
***Pro Archia*** (62 BC, on the citizenship of the poet Archias
of Antioch, the famous defence of letters); ***Pro Flacco***
(59 BC); the speeches of the 50s --- ***Pro Sestio***, ***In
Vatinium***, ***De Provinciis Consularibus***, ***Pro
Caelio***, ***De Domo Sua***, ***De Haruspicum Responso***,
***Pro Plancio***, ***Pro Rabirio Postumo***, ***Pro
Milone***, ***Pro Marcello***, ***Pro Ligario***, ***Pro Rege
Deiotaro*** --- the 14 ***Philippics*** of 44--43, and the
philosophical and rhetorical works that begin to be drafted in
earnest in the 50s and pour out in the 40s, with the letters
interleaved throughout.

## Generated index

A complete chronological table of contents lives in `MANIFEST.md` and is
regenerated by `scripts/build_manifest.py` from `meta/works.yaml`.
