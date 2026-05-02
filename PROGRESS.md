# Progress

This file tracks the state of the translation effort. Auto-generated entries
are derived from `meta/works.yaml`; the prose summary at the top is hand-edited
as milestones are reached.

## Status summary

- **Drafted**: 26 speeches end-to-end --- *Pro Quinctio* (81 BC),
  *Pro Roscio Amerino* (80 BC), *Pro Roscio Comoedo* (~76 BC),
  *Pro Tullio* (71 BC), *Divinatio in Caecilium* (Jan 70 BC),
  *In Verrem Actio Prima* (5 Aug 70 BC), the entire five-book
  *Actio Secunda* (I--V; autumn 70 BC), *Pro Caecina* (69 BC),
  *Pro Fonteio* (69 BC), *Pro Lege Manilia* (66 BC), *Pro
  Cluentio* (66 BC, the longest forensic speech in the corpus),
  the entire 63 BC consular corpus --- *Pro Rabirio Perduellionis
  Reo*, the three surviving *De Lege Agraria*, the four
  *Catilinarians*, and *Pro Murena* --- and the two 62 BC
  defences, *Pro Sulla* (mid-62 BC) and *Pro Archia* (summer 62
  BC). *Pro Flacco* (59 BC) is partly drafted: sections 1--5
  plus the Bobiensian fragments are committed; sections 6--106
  remain.
- **In progress**: *Pro Flacco* (59 BC), parked at section 5
  pending the chronological catch-up of the letters.
- **Reviewed**: 0
- **Final**: 0
- **Pending**: 930 entries.

### The chronological situation, plainly stated

The 26 drafted speeches are in correct relative order **among
themselves**, but the previous three sessions translated only
speeches; **letters, philosophical works, and rhetorical works
were skipped over silently** in the chronological sweep. As of
the dating refresh that produced this section, the chronology
across all four categories looks like this:

  * 873 letters, all dated against Perseus's TEI ``<date when=...>``
    attributes and dateline parsing (Roman calendar phrases:
    ``Kal.``/``Non.``/``Id.``, ``a. d. III Kal. Mart.``, ``prid.
    Kal. Iun.``, etc.); 548 of 863 parseable letters (~64%) now
    carry day precision, ~15% month precision, ~18% year-only;
    41 letters had no Perseus dateline and remain at year
    precision. URLs repointed to Perseus
    ``canonical-latinLit`` (phi056/057/058/059) with Latin
    Library as fallback per book.
  * 25 philosophy and rhetoric works similarly. URLs repointed to
    the correct phi numbers (phi036--055, plus phi072 for
    *Timaeus*); five remain ``no_perseus`` (Aratea, De Consulatu
    Suo, De Temporibus Suis, Hortensius, Consolatio); De Legibus
    is at the Latin Library only.
  * 32 pending speeches dated as before.

The earliest pending work in the corpus is now *ad-atticum-01-06*
(15 January 67 BC). Everything in 67 BC, 66 BC, 65 BC, 62 BC, 61
BC, and 60 BC that is **letters or philosophy/rhetoric** sits in
the gap between drafted speeches and the resume point, and must
be translated in date order, not skipped past.

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

- Letter dating refinement: dates have been pulled from Perseus's TEI
  ``<seg rend="dateline">`` text and parsed via `scripts/refresh_letter_dates.py`.
  548 / 863 letters carry day precision, ~15% month, the rest year. A
  later editorial pass against Shackleton Bailey can tighten the year-only
  ones. Re-running the script is idempotent (Perseus's metadata doesn't
  change unless the corpus is updated).
- Six works lack a Perseus source: Aratea, De Consulatu Suo, De
  Temporibus Suis, Hortensius, Consolatio (all fragmentary), and De
  Legibus (whole; only at thelatinlibrary.com). When the chronology
  reaches one of these, the Latin source must be supplied manually.
- The `In Verrem` Actio Secunda books, Catilinarians, Philippics, and
  Agrarians share a single Perseus XML file each; `fetch_latin.py` selects
  individual speeches via the `speech_index` field on each entry. The
  same mechanism is now used for letters: each letter entry carries a
  ``speech_index: book:N,letter:M`` pointer into the corresponding letter
  corpus.

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

- **Branching: `main` is the durable tip.** The web harness assigns a
  freshly-named branch (`claude/setup-cicero-project-fLUZH-<random>`)
  at the start of every session. Do **not** treat that branch as the
  source of truth --- it is a sandbox. The source of truth is
  `origin/main`. Every session begins by running
  `bash scripts/session_start.sh`, which fast-forwards the session
  branch to `origin/main` if needed and prints the chronologically-next
  pending work. Every session ends by running
  `bash scripts/session_end.sh`, which pushes the session branch and
  fast-forwards `origin/main` to the same tip. This means a new session
  --- whatever its assigned branch name --- can start work immediately
  from `main` and never has to hunt for the latest state.
  Note: the harness's git server refuses branch deletions, so old
  session branches accumulate on origin. They are harmless (strict
  ancestors of `main` with no unique commits). Alexander can prune
  them via the GitHub web UI at any time; agents should leave them
  alone.
- **Continuous mode.** Translate forward chronologically without pausing
  for per-work approval. Commit and push per finished work; for long works,
  commit at section boundaries (~30--50 sections) so progress is durable.
- **Chronologically next means across all categories.** "The next pending
  work" is the chronologically earliest entry in `meta/works.yaml` whose
  status is `pending`, regardless of category. Letters, speeches,
  philosophical works, and rhetorical works all interleave by date. The
  previous practice of advancing through speeches alone is **explicitly
  retired**, and `scripts/validate.py` carries a chronological-gap warning
  that fires whenever any pending work is dated earlier than the latest
  drafted work --- run it at the start and end of every session.
- **Batch shape.** Adaptive --- whichever comes first: end of work, or
  ~30--50 sections. Short works (letters, especially) finish in one batch;
  long works are split at section boundaries.
- **Timeout discipline.** Write each long translation in halves and commit
  between halves, so an Anthropic API stream timeout costs at most half a
  chunk. Latin-source files are committed before translation begins.
- **Letters** use the `\begin{ciceroletter}` LaTeX environment (which the
  assemble script already wires up); the dateline goes in italic small
  caps above the body. The Perseus-extracted dateline is preserved as a
  `% Dateline (Perseus): ...` comment at the top of the Latin file;
  `\ciceroLetterOpener{salute}` carries the Latin salutation (e.g.
  `CICERO ATTICO salutem`) into the head of section 1.
- **Aratea (86 BC) and De Inventione (85 BC) deferred.** They precede
  *Pro Quinctio* chronologically but were skipped because *Pro Quinctio*
  was the agreed test case. Treat them as a deliberate later-pass; do not
  circle back at the start of a continuation. The chronology re-sorts
  correctly at build time once they are translated. The validator
  excludes them from the chronological-gap warning.
- **No-Perseus works.** Five works lack a Perseus source (Aratea,
  De Consulatu Suo, De Temporibus Suis, Hortensius, Consolatio); De
  Legibus is at the Latin Library only. When the chronology reaches one
  of these, the Latin source must be supplied manually before the
  translation pass.
- **Translator's voice.** Strict adherence to `STYLE.md`. The collaborator's
  name is **Alexander Woods** (never abbreviated). The front-matter note
  *Why this exists* is Alexander's words and should not be edited.
- **What "done" looks like for a single work.** Latin file fetched and
  committed; English file translated end-to-end against the Latin (not
  another translation); headnote written; `status` flipped to `drafted`
  in `meta/works.yaml`; `PROGRESS.md` updated; build pipeline run
  (`scripts/validate.py`, `scripts/build_manifest.py`,
  `scripts/assemble_book.py`); commit and push.

## Where to resume now

The current resume point is ***Ad Atticum 1.6*** (15 January 67
BC), Cicero in his praetor-elect year writing to Atticus at
Athens. Forward from there in strict chronological order across
all categories (letters, speeches, philosophy, rhetoric):

- **67--62 BC** --- the early Atticus letters (Att 1.5--1.11
  plus 1.1--1.4, in date order, not manuscript order: Perseus's
  dateline parsing has rearranged them) interleave with the
  drafted speeches *Pro Lege Manilia* (66 BC), *Pro Cluentio*
  (66 BC), the four 63 BC consular speeches, *Pro Murena*
  (Nov 63 BC), *Pro Sulla* (mid-62 BC), *Pro Archia* (summer
  62 BC). The drafted speeches keep their `drafted` status; the
  letters of those years fill in the gaps.
- **61--58 BC** --- the body of *Ad Atticum* book 1 closing,
  *Ad Atticum* book 2 (the Bona Dea letters, the Vettius
  affair, the gathering crisis of 59 BC), the bulk of Cicero's
  exile correspondence in 58 BC. *Pro Flacco* (mid-59 BC)
  resumes from section 6 when its date is reached.
- **57--52 BC** --- the post-exile speeches *Pro Sestio*, *In
  Vatinium*, *De Provinciis Consularibus*, *Pro Caelio*, *De
  Domo Sua*, *De Haruspicum Responso*, *Pro Plancio*, *Pro
  Rabirio Postumo*, *Pro Milone*, with *De Oratore* (55 BC),
  *De Re Publica* (54 BC), *De Legibus* (52 BC) and the great
  triple letter book of 54 BC interleaved.
- **51--47 BC** --- the Cilician proconsulship and the civil
  war, with *Ad Familiares* and *Ad Atticum* and *Ad Quintum
  Fratrem* dense throughout.
- **46--43 BC** --- the philosophical torrent (*Brutus*,
  *Orator*, *Academica*, *De Finibus*, *Tusculanae*, *De
  Natura Deorum*, *De Divinatione*, *De Senectute*, *De
  Amicitia*, *De Officiis*), the late forensic speeches (*Pro
  Marcello*, *Pro Ligario*, *Pro Rege Deiotaro*), the 14
  *Philippics*, and the dense final-year letters of 44--43 BC,
  closing on *Ad M. Brutum* and Cicero's death at Formiae in
  December 43 BC.

Run `scripts/validate.py` at the start of each session: a
non-zero count of "earlier-pending" warnings means the
chronological sweep has skipped something and must double back.

## Generated index

A complete chronological table of contents lives in `MANIFEST.md` and is
regenerated by `scripts/build_manifest.py` from `meta/works.yaml`.
