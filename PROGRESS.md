# Progress

This file tracks the state of the translation effort. Auto-generated entries
are derived from `meta/works.yaml`; the prose summary at the top is hand-edited
as milestones are reached.

## Status summary

- **Drafted**: 904 / 958 works end-to-end across all categories (~94.4%). See "Where to resume now" below for the post-session-33 chronology pointer and next-batch suggestions. The prose summary that follows describes the project state through session 4 only (drafted=160 then); the current authoritative state is in "Where to resume now."

- **Drafted (legacy session-4 snapshot — see "Where to resume now" for current)**: 160 works end-to-end across all categories.
  - **Speeches (30)**: *Pro Quinctio* (81 BC), *Pro Roscio
    Amerino* (80 BC), *Pro Roscio Comoedo* (~76 BC),
    *Pro Tullio* (71 BC), *Divinatio in Caecilium* (Jan 70 BC),
    *In Verrem Actio Prima* (5 Aug 70 BC), the entire five-book
    *Actio Secunda* (I--V; autumn 70 BC), *Pro Caecina* (69 BC),
    *Pro Fonteio* (69 BC), *Pro Lege Manilia* (66 BC), *Pro
    Cluentio* (66 BC), the entire 63 BC consular corpus
    (\textit{Pro Rabirio Perduellionis Reo}, the three surviving
    \textit{De Lege Agraria}, the four \textit{Catilinarians},
    \textit{Pro Murena}), the two 62 BC defences
    (\textit{Pro Sulla}, \textit{Pro Archia}),
    \textit{Pro Flacco} (mid-59 BC), and the three speeches of
    September 57 BC marking the return from exile:
    \textit{Post Reditum in Senatu} (5 Sept), \textit{Post
    Reditum ad Quirites} (7 Sept), and \textit{De Domo Sua}
    (29 Sept --- before the College of Pontiffs, on the
    Palatine house).
  - **Letters (96)**: the early Atticus correspondence ---
    \textit{Att.} 1.1--1.20 (in chronological, not manuscript,
    order: 67--60 BC), \textit{Att.} 2.1--2.25 (60--late 59
    BC, including the Vettius affair and the closing of
    \textit{Att.} book 2 on the eve of Clodius's tribunate),
    \textit{Att.} 3.1--3.27 (April 58 BC -- end of January 57
    BC: the entire surviving exile correspondence with Atticus,
    from the journey south through Lucania to Brundisium, the
    crossing on 30 April, the long Thessalonican stretch,
    Dyrrachium, and the news of the failed early-January
    recall attempts), and \textit{Att.} 4.1--4.3 (mid-September
    to 26 November 57 BC --- return to Rome, the corn-supply
    crisis and Pompey's \textit{cura annonae}, the Senate
    proceedings on the house, and the November Clodian
    violence); the early Familiares --- \textit{Fam.} 5.1,
    5.2, 5.5, 5.6, 5.7, 7.23 (62 BC), \textit{Fam.} 5.4 (April
    57 BC to Metellus Nepos), \textit{Fam.} 5.17 (late 57 BC
    to Sittius); \textit{Fam.} 13.41, 13.42 (ca. early 58 BC
    to Culleolus), 13.43 (ca. late 59 BC to Quinctius Gallus),
    13.44 (ca. early 58 BC to Fadius Gallus); the family
    letters from exile \textit{Fam.} 14.1 (Dyrrachium, 25 Nov
    58), 14.2 (Thessalonica, 5 Oct 58), 14.3 (Dyrrachium, 29
    Nov 58), 14.4 (Brundisium, 30 April 58 --- the first letter
    to Terentia from exile); and the \textit{Ad Quintum
    Fratrem} sweep --- 1.1 (late 60/early 59 BC), 1.2 (late
    59 BC), 1.3 (Thessalonica, 13 June 58 --- the famous
    \textit{mi frater, mi frater, mi frater} letter), 1.4
    (Thessalonica, ca. 5 Aug 58), 2.1 (Rome, mid-Dec 57 BC,
    opening Q.fr. book 2).
- **Reviewed**: 0
- **Final**: 0
- **Pending**: 812 entries.

### The chronological situation

The chronology is now a clean single-thread sweep from
\textit{Pro Quinctio} (81 BC) through the end of 57 BC: through
all 27 surviving speeches up to \textit{Pro Flacco} (mid-59
BC), the entire exile and recovery correspondence
(\textit{Att.} 3.1--3.27 and 4.1--4.3, the four \textit{Fam.}
14 family letters, four \textit{Q. fr.} letters of the period,
\textit{Fam.} 5.4 to Metellus Nepos and \textit{Fam.} 5.17 to
Sittius, and the recommendation letters \textit{Fam.}
13.41--13.43), and the three speeches of September 57 BC that
mark the return: \textit{Post Reditum in Senatu}, \textit{Post
Reditum ad Quirites}, \textit{De Domo Sua}. The next
chronological items are \textit{Q. fr.} 2.4 and the long
correspondence of 56 BC opening with \textit{Ad Familiares}
book 1 (the Lentulus Spinther sequence on the Egyptian
question).

The dating infrastructure remains in place: Perseus's
\texttt{<date when="...">} attributes and dateline parsing
(\texttt{scripts/refresh\_letter\_dates.py}) supply the
chronology; \texttt{scripts/validate.py} reports a
chronological-gap warning if any pending work is dated earlier
than the latest drafted work; the validator excludes Aratea
(86 BC), De Inventione (85 BC), and the four other no\_perseus
fragmentary works (\textit{de-consulatu-suo} 60 BC,
\textit{de-temporibus-suis} 54 BC, \textit{Hortensius} 45 BC,
\textit{Consolatio} 45 BC) from the gap-check.

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
- **Fourth continuous session** *(complete)*: the entire
  exile and recovery arc drafted end-to-end. The Thessalonican
  letters \textit{Att.} 3.8--3.21 (29 May 58 BC -- 28 October
  58 BC), with the long key letter \textit{Att.} 3.15 (19
  August: the \textit{caeci, caeci inquam fuimus} reproach to
  Atticus); the move to Dyrrachium and the closing letters of
  58 BC \textit{Att.} 3.22--3.25; the two short
  letters of January 57 BC \textit{Att.} 3.26 and 3.27 (date
  corrections in works.yaml); the four family letters
  (\textit{Fam.} 14.2 of 5 October 58 BC carrying the news that
  Terentia was hauled from Vesta to the Tabula Valeria;
  \textit{Fam.} 14.1 of 25 November --- the \textit{vicus}
  she meant to sell; \textit{Fam.} 14.3 of 29 November ---
  the three lost options of self-defence: legateship, careful
  resistance, falling bravely); the two letters to Quintus
  \textit{Q. fr.} 1.3 (the famous \textit{mi frater, mi
  frater, mi frater} letter, 13 June 58) and 1.4 (around 5
  August); \textit{Fam.} 5.4 to Metellus Nepos in spring 57
  BC; \textit{Fam.} 13.41--43 (recommendation letters from
  Rome before exile, with date corrections so they sort with
  the other early-58 letters). The recovery year: \textit{Fam.}
  5.17 to Sittius, the three speeches that mark the return
  --- \textit{Post Reditum in Senatu} (5 September 57 BC, 39
  sections, the senatorial \textit{gratiarum actio} with the
  great paired invective on Gabinius and Piso),
  \textit{Post Reditum ad Quirites} (7 September, 25 sections,
  to the assembled people, with the \textit{devotio}
  declaration of \textsection 1 and the parallel-and-contrast
  with Marius's sword-borne return), and \textit{De Domo Sua}
  (29 September, 147 sections, before the College of Pontiffs:
  the speech that won back the Palatine site, built on three
  legal threads --- Clodius was no lawful tribune (the
  \textit{transitio} attack \textsection 34--42), the
  \textit{privilegium} argument (\textsection 43--57), the
  \textit{lex Papiria} argument that the bill carried no word
  of consecration (\textsection 127--128) --- with the famous
  satirical genealogy of ``Liberty'' as the marble image of a
  Tanagran courtesan from a tomb (\textsection 111--112) and
  the closing prayer to the Capitoline gods,
  Vesta, the household gods (\textsection 142--147)). The
  October correspondence \textit{Att.} 4.1 (mid-September,
  closing on ``We are beginning a kind of second life''),
  \textit{Att.} 4.2 (the report on the pontifical decision and
  the senatorial valuation), \textit{Att.} 4.3 (26 November,
  the November Clodian assault: the ambush on the Sacra Via,
  the storming of Milo's house, the Marcellinus motion);
  \textit{Q. fr.} 2.1 (mid-December, opening Q.fr. book 2 with
  the Senate proceedings on the Campanian land and on Clodius
  in court). Thirty-seven works drafted in this session.
  Resume point moves forward to \textit{Q. fr.} 2.4 and the
  long Lentulus Spinther correspondence opening
  \textit{Ad Familiares} book 1 in early 56 BC.
- **Fifth continuous session** *(complete)*: the early-56 BC
  political-letter sequence and \textit{Pro Sestio} drafted
  end-to-end. The Lentulus Spinther correspondence
  \textit{Fam.} 1.1--1.5b (Cicero's daily reports on the
  Senate's struggle over the Egyptian commission and Pompey's
  collapse on 8 February at the Milo contio); the brother
  letters \textit{Q. fr.} 2.2 (19 January, dictated through
  an eye inflammation), 2.3 (12--15 February --- the great
  companion-piece to Fam. 1.5b on the riot of 8 Feb, the SC
  at the temple of Apollo, the open break with Crassus), 2.4
  (mid-March, after the 11 March Sestius acquittal --- the
  Tyrannio note, the Tullia-Crassipes engagement, Milo's
  trick of buying up Cato's beast-fighter gang via Racilius);
  the brief \textit{Att.} 4.4 of 30 January and the
  recommendation \textit{Fam.} 1.3. Then \textit{Pro Sestio}
  (147 sections), the great political defence with the long
  \textit{narratio} of the year of exile (the joint portrait
  of Gabinius and Piso as the ``two whirlwinds of the
  commonwealth,'' the apology for not fighting against
  Marius's and Metellus Numidicus's exiles, the
  Pompey--Cato--Cyprus stretch), the parallel-with-Milo
  defence of guarding-by-private-force, and the
  \textit{cum dignitate otium} digression of \textsection
  96--143 (the optimate-as-disposition formula, the catalogue
  of the foundations of peace-with-standing, the
  contio-vs-populus distinction, the Aesopus-on-the-stage
  scene from Accius's \textit{Eurysaces} and \textit{Brutus},
  the gladiatorial show of Scipio Nasica with Sestius from
  the Maenian column, the closing roll-call of Roman
  forefathers in the \textit{coetus deorum immortalium}).
  Eleven works drafted. The session also did the metadata
  cleanup the resume note flagged: \textit{Fam.} 1.5 split
  into 1.5a and 1.5b per Perseus (the previous single entry
  had the wrong Latin Library URL and no speech\_index);
  \textit{Att.} 4.4A and 4.8A added (present in Perseus,
  missing from the manifest); placeholder dates corrected
  against the Perseus datelines for \textit{Q. fr.} 2.4,
  2.5, 2.6, \textit{Fam.} 1.6, and \textit{Att.} 4.5. Resume
  point moves forward to \textit{In Vatinium} (the
  cross-examination of Vatinius from the Sestius trial, which
  survives as a separate work) and onward through the
  post-Luca speeches and \textit{Q. fr.} book 2 of 56 BC.

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

- **Sixth continuous session** *(complete; assigned-list)*:
  the post-Sestio mid-56 BC senatorial-front sequence ---
  \textit{De Provinciis Consularibus} (June 56 BC, 47
  sections, the famous post-Luca about-face speech with the
  rage-portrait of Gabinius and Piso in the first third
  followed by the great pivot at \textsection 18 to defend
  Caesar's continuation in Gaul, with the catalogue of
  laying-aside-of-feud exempla --- T. Gracchus the elder
  for Scipio Africanus's brother, the Metelli for Marius
  in Gaul, M. Lepidus and M. Fulvius reconciled in the
  Campus on the day of their election to the censorship,
  Q. Metellus Nepos with Cicero himself --- and the
  closing legal trap on the Julian-laws-vs-lex-Clodia
  inconsistency at \textsection 45--46);
  \textit{Ad Familiares 5.12} (June 56 BC to L. Lucceius,
  the famous request for an historical monograph on the
  Catilinarian conspiracy and Cicero's exile-and-recovery,
  the \textit{epistula non erubescit} apology and the
  Hellenistic-historiographical exempla in section 7
  closing on the Naevian \textit{laudari a laudato viro});
  \textit{De Haruspicum Responsis} (late May / early
  summer 56 BC, 63 sections, the speech in reply to
  Clodius's contio reading the haruspical response on the
  rumble in the agro Latiniensi, with the head-by-head
  expansion of every clause as a prosecution-of-Clodius
  and the great catalogue of popularis turncoats from
  the Gracchi to Sulpicius and Clodius at \textsection
  41--44, closing on the famous symptoms-of-the-late-
  Republic catalogue at \textsection 60); and
  \textit{Pro Balbo} (summer 56 BC, 65 sections, the
  joint defence with Crassus and Pompey of L. Cornelius
  Balbus on his Pompeian citizenship grant from the
  Sertorian war, with the great catalogue of
  generals'-citizenship-grants from Marius through Sulla
  to Pompey himself --- the section-51 Ennian Hannibal-
  fragment \textit{hostem qui feriet, mihi Carthaginiensis
  erit, quisquis erit} --- and the most explicit surviving
  statement of the post-Luca self-reckoning at
  \textsection 61: \textit{voluimus quaedam, contendimus,
  experti sumus: obtenta non sunt}). Four works drafted.
  Also a metadata cleanup: the phantom
  \textit{Ad Quintum Fratrem 2.16} entry deleted from
  \texttt{meta/works.yaml} (a Tyrrell-Purser numbering
  artifact: TP split modern Q.fr. 2.3 into 2.3 + 2.4 and
  so counted 16 letters in book 2; modern Watt OCT,
  Shackleton Bailey, and Perseus carry only 15, with
  TP's 2.16 = modern 2.15 already drafted as
  \texttt{ad-quintum-fratrem-02-15}).

- **Seventh continuous session** *(complete; assigned-list)*:
  five letters of late 55 BC and the first half of 54 BC ---
  \textit{Att.} 4.13 (Tusculum, mid-November 55 BC, after 17
  K. Dec.: the brief return-from-the-bay letter on Milo's
  wedding, the elections, and Crassus's undignified Parthian
  departure compared with L. Aemilius Paulus's once for
  Macedon, with the De Oratore now in Cicero's hands and the
  Greek \textit{tēn parousan} request that Pilia be at home
  for the visit); \textit{Att.} 4.14 (Cumae, mid-May 54 BC,
  after 6 Id. Mai.: the request for the run of Atticus's
  library while the owner is away, ``especially Varro's,''
  for a work in hand --- almost certainly the De Re Publica);
  \textit{Q.fr.} 2.9 (Rome, early February 54: the
  Tenedian-axe pun on the senate's refusal of the Tenedian
  embassy's plea --- four optimate names voting with Cicero,
  Bibulus, Calidius, Favonius --- the praise of Quintus by
  the Magnesians from Sipylum, and the famous Cicero on
  Lucretius: ``many flashes of genius, yet much craft as
  well,'' with the closing tease on Cn. Sallustius's
  Empedoclea); \textit{Fam.} 7.7 (Rome, end of June 54 BC,
  to Trebatius in Caesar's camp on the eve of the second
  British expedition: the joke ``no gold or silver in
  Britain --- grab some war-chariot and run back,'' the more
  serious advice on becoming one of Caesar's intimates with
  Balbus's and Quintus's help); and \textit{Q.fr.} 2.13
  (Rome, 29 May 54: the great Caesar-letter day, with
  Cicero's pledge ``you are urging on a runner'' and the
  four-horse chariot of poetry --- ``only give me Britain,
  that I may paint it with your colours and my own brush''
  --- Caesar's witty thanks for Trebatius, the tribunate-for-
  M.-Curtius dance with the consuls Domitius and Appius, and
  the closing tragic-tag on wretched war's deeds).
  Sidecars emitted comprehensively (parallel, mentions,
  glossary, crossrefs, allusions where applicable). Seventeen
  new entities: persons (Vestorius, Varro, Aemilius Paulus,
  Bibulus, Calidius, Favonius, L. Sestius Pansa, Lucretius,
  Cn. Sallustius, Trebatius, L. Cornelius Balbus, M. Curtius,
  Domitius Ahenobarbus), places (Tenedos, Magnesia ad
  Sipylum, Britannia), and the lost text (Sallustius's
  Empedoclea). Four Greek phrases logged
  (\textit{skylmon}, \textit{oxypeinos}, \textit{tēn
  parousan}, \textit{toiauth' ho tlēmōn polemos
  exergazetai}). Seven translator's-notes entries logged for
  contested renderings (the Att. 4.13 \textit{ut sit rata}
  and \textit{tēn parousan}, the Lucretius textual crux,
  the \textit{vir/homo} pun, the British \textit{essedum},
  the \textit{currentem hortaris} idiom, the \textit{oricula
  infima} proverb).

- **Eighth-or-later parallel-assignment session** *(complete;
  assigned-list)*: seven of the eight Fam. 13 recommendation letters
  named in the launch prompt drafted end-to-end --- the four-letter
  Brutus-as-proconsul-of-Cisalpine-Gaul cluster (Fam. 13.11 commending
  three Roman-knight legates of Arpinum --- Q. Fufidius, M. Faucius,
  Q. Mamercius --- to oversee the municipal revenues Arpinum holds in
  Cisalpine Gaul, with the closing reference to Cicero's son and
  nephew and M. Caesius being the three Arpinate aediles in this same
  year; Fam. 13.12 the separate warmer commendation of Q. Fufidius;
  Fam. 13.13 for L. Castronius Paetus of Luca; Fam. 13.14 the
  remanded debt-recovery for L. Titius Strabo against P. Cornelius);
  the long Caesar-letter Fam. 13.16 commending Apollonius the Greek
  freedman of P. Crassus iunior, who served Cicero in Cilicia,
  Caesar in the Alexandrian war, and now sets out for Spain in 45 BC
  to write the history of Caesar's wars in Greek (the longest of the
  seven, with the Diodotus-the-Stoic backstory in section 4); and
  the two short Appuleius-as-proquaestor-of-Asia letters Fam. 13.45
  (L. Egnatius's slave Anchialus on Asian business) and 13.46
  (L. Nostius Zoilus, Cicero's coheir and freedman of his patron).
  Sidecars emitted comprehensively (parallel, mentions, glossary,
  letter-network, two translator's notes for the Fam. 13.16 textual
  crux \texttt{eximus} -> \texttt{eximiis} and the
  \textit{litterae Graecae} idiom). Eighteen new entities added to
  \texttt{entities.json}: the Arpinate cluster
  (Q. Fufidius, M. Faucius, Q. Mamercius, M. Caesius, place:arpinum)
  plus Cicero's son and nephew (Marcus and Quintus the Younger), the
  Brutus-letter cast (L. Castronius Paetus, place:luca, L. Titius
  Strabo, P. Cornelius the debtor, C. Volcacius Tullus the urban
  praetor), the Caesar letter cast (P. Crassus iunior, Apollonius
  the freedman, Diodotus the Stoic, event:alexandrian-war), and the
  Appuleius cluster (M. Appuleius, L. Egnatius Rufus, Anchialus,
  L. Nostius Zoilus). Metadata fix: the eight assigned letters had
  their \texttt{latin\_source\_url} pointing at the 403'd Latin
  Library; updated to Perseus phi0474.phi056 and \texttt{speech\_index}
  added per entry. \textbf{The eighth assigned letter ---
  ad-familiares-13-49 --- is absent from Perseus's edition (book 13
  jumps from letter 48 directly to 50) and could not be fetched;
  remains pending and will need manual sourcing from another Latin
  repository in a later pass.}

## Where to resume now

**Project management is now Claude Cowork** (running on Alexander's
desktop, on his Max subscription quota). When Cowork opens this
repo, this is the first section to read; \texttt{PLAN.md} is the
binding multi-surface roadmap.

\textbf{Translation state (post-Cowork-session-33):} \textbf{904 /
958 works drafted (\~94.4\%)}. \textbf{Latest drafted by deep
chronology is unchanged}: \textit{Ad Familiares} 10.24 (Plancus's
camp in Gaul, 28 July 43 BC) remains the marker, because the one
speech drafted this session (\textit{Pro Ligario}) is dated
November 46 BC, far earlier than the marker. Session 33 \textbf{
continued the single-substantial-speech-per-session mode} that
session 32 pivoted to: one worker, end-to-end translation of the
second of the three Caesarian speeches, with 5-section-per-Edit
chunk discipline and parallel-sidecar emission in the same session.
The chronological-gap warning falls from \textbf{49} (post-session-
32) to \textbf{48} (post-session-33), exactly the expected decrement
of one speech moved out of the gap.

\textbf{Cowork session 33 --- 1 substantial speech drafted (1
worker, 38 sections, 5-section chunks):}

\begin{itemize}
\item \textbf{Worker A (\textit{Pro Ligario} --- the famous
forensic speech before Caesar pleading for the pardon of Q.
Ligarius, late November 46 BC, delivered in the Forum with
Caesar sitting as judge):} 38 sections, $\sim$6{,}300 English
words. The second of the three Caesarian speeches. Q. Ligarius
had been Pompeian legate in Africa under C. Considius, was
left in charge of the province on Considius's departure, joined
P. Attius Varus when Varus seized command at Utica, and was
on the losing side at Thapsus; Q. Tubero (whose own father had
also been on the Pompeian side) now turned prosecutor before
Caesar. Contains: the \S 1 \textit{novum crimen} opening
(``a novel charge, Gaius Caesar, and one not heard before this
day''); the \S 6 \textit{O clementiam admirabilem!} apostrophe;
the \S 9 four-question forensic attack on Tubero himself
(\textit{quid enim, Tubero, tuus ille destrictus in acie
Pharsalica gladius agebat? cuius latus ille mucro petebat? qui
sensus erat armorum tuorum? quae tua mens, oculi, manus, ardor
animi?}) --- the most pointed second-person assault in any of
the Caesarian speeches; the \S 15 \textit{per te, per te,
inquam, obtines} anaphora; the \S 19 deification climax
\textbf{\textit{nihil habet nec fortuna tua maius quam ut
possis, nec natura tua melius quam ut velis servare quam
plurimos}} echoed and crowned at \S 38 by the famous
\textbf{\textit{homines enim ad deos nulla re propius accedunt
quam salutem hominibus dando}} (``For men come closer to the
gods by nothing than by giving safety to men'') --- rendered
freshly from the Latin without echoing Yonge / Watts / Loeb /
Berry, per STYLE.md; the \S 30 forensic-vs-filial register break
(\textit{ad iudicem} vs.~\textit{ad parentem}); the \S 33
\textit{valeat tua vox illa quae vicit} reminder of Caesar's
own reported neutrality-policy saying; and the \S 38 closing
pledge \textit{si absenti salutem dederis, praesentibus te his
daturum} (``if you grant his safety to one who is absent, you
will grant yourself to all these who are present''). No Greek
phrases in this speech (pure Latin oratory throughout; the
\S 11 \textit{externi \ldots mores aut levium Graecorum aut
immanium barbarorum} is a Latin gibe, not a Greek phrase).
\textbf{No date correction:} \texttt{-0046-11-01} month-precision
stands; the Perseus Latin file has no narrower dateline, and
standard scholarly placement is late November 46 BC, after the
\textit{Pro Marcello} of mid-to-late September.
\end{itemize}

\textbf{No metadata corrections committed during session 33.}
The single status flip (pro-ligario: pending $\rightarrow$
drafted) was clean; the meta entry's date and Latin source URL
match the fetch.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{\S 1 \textit{abuterer}.} Rendered ``take advantage
of'' --- preserves the slightly admissive ironic edge (``I had
come prepared to \textit{misuse} your ignorance''). Alternative:
``exploit.''
\item \textbf{\S 6 \textit{prodo meam}.} Rendered ``I am giving
away my own [case]''; the \textit{prodo} carries betrayal-
undertones that were deliberately softened to ``giving away''
rather than ``betraying,'' since the rhetorical posture is
generous self-confession, not treason.
\item \textbf{\S 11 \textit{prodigi simile}.} ``Something close
to a monstrosity'': \textit{prodigium} is an evil portent,
almost an outrage of nature; ``monstrosity'' carries the
unnatural weight better than ``marvel.''
\item \textbf{\S 11 \textit{levium Graecorum}.} ``Frivolous
Greeks'': \textit{levium} sometimes drifts toward ``fickle'';
``frivolous'' was chosen to keep the parallelism with ``savage
barbarians.''
\item \textbf{\S 15 \textit{per te, per te, inquam, obtines}.}
Anaphora preserved as ``by your own self, by your own self, I
say''; an alternative is ``of yourself, of yourself,'' but ``by
your own self'' lands the agency more cleanly.
\item \textbf{\S 17 \textit{fatalis quaedam calamitas \ldots
humana consilia divina necessitate esse superata}.} ``Fated
disaster \ldots human counsels overborne by divine necessity'';
the \textit{fatalis} / \textit{divina necessitate} pair is
theological-Stoic and was not flattened to ``fate / fate.''
\item \textbf{\S 29 \textit{ad unam summam referri volo vel
humanitatis vel clementiae vel misericordiae}.} ``To one single
sum: of humanity, of clemency, of pity''; the \textit{summam}
metaphor is a ledger-image preserved as ``sum'' rather than
``head'' or ``total.''
\item \textbf{\S 30 \textit{ad parentem \ldots ad iudicem}.}
Central rhetorical turn rendered with explicit ``So one speaks
before a judge: but I am speaking before a parent.''
\item \textbf{\S 33 \textit{valeat tua vox illa quae vicit}.}
``Let that voice of yours which won the day prevail''; \textit{
vox quae vicit} is shorthand for Caesar's reported neutrality-
policy saying, quoted in the next sentence --- the cataphora is
left as Cicero has it.
\item \textbf{\S 38 \textit{homines enim ad deos \ldots dando}.}
``For men come closer to the gods by nothing than by giving
safety to men.'' Translated freshly from the Latin without
consulting Yonge / Watts / Loeb / Berry; preserved the syntax
shape \textit{nulla re propius \ldots quam \ldots dando} as
``by nothing \ldots than by \ldots giving.''
\item \textbf{\S 38 closing \textit{praesentibus te his
daturum}.} Read as ``you will grant yourself to all these who
are present'' (the \textit{te} as direct object, future
infinitive \textit{daturum [esse]}); a less common reading
takes the object as still \textit{salutem}, but the
construction with explicit \textit{te} favours the reflexive
--- Caesar's pardon for the absent man is also a pledge of
Caesar's presence and favour to those present in the Forum.
\end{itemize}

\textbf{Suggested next translation batch} (when session 33 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 33:
\ldots"} and the next Cowork session opens):

\textbf{Session 34 should pick up \texttt{pro-rege-deiotaro}}
(November 45 BC, $\sim$43 sections), the third and final of the
three ``Caesarian'' speeches --- Cicero pleading before Caesar
himself, this time in Caesar's own house, on behalf of king
Deiotarus of Galatia, charged by his own grandson Castor with
having plotted against Caesar's life during Caesar's stay at the
royal estate after Zela. Same single-substantial-speech-per-
session pattern as sessions 32--33; one worker, 5-section chunks
of the English file, WIP discipline, parallel-sidecar emission
in two-three JSON chunks. The Latin will fetch cleanly from
Perseus (\texttt{phi0474.phi034}).

\textbf{After \texttt{pro-rege-deiotaro}}: sessions 35--47 sweep
the \textit{Philippics} (\texttt{philippic-1} through
\texttt{philippic-14}, with \textit{Philippic} 2 at $\sim$119
sections planned as a 2-session work). Sessions 48--58 sweep
the major philosophical treatises (\textit{Paradoxa Stoicorum},
\textit{Academica}, \textit{De Finibus}, \textit{Timaeus},
\textit{De Natura Deorum}, \textit{Tusculanae Disputationes},
\textit{Cato Maior De Senectute}, \textit{De Divinatione},
\textit{De Fato}, \textit{Laelius De Amicitia},
\textit{De Officiis}). The remaining minor speeches and the
rhetorica (\textit{partitiones-oratoriae}, \textit{brutus},
\textit{de-optimo-genere-oratorum}, \textit{orator},
\textit{topica}) are slotted alongside as one-session pickups.

\textbf{Slice F (the 12 no-Perseus deferred letters)} continues
to require a single-session manual-fetch batch and is held
until someone supplies the Latin from a standard printed
edition.

\textbf{Slice M (entity-stub enrichment, 429+ stubs in
\texttt{data/entities.json})} remains the parallel-friendly
fallback when no substantial work is ready to be picked up.

\textbf{File-rename carry-overs from earlier sessions (sandbox
cannot delete files; Alexander handles at handoff or follow-up):}
\textit{Att.} 5.1, 5.7 (\texttt{049bc-} $\rightarrow$
\texttt{051bc-}) and \textit{Fam.} 13.09 (\texttt{005bc-}
$\rightarrow$ \texttt{050bc-}).

\textbf{Launch-prompt advisory for the scheduled 2-hour Cowork
task on Alexander's side:} the prompt text (\texttt{dispatch
3--4 parallel batches of worker sub-agents, each translating
3--5 short letters end-to-end}) remains stale. Sessions 32 and
33 both auto-pivoted to single-substantial-speech mode per this
section's instructions; the same auto-pivot will apply to
session 34 and onward through the Caesarian / Philippic /
philosophical phases. Updating the scheduled-task prompt to
reflect Phase 3 of OPERATING\_PLAN.md (``one substantial-speech
worker per session, 5-section chunks, WIP-commit discipline'')
is recommended but not blocking --- the PM in each scheduled
session reads ``Where to resume now'' first and follows what
it says.


\textbf{Translation state (post-Cowork-session-32):} \textbf{903 /
958 works drafted (\~94.3\%)}. \textbf{Latest drafted by deep
chronology is unchanged}: \textit{Ad Familiares} 10.24 (Plancus's
camp in Gaul, 28 July 43 BC) remains the marker, because the one
speech drafted this session (\textit{Pro Marcello}) is dated
September 46 BC, far earlier than the marker. Session 32 \textbf{
executed the mode pivot foreshadowed by session 31}: from short-
letter parallel mode (3--5 letters per worker, 3--4 parallel
batches per session) to \textbf{single-substantial-speech-per-
session mode} (one worker, 5-section-per-Edit chunk discipline,
WIP-payload sizing). The chronological-gap warning falls from
\textbf{50} (post-session-31) to \textbf{49} (post-session-32),
exactly the expected decrement of one speech moved out of the gap.

\textbf{Cowork session 32 --- 1 substantial speech drafted (1
worker, 34 sections, 5-section chunks):}

\begin{itemize}
\item \textbf{Worker A (\textit{Pro Marcello} --- the famous
``Caesarian'' senatorial speech of thanks to Caesar for the
pardon of M. Claudius Marcellus, mid-to-late September 46 BC,
delivered in the Senate at Rome):} 34 sections, $\sim$5{,}200
English words. The first of the three Caesarian speeches.
Cicero's broken silence after Pharsalus, on the day Caesar
yielded to a Senate motion led by L. Calpurnius Piso and
Marcellus's cousin C. Marcellus and restored the most stubborn
of the Pompeian consulars to public life. Contains: the §1
fourfold anaphora \textit{tantam \ldots tam \ldots tantum
\ldots tam} (gentleness, clemency, moderation, wisdom) opening
the encomium; the §6--9 architecture of moral-over-military
victory closing with the §8 climax \textit{animum vincere,
iracundiam cohibere, victo temperare \ldots simillimum deo
iudico} (``to conquer one's own spirit, to restrain anger, to
spare the conquered \ldots I judge him most like a god''); the
§12 antithesis \textbf{\textit{ipsam victoriam vicisse videris}}
(``you seem to have conquered victory itself'') --- the speech's
most-famous line, rendered freshly from the Latin without
echoing the canonical English versions; the §23 immortality-
through-deeds turn; the §25--32 pivot to the still-unsettled
\textit{res publica} and Cicero's appeal that Caesar must guard
his own life because the state's life now depends on it
(\textit{tua, Caesar, salus}); the §27 \textit{iste tuus
animus}/\textit{immortalitatis amor} passage (\textbf{NOT}
\textit{mens et ratio et consilium}, which the launch prompt
misattributed --- worth flagging as a translator-notes entry);
the §32 bodyguard-language \textit{laterum nostrorum oppositus
et corporum pollicemur} (``the interposing of our own flanks
and our own bodies''); and the §33--34 closing \textit{gratiarum
actio} with the §1 ring composition (\textit{sed ut unde est
orsa}). No Greek phrases in this speech. \textbf{No date
correction:} \texttt{-0046-09-01} month-precision stands; the
Perseus Latin file has no narrower dateline, and standard
scholarly placement is mid-to-late September 46 BC after
Caesar's Spanish triumph.
\end{itemize}

\textbf{No metadata corrections committed during session 32.}
The single status flip (pro-marcello: pending $\rightarrow$
drafted) was clean; the meta entry's date and section count
match the Latin.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{§1 fourfold anaphora.} \textit{tantam mansuetudinem,
tam inusitatam inauditamque clementiam, tantum \ldots modum,
tam denique incredibilem sapientiam} --- the architecture of
the encomium of Caesar's qualities. English preserves the
repeated \textit{tantam}/\textit{tam} as ``so great''/``so'';
the alternation between the two correlatives is intentional and
preserved.
\item \textbf{§8 the simillimum deo iudico climax.} The pivot
from military to moral excellence is the structural hinge of
the speech. ``I judge him most like a god'' --- not ``equal to
a god,'' which would be \textit{parem} and would overstate.
\item \textbf{§10 \textit{me dius fidius}.} Rendered ``by all
that's holy'' --- a measured oratorical asseverative for the
Senate floor, not the colloquial register the phrase carries in
letters.
\item \textbf{§11 syntactic carry-over into §12.} The em-dash
that closes §11 in Perseus's text hangs syntactically into §12;
preserved by keeping the dash at §11's close and resuming §12
with a lowercase ``but,'' which preserves the section boundary
while honouring the unbroken sentence.
\item \textbf{§12 \textit{ipsam victoriam vicisse videris}.} The
most-quoted line of the speech. Rendered ``you seem to have
conquered victory itself, when you have given back to the
conquered the things which had been taken from them'' --- word
order preserves the chiastic punch; phrasing is fresh and does
not echo the canonical English versions (Yonge, Cary, Watts,
Berry, Loeb), per STYLE.md.
\item \textbf{§27 Perseus reading vs. memory-citation.} The
launch prompt named \textit{mens et ratio et consilium} as a
§27 phrase. Perseus's §27 reads \textit{iste tuus animus
\ldots immortalitatis amor flagravit}, not the mens-ratio-
consilium triad. The translation honours what is on the page;
future apparatus may wish a note recording that the famous
triad belongs (in some critical traditions or paraphrases) to a
nearby section, not §27 as printed in Perseus.
\item \textbf{§29 \textit{Servi igitur} read as imperative of
\textit{servio}.} Perseus prints \textit{Servi} with capital S;
treated as ``be a servant to those judges,'' not \textit{serva}
``save them.'' Worth a one-line note in apparatus.
\item \textbf{§32 \textit{laterum oppositus et corporum}.}
Bodyguard-language preserved literally as ``the interposing of
our own flanks and our own bodies'' rather than smoothed to
``we pledge ourselves as shields'' --- the \textit{latera}/
\textit{corpora} pairing is Roman-bodyguard idiom and worth
keeping.
\end{itemize}

\textbf{Suggested next translation batch} (when session 32 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 32:
\ldots"} and the next Cowork session opens):

\textbf{Session 33 should pick up \texttt{pro-ligario}}
(November 46 BC, $\sim$38 sections), the second of the three
``Caesarian'' speeches --- Cicero pleading before Caesar for Q.
Ligarius's recall from exile. Same single-substantial-speech-
per-session pattern as session 32; one worker, 5-section chunks
of the English file, WIP discipline, parallel-sidecar emission
in two-three JSON chunks. The Latin will fetch cleanly from
Perseus (\texttt{phi0474.phi033}).

\textbf{After \texttt{pro-ligario}}: session 34 should pick up
\texttt{pro-rege-deiotaro} (November 45 BC, $\sim$43 sections),
closing out the three Caesarian speeches. Sessions 35--47 then
sweep the \textit{Philippics} (\texttt{philippic-1} through
\texttt{philippic-14}, with \textit{Philippic} 2 at $\sim$119
sections planned as a 2-session work). Sessions 48--58 sweep
the major philosophical treatises (\textit{Paradoxa
Stoicorum}, \textit{Academica}, \textit{De Finibus},
\textit{Timaeus}, \textit{De Natura Deorum}, \textit{Tusculanae
Disputationes}, \textit{Cato Maior De Senectute}, \textit{De
Divinatione}, \textit{De Fato}, \textit{Laelius De Amicitia},
\textit{De Officiis}). The remaining minor speeches and the
rhetorica (\textit{partitiones-oratoriae}, \textit{brutus},
\textit{de-optimo-genere-oratorum}, \textit{orator},
\textit{topica}) are slotted alongside as one-session pickups.

\textbf{Slice F (the 12 no-Perseus deferred letters)} continues
to require a single-session manual-fetch batch and is held
until someone supplies the Latin from a standard printed
edition.

\textbf{Slice M (entity-stub enrichment, 429+ stubs in
\texttt{data/entities.json})} remains the parallel-friendly
fallback when no substantial work is ready to be picked up.

\textbf{File-rename carry-overs from earlier sessions (sandbox
cannot delete files; Alexander handles at handoff or follow-up):}
\textit{Att.} 5.1, 5.7 (\texttt{049bc-} $\rightarrow$
\texttt{051bc-}) and \textit{Fam.} 13.09 (\texttt{005bc-}
$\rightarrow$ \texttt{050bc-}).

\textbf{Launch-prompt advisory for the scheduled 2-hour Cowork
task on Alexander's side:} the prompt text (\texttt{dispatch
3--4 parallel batches of worker sub-agents, each translating
3--5 short letters end-to-end}) is now stale. Session 32
auto-pivoted to single-substantial-speech mode per this
section's instructions; the same auto-pivot will apply to
session 33 and onward. Updating the scheduled-task prompt to
reflect Phase 3 of OPERATING\_PLAN.md (``one substantial-speech
worker per session, 5-section chunks, WIP-commit discipline'')
is recommended but not blocking.


\textbf{Translation state (post-Cowork-session-31):} \textbf{902 /
958 works drafted (\~94.2\%)}. \textbf{Latest drafted by deep
chronology is unchanged}: \textit{Ad Familiares} 10.24 (Plancus's
camp in Gaul, 28 July 43 BC) remains the marker, because the one
letter drafted this session (\textit{Ad Brutum} 1.15) is dated
14 July 43 BC, earlier than the marker. Session 31 \textbf{closed
out the last fetchable letter in the chronological gap}, drafting
the substantial 13-section Cicero-to-Brutus letter on rewards and
punishments (the Solon two-pillars citation), Cicero's defence of
his honors-to-Octavian policy, the Lepidus-statue passage, and the
closing plea (\textit{sed propera, per deos!}). The chronological-
gap warning count is unchanged at \textbf{50} because
\textit{Ad Brutum} 1.15 was previously dated \texttt{-0043-08-04}
(year-precision, placing it \textit{after} the marker, so it never
appeared in the earlier-than-marker set) and is now correctly
dated \texttt{-0043-07-14} day-precision \textit{and} drafted (so
it still does not appear in the set). The 50 remaining gap entries
are all speeches, philosophy, rhetoric, or no-Perseus-deferred
letters.

\textbf{IMPORTANT MODE PIVOT: short-letter parallel mode is now
exhausted.} Of the 49 remaining gap entries, \textbf{zero are
short, Perseus-fetchable letters in the standard worker-friendly
shape}. The breakdown is:

\begin{itemize}
\item \textbf{12 no-Perseus deferred letters (Slice F)}, all with
\texttt{thelatinlibrary.com} URLs that 403 or dump whole-book
files: \textit{Fam.} 5.10 (51 BC), \textit{Fam.} 9.25 (46 BC),
\textit{Att.} 13.15/13.18/13.36 (45 BC), \textit{Ad Brutum}
01-16/02-06/02-07/02-08 (43 BC), \textit{Fam.} 11.08/11.17/11.28
(43 BC). All have placeholder stubs already in
\texttt{latin/letters/} from sessions 17--18; need manual sourcing
from Shackleton Bailey / Teubner / OCT.
\item \textbf{14 substantial speeches (Slice C)}: \texttt{pro-
plancio}, \texttt{pro-rabirio-postumo}, \texttt{pro-scauro},
\texttt{pro-milone} (52 BC), \texttt{pro-marcello}, \texttt{pro-
ligario}, \texttt{pro-rege-deiotaro}, and the eight surviving
\textit{Philippics} not yet drafted: \texttt{philippic-1, -2, -3,
-4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14}. One substantial
speech per session, with the 5-section-per-Edit chunk discipline
of CLAUDE.md \S Timeout discipline.
\item \textbf{11 philosophy treatises} of 46--44 BC:
\texttt{paradoxa-stoicorum}, \texttt{academica}, \texttt{de-
finibus}, \texttt{timaeus}, \texttt{de-natura-deorum},
\texttt{tusculanae-disputationes}, \texttt{cato-maior-de-
senectute}, \texttt{de-divinatione}, \texttt{de-fato},
\texttt{laelius-de-amicitia}, \texttt{de-officiis}. Each is a major
multi-session work; \texttt{de-officiis} alone is three books and
will likely take 2--3 sessions on its own.
\item \textbf{4 rhetoric works}: \texttt{partitiones-oratoriae},
\texttt{brutus}, \texttt{de-optimo-genere-oratorum},
\texttt{orator}, \texttt{topica} (\texttt{topica} is 44 BC, the
others 46--45 BC). \texttt{brutus} is the substantial dialogue on
the history of Roman oratory; the others are shorter.
\item \textbf{1 no-Perseus complete work}: \texttt{de-legibus}
(52 BC), three books surviving in full but absent from Perseus's
TEI corpus; needs manual Latin sourcing (see CLAUDE.md
\S Metadata gotchas).
\item Plus \textbf{7 more entries} outside the gap (later than the
28 July marker): primarily later \textit{Phil.} and \textit{Fam.}
items not aggregated here.
\end{itemize}

\textbf{Recommendation for Cowork session 32 and following:} pivot
from parallel-letter mode to single-substantial-work-per-session
mode (Phase 3 of OPERATING\_PLAN.md). The natural chronological
sequence to address is, in order:

\begin{enumerate}
\item \texttt{pro-marcello} (Sept 46 BC, $\sim$34 sections, one
session) --- the famous Caesarian-clemency speech, short enough
that one worker with 5-section chunk discipline can finish it.
\item \texttt{pro-ligario} (Nov 46 BC, $\sim$38 sections, one
session).
\item \texttt{pro-rege-deiotaro} (Nov 45 BC, $\sim$43 sections,
one session) --- closes out the three Caesarian speeches.
\item \texttt{philippic-1} (Sept 44 BC, $\sim$38 sections, one
session) --- opens the \textit{Philippics} sequence.
\item Continue Philippics 2--14 in order, one per session
(\textit{Philippic} 2 is the longest at $\sim$119 sections and
should be planned as a 2-session work; the others mostly
20--40 sections each).
\end{enumerate}

The launch prompt for the next session should switch from ``3--4
parallel batches of worker sub-agents, each translating 3--5 short
letters'' to ``one substantial-speech worker, 5-section chunks,
WIP-commit discipline'' or equivalent. The standard 2-hour
scheduled-task prompt may need an update on Alexander's side.

\textbf{Slice F (12 no-Perseus deferred letters) remains a single-
session manual-fetch batch}, held until someone supplies the Latin
from a printed edition. This is not urgent --- the bound volume can
be assembled around their absence with marginal notes pointing to
the corresponding Shackleton Bailey passages --- but it is the
only path to fully closing the chronological gap below 49.

\textbf{Cowork session 31 --- 1 letter drafted (1 worker, 1
substantial letter):}

\begin{itemize}
\item \textbf{Worker A (\textit{Ad Brutum} 1.15 --- the long
political-philosophical letter to Brutus, mid-early July 43 BC,
Rome):} 13 sections, $\sim$1{,}840 English words. The substantial
letter pairing with the 1.14 reproach and looking forward to the
1.17 Brutus-to-Atticus broadside. Contains: the Messala
encomium of \S 1--2; the Solon two-pillars-of-the-republic
citation (with the daggered crux \textit{$\dagger$neque solum ut
Solonis dictum usurpem$\dagger$} preserved) and the
\textit{praemio et poena} architecture of \S 3; the
\textit{instrumentum regni delatum ad Lepidum et Antonium}
``instrument of monarchy'' phrase of \S 4; Cicero's defence of
his decree of honours to Octavian (\S 7--9) and the Lepidus-
statue passage (``\textit{nos illum honore studuimus a furore
revocare. vicit amentia levissimi hominis nostram prudentiam}''
--- ``we honoured him to recall him from madness; the madness
of a most worthless man overcame our prudence''); and the
closing plea \textbf{\textit{sed propera, per deos!}} (``but
hurry, by the gods!''), sharper than the parallel plea in 1.14.
No Greek phrases in this letter. \textbf{DATE CORRECTION
committed:} \texttt{-0043-08-04} year-precision $\rightarrow$
\texttt{-0043-07-14} day-precision (Shackleton Bailey assigns
ca.~14 July; Perseus dateline ``\textit{circ. med. in. Quint.}''
= approximately the middle of early Quintilis, i.e.~5--14 July;
the meta date of 4 August cannot stand against Perseus's
explicit ``\textit{Quint.}'' = Quintilis = July).
\end{itemize}

\textbf{Metadata corrections committed to \texttt{meta/works.yaml}
during session 31 (1 date correction):}
\begin{itemize}
\item \textit{Ad Brutum} 1.15: \texttt{date} \mbox{-0043-08-04}
year-precision $\rightarrow$ \mbox{-0043-07-14} day-precision
(per Perseus \textit{Scr. Romae circ. med. in. Quint. a. 711
(43)} and Shackleton Bailey's editorial dating).
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Ad Brutum} 1.15 \S 3 Solon-citation
crux} \textit{$\dagger$neque solum ut Solonis dictum usurpem$
\dagger$}. The Greek scholarly tradition does ascribe to Solon
the two-pillars-of-the-republic maxim, but the Latin transmission
of the line in this letter is plainly corrupt around the
particle structure. Daggers preserved; English rendered inside
them as a literal best-effort.
\item \textbf{The \S 4 \textit{instrumentum regni}} phrase. ``The
instrument of monarchy was handed over to Lepidus and Antony''
--- preserves the political weight of \textit{regnum} as the
Roman terror-word for autocratic kingship; ``tyranny'' would be
weaker and Greek-flavoured, ``kingship'' weaker still.
\item \textbf{The \S 6 \textit{consilia imre coepi Brutina}}
orthographic corruption. \textit{imre} is plainly a slip for
\textit{inire}; the translation reads ``I began to lay plans
plainly in the Brutus style.'' Silent emendation rather than a
substantive crux, but worth flagging once for the apparatus.
\item \textbf{The \S 9 Lepidus-statue concession.} The rhetorical
pivot around which Cicero's defence of his honours policy turns
--- the only honour he openly acknowledges as a misjudgment.
``We honoured him to recall him from madness; the madness of a
most worthless man overcame our prudence; nor was so much harm
done in setting up Lepidus's statue as good was done in tearing
it down.''
\item \textbf{The \S 12 closing plea \textit{sed propera, per
deos!}} Sharper than 1.14's closing because it follows 1.14's
unanswered earlier plea by only three days (1.14 dated 11 July,
1.15 dated $\sim$14 July). The escalation in tone is the
emotional fact of the letter.
\end{itemize}

\textbf{Suggested next translation batch} (when session 31 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 31:
\ldots"} and the next Cowork session opens):

\textbf{Recommended pivot for session 32}: \textbf{\texttt{pro-
marcello}} as a single-worker substantial-speech session.
$\sim$34 sections, Perseus-fetchable, the famous Caesar-clemency
speech delivered before the Senate when Caesar pardoned M.
Marcellus. One worker, 5-section chunks, WIP discipline. After
\texttt{pro-marcello} lands, session 33 should pick up
\texttt{pro-ligario}; sessions 34--47 sweep the
\textit{Philippics}; sessions 48--58 sweep the major philosophical
treatises; the remaining minor speeches and rhetorica are slotted
in alongside.

\textbf{Slice F (the 12 no-Perseus deferred letters)} continues to
require a single-session manual-fetch batch and is held until
someone supplies the Latin from a standard printed edition.

\textbf{Slice M (entity-stub enrichment, 429+ stubs in
\texttt{data/entities.json})} remains the parallel-friendly
fallback when no substantial work is ready to be picked up.

\textbf{File-rename carry-overs from earlier sessions (sandbox
cannot delete files; Alexander handles at handoff or follow-up):}
\textit{Att.} 5.1, 5.7 (\texttt{049bc-} $\rightarrow$
\texttt{051bc-}) and \textit{Fam.} 13.09 (\texttt{005bc-}
$\rightarrow$ \texttt{050bc-}).


\textbf{Translation state (post-Cowork-session-30):} \textbf{901 /
958 works drafted (\~94.0\%)}. \textbf{Latest drafted by deep
chronology is unchanged} from sessions 27--29: \textit{Ad
Familiares} 10.24 (Plancus's camp in Gaul, 28 July 43 BC) remains
the marker, because all 21 letters drafted this session are dated
earlier than that. Session 30 \textbf{continued the chronological-
gap sweep (Slice S')}, drafting 21 \textit{Ad Familiares} and
\textit{Ad Atticum} letters across two waves (five workers total),
spanning May 51 BC (Cicero's Cilician journey) through December 45
BC (post-Tullia mourning). The chronological-gap warning falls
from \textbf{71} pending-earlier-than-marker (post-session-29) to
\textbf{50} (post-session-30) --- a 21-letter reduction inside the
gap.

\textbf{Cowork session 30 --- 21 letters drafted across two waves
(five workers total):}

\textbf{Wave 1 (4 workers, 17 letters):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 5.1, 5.7; \textit{Fam.} 5.20,
4.1, 5.19 --- 5 letters of the Cilician departure + civil-war
outbreak, May 51 -- April 49 BC):} \textbf{\textit{Att.} 5.1
(Cicero, Minturnae, c. 6 May 51 BC, to Atticus --- the famous
domestic-spat-with-Pomponia letter on the journey to Cilicia)
and 5.7 (Tarentum, 22 May 51 BC) --- \textbf{MAJOR DATE
CORRECTIONS}: both meta entries had \texttt{-0049-} (Perseus's
parenthetical ``(49)'' is corrupted; AUC 703 = 51 BC); corrected
to \texttt{-0051-05-06} and \texttt{-0051-05-22} day-precision;
files retain \texttt{049bc-} prefix pending Alexander's rename
at handoff}; \textit{Fam.} 5.20 (Cicero, ad urbem, c. 6 January
49 BC, to L. Mescinius Rufus --- the substantial accounts letter
with the obelized §4 \textit{†cum rem a me non insipienter
excogitatam quidem putas†} and contested \texttt{HS xxx/xix/xxii/c}
sums); \textit{Fam.} 4.1 (Lateris/Arcanum, c. 5 April 49 BC, to
Servius Sulpicius --- the \textit{quam honestissime lugeamus} ``to
mourn the most honourably we can'' letter, declining to attend
Caesar's \textit{conventus senatorum}); \textit{Fam.} 5.19 (Cumae,
c. 28 April 49 BC --- recipient confirmed as L. Mescinius Rufus
per \texttt{CICERO RVFO} salutation, not M'. Curius as suggested,
with the famous antithesis \textit{quid rectum sit apparet, quid
expediat obscurum est}).
\item \textbf{Worker B (\textit{Fam.} 4.2, 2.16, 16.18, 15.15 ---
4 letters, April-August 49--47 BC):} \textit{Fam.} 4.2 (Cumae,
28 April 49 BC, to Servius Sulpicius --- the second exchange in
the Sulpicius cluster); \textit{Fam.} 2.16 (Cumae, 4 May 49 BC,
to M. Caelius Rufus --- the substantial reply to Caelius's
Caesar-side overtures, with the \textit{dibaphum} ``twice-dyed
garment'' joke about Curtius, the \textit{toga praetexta} gift,
and the §6 aposiopesis \textit{sed tamen---}); \textit{Fam.}
16.18 (Cicero, Rome, c. May 47 BC, to Tiro --- the famous
\textbf{SIX-GREEK-PHRASES medical-vocabulary letter}:
\textit{diaphoresin}, \textit{pepsin}, \textit{akopian},
\textit{peripaton symmetron}, \textit{tripsin}, \textit{eulysian
koilias}, ordering Tiro a regimen of measured walking, rubdowns,
and digestive care; with the obscure colloquialism \textit{Calface
hominem ut ego Mothonem; itaque abutor coronis}, and the Aqua
Crabra reference); \textit{Fam.} 15.15 (Brundisium, mid-August
47 BC, to C. Cassius --- the substantial Stoic-philosophical
letter on the African resistance, with \textit{currentem ut aiunt
incitarem} ``to urge him on toward peace, as the saying is, while
he was already running'' as the rhetorical hinge).
\item \textbf{Worker C (\textit{Fam.} 15.21, 5.21, 4.13, 4.14 ---
4 letters with \textbf{three meta corrections}):} \textit{Fam.}
15.21 (Cicero, Rome, late 47 BC, to C. Trebonius --- with the
grammatically broken §3 \textit{cui quidem ego amori utinam ceteris
rebus possem amore certe respondebo}); \textbf{\textit{Fam.} 5.21
(Cicero, Rome, early-to-mid April 46 BC, to L. Mescinius Rufus
--- \textbf{DATE CORRECTION}: \texttt{-0046-06-18} year-precision
$\rightarrow$ \texttt{-0046-04-01} month-precision, per Perseus
\textit{in. aut med. m. April. a. 708 (46)}; with the
\textit{medius fidius} and the elliptical \textit{is, quem tu
numquam amasti (me enim amabas)})}; \textbf{\textit{Fam.} 4.13
(Cicero, Rome, early August 46 BC --- \textbf{TWO CORRECTIONS}:
\textbf{DATE} \texttt{-0046-06-22} $\rightarrow$
\texttt{-0046-08-01} month-precision per Perseus \textit{ui. in.
Sext. a. 708 (46)}; \textbf{RECIPIENT CORRECTION}: salutation
\texttt{M. CICERO S. D. P. FIGVLO.} confirms recipient is
\textbf{P. Nigidius Figulus}, not Servius Sulpicius as the launch
prompt suggested; with the §1 daggered \textit{†adiectus} read as
\textit{afflictus} and the abrupt §6 closing \textit{te esse usurum
tuis})}; \textbf{\textit{Fam.} 4.14 (Cicero, Rome, early 46 BC, to
Cn. Plancius --- \textbf{DATE CORRECTION}: \texttt{-0046-07-23}
$\rightarrow$ \texttt{-0046-01-15} month-precision per Perseus
\textit{in. a. 708 (46)}; with the \textit{dignitas}
double-definition opening and the §4 Perseus scribal corruptions
\textit{in ite}, \textit{qui sini})}.
\item \textbf{Worker D (\textit{Fam.} 4.3, 4.15, 7.4, 4.4 --- 4
letters with \textbf{one recipient correction}, mid-late 46 BC):}
\textit{Fam.} 4.3 (Cicero, Rome, c. 12 August 46 BC, to Servius
Sulpicius Rufus --- with the \textit{parietinis rei publicae} ``the
ruined walls of the state'' image preserved); \textit{Fam.} 4.15
(Cicero, Rome, c. 24 August 46 BC, to Cn. Plancius --- the short
follow-up); \textbf{\textit{Fam.} 7.4 (Cicero, in Cumano,
intercalary month after Sept 46 BC --- \textbf{RECIPIENT
CORRECTION}: salutation \texttt{M. CICERO S. D. M. MARIO.}
confirms \textbf{M. Marius}, not Trebatius as the launch prompt
suggested; the very short Cumae arrival note with the
\textit{podagra} ``gout'' joke about putting off appointments)};
\textit{Fam.} 4.4 (Cicero, Rome, c. 15 October 46 BC, to Servius
Sulpicius Rufus --- with the famous \textit{quasi reviviscentis
rei publicae} ``an image, as it were, of a state coming back to
life'' on the Marcellus restoration, and \textbf{two Greek
phrases}: \textit{eironeuesthai} ``to play the ironist'' and
\textit{eironeuomenos} ``ironizing'' in Cicero's self-deprecating
contrast of his eloquence with Sulpicius's).
\end{itemize}

\textbf{Wave 2 (1 worker, 4 letters):}
\begin{itemize}
\item \textbf{Worker E (\textit{Fam.} 6.22, 4.12, 6.20, 5.15 --- 4
letters with \textbf{two corrections}, including the famous
\textit{Fam.} 4.12 MARCELLUS-MURDER letter):}
\textbf{\textit{Fam.} 6.22 (Cicero, Rome, May 46 BC, to
\textbf{Cn. Domitius Ahenobarbus} --- \textbf{DATE CORRECTION}:
\texttt{-0046-11-07} year-precision $\rightarrow$
\texttt{-0046-05-15} month-precision per Perseus \textit{Romae m.
Maio a. 708 (46)}; the consolation/exhortation to the young
Pompeian survivor of Pharsalus, with the long suspended
tetracolon of §2 governed by \textit{oro obtestorque})};
\textbf{\textit{Fam.} 4.12 (\textbf{SERVIUS SULPICIUS RUFUS},
Athens, \textbf{31 May 45 BC}, to Cicero --- \textbf{DIRECTION-
FLIP letter}: salutation \texttt{SERVIVS CICERONI sal. PLVR.},
the corpus's most famous eyewitness report of the
\textbf{MURDER OF M. CLAUDIUS MARCELLUS at the Piraeus} by his
client P. Magius Cilo; \textbf{DATE CORRECTION}:
\texttt{-0045-05-21} year-precision $\rightarrow$
\texttt{-0045-05-31} day-precision per Perseus \textit{pr. K.
Iunias a. 709 (45)} and closing subscript \textit{D. pr. K. Iun.
Athenis}; with the central epigram \textit{vir clarissimus ab
homine deterrimo acerbissima morte est adfectus} and the
Academy-interment/cremation/marble-monument tricolon; STRONG
translator-notes candidate for both the literary qualities and
the date-precision repair)}; \textbf{\textit{Fam.} 6.20 (Cicero,
Astura, late July 45 BC --- recipient confirmed as
\textbf{C. Toranius} per \texttt{CICERO TORANIO S.} salutation,
NOT A. Caecina as the launch prompt suggested; with the
veiled-Caesar reference \textit{recipiet ille se ad tempus} ``if
he gets back in time'' as Caesar still in Spain after Munda, and
the tricolon closing \textit{desiderant et diligunt et colunt})};
\textit{Fam.} 5.15 (Cicero, Astura, December 45 BC, to L.
Lucceius --- the substantial post-Tullia mourning letter with the
parenthetical \textit{dicerem `iucundus,' nisi id verbum in omne
tempus perdidissem} ``I would say `delightful,' had I not put that
word out of service for every season'' and the elaborate Latin
\textit{Litterae} (literary studies / books / letters)
play across §§3-4).
\end{itemize}

\textbf{Metadata corrections committed to \texttt{meta/works.yaml}
during session 30 (7 date corrections; 2 recipient mismatches
noted but salutations were authoritative so no yaml-recipient
change needed since the yaml fields already matched the Latin
salutations):}
\begin{itemize}
\item \textit{Att.} 5.1: \texttt{date} \mbox{-0049-05-06}
$\rightarrow$ \mbox{-0051-05-06} day-precision (Perseus
parenthetical ``(49)'' is corrupted; AUC 703 = 51 BC; content
confirms Cicero outbound to Cilicia).
\item \textit{Att.} 5.7: \texttt{date} \mbox{-0049-05-22}
$\rightarrow$ \mbox{-0051-05-22} day-precision (same calendar
correction as 5.1; the brief Tarentum letter from the same
journey).
\item \textit{Fam.} 5.21: \texttt{date} \mbox{-0046-06-18}
year-precision $\rightarrow$ \mbox{-0046-04-01} month-precision
(per Perseus \textit{in. aut med. m. April. a. 708 (46)}).
\item \textit{Fam.} 4.13: \texttt{date} \mbox{-0046-06-22}
year-precision $\rightarrow$ \mbox{-0046-08-01} month-precision
(per Perseus \textit{ui. in. Sext. a. 708 (46)}).
\item \textit{Fam.} 4.14: \texttt{date} \mbox{-0046-07-23}
year-precision $\rightarrow$ \mbox{-0046-01-15} month-precision
(per Perseus \textit{in. a. 708 (46)}).
\item \textit{Fam.} 6.22: \texttt{date} \mbox{-0046-11-07}
year-precision $\rightarrow$ \mbox{-0046-05-15} month-precision
(per Perseus \textit{Romae m. Maio a. 708 (46)}).
\item \textit{Fam.} 4.12: \texttt{date} \mbox{-0045-05-21}
year-precision $\rightarrow$ \mbox{-0045-05-31} day-precision
(per Perseus \textit{pr. K. Iunias a. 709 (45)}; the Marcellus-
murder letter, now anchored to its exact day).
\end{itemize}

\textbf{Pending file renames carried forward to Alexander's
handoff} (the sandbox cannot delete files, so renames happen on
Alexander's side):
\begin{itemize}
\item \textit{Att.} 5.1: \texttt{049bc-ad-atticum-05-01.\{tex,json\}}
across \texttt{latin/}, \texttt{english/}, \texttt{headnotes/},
\texttt{data/parallel/letters/} $\rightarrow$ rename prefix to
\texttt{051bc-}; update the three path fields in \texttt{meta/
works.yaml} to match.
\item \textit{Att.} 5.7: same pattern, \texttt{049bc-} $\rightarrow$
\texttt{051bc-}.
\item Carry-over from session 28: \textit{Fam.} 13.09 still under
\texttt{005bc-} prefix, should be \texttt{050bc-}.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Fam.} 4.12 \textit{vir clarissimus ab
homine deterrimo acerbissima morte est adfectus} epigram.}
Servius Sulpicius's central antithesis on the Marcellus murder,
preserved with the parallel superlatives ``a most illustrious
man / a most worthless one'' and ``the harshest of deaths.''
Strong translator-notes candidate for the literary register of
the Sulpicius letter --- one of the rare moments in the
correspondence where a non-Cicero hand produces sustained
high-style Latin.
\item \textbf{The \textit{Fam.} 16.18 medical-Greek catalogue.}
Six Greek phrases in one paragraph (\textit{diaphoresin},
\textit{pepsin}, \textit{akopian}, \textit{peripaton symmetron},
\textit{tripsin}, \textit{eulysian koilias}) form a compact
clinical-regimen vocabulary for Tiro's recuperation; structural
analogue to the Fam 7.26 dietary-letter parody-vocabulary noted
in session 29.
\item \textbf{The \textit{Fam.} 4.4 \textit{quasi reviviscentis
rei publicae} on the Marcellus restoration.} ``An image, as it
were, of a state coming back to life'' --- one of Cicero's most
politically pointed phrasings under Caesar's dictatorship.
Paired with the \textit{eironeuesthai}/\textit{eironeuomenos}
self-deprecation Greek-doublet, the letter contains the entire
emotional shape of post-Pharsalus Ciceronian rhetoric in compact
form.
\item \textbf{The \textit{Att.} 5.1 Perseus AUC corruption.} Both
\textit{Att.} 5.1 and 5.7 have Perseus parentheticals of the form
\texttt{a. 70X (49)} where the AUC year is 70X and the BC year
should be 51 BC (AUC 703) or 51 BC (AUC 705 corrected). Perseus's
parenthetical apparently subtracts AUC from 754 instead of
753+1, producing a systematic two-year error. Worth a
sustained translator-note OR a standing audit caveat in
\texttt{CLAUDE.md} on the Perseus dateline parsing.
\item \textbf{Three recipient-mismatch flags resolved against
salutations:} (i) launch prompt suggested \textit{Fam.} 4.13 to
Sulpicius; salutation \texttt{P. FIGVLO} settles it as P. Nigidius
Figulus. (ii) launch prompt suggested \textit{Fam.} 7.4 to
Trebatius; salutation \texttt{M. MARIO} settles it as M. Marius.
(iii) launch prompt suggested \textit{Fam.} 6.20 to A. Caecina;
salutation \texttt{TORANIO} (matching meta) settles it as
C. Toranius. The \texttt{meta/works.yaml} \texttt{recipient:}
fields already match the salutations in all three cases; no yaml
change needed, but the pattern (when in doubt, the salutation
governs) is worth a CLAUDE.md note.
\item \textbf{The \textit{Fam.} 5.15 \textit{Litterae} word-play.}
Cicero's pun across §§3-4 on \textit{litterae} as letters
(correspondence) / letters (literary studies) / Letters (books)
--- the central crux of the post-Tullia letter to the historian
Lucceius. Strong sustained-translator-note candidate.
\item \textbf{The \textit{Fam.} 5.20 contested HS sums.} The
\texttt{HS xxx} / \texttt{HS xix} / \texttt{HS xxii} / \texttt{HS
c} figures in §§3-4 of the long Mescinius Rufus accounts letter
diverge between manuscripts; most modern editors emend ``19{,}000''
to ``1{,}900{,}000'' to make the Volusius-Valerius dispute
intelligible. Preserved as Perseus prints them, with a
\texttt{notes} flag in the parallel-sidecar JSON. Worth a
sustained translator-note in the apparatus pass.
\end{itemize}

\textbf{Suggested next translation batch} (when session 30 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 30:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice S' continuation (50 pending letters earlier
than the -0043-07-28 10.24 marker, down from 71 at start of
this session):} the next natural clusters are (a) the remaining
\textit{Att.} 12 / 13 / 14 / 15 letters of post-Tullia mourning
and 44 BC; (b) further \textit{Q. fr.} letters not yet covered;
(c) more 49--46 BC scattered \textit{Fam.} letters across the
civil-war and post-Pharsalus years.
\item \textbf{Slice F (the nine no-Perseus deferred letters):}
\textit{Fam.} 11.8, 11.17, 11.28 (all 43 BC), \textit{Fam.}
5.10 (51 BC), \textit{Fam.} 9.25, \textit{Att.} 13.15, 13.18,
13.36, plus the \textit{Ad Brutum} no-Perseus deferred (01-15,
01-16, 02-06, 02-07, 02-08 --- 5 letters whose
\texttt{latin\_source\_url} points to thelatinlibrary.com;
require manual Latin sourcing from Shackleton Bailey / Teubner
/ OCT). Held as a single-session manual-fetch batch.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, one per session, not in parallel):}
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} 429+ entity stubs
in \texttt{data/entities.json} remain ripe for an aggressive
parallel apparatus pass.
\item \textbf{File-rename carry-overs:} \textit{Att.} 5.1, 5.7
(\texttt{049bc-} $\rightarrow$ \texttt{051bc-}) and \textit{Fam.}
13.09 (\texttt{005bc-} $\rightarrow$ \texttt{050bc-}); sandbox
cannot delete files, so Alexander handles at handoff or
follow-up session.
\end{itemize}


\textbf{Translation state (post-Cowork-session-29):} \textbf{880 /
958 works drafted (\~91.9\%)}. \textbf{Latest drafted by deep
chronology is unchanged} from sessions 27 and 28: \textit{Ad
Familiares} 10.24 (Plancus's camp in Gaul, 28 July 43 BC) remains
the marker, because all 34 letters drafted this session are dated
earlier than that. Session 29 \textbf{continued the chronological-
gap sweep (Slice S')}, drafting 34 letters across two waves
(seven workers total): the entire \textit{Ad Brutum} cluster (21
letters, books 1 and 2; the Perseus-available ones --- 01-15,
01-16, 02-06, 02-07, 02-08 remain as Latin-Library no-Perseus
deferred), plus 13 scattered \textit{Ad Familiares} letters of
46-43 BC. The chronological-gap warning falls from \textbf{102}
pending-earlier-than-marker (post-session-28) to \textbf{71}
(post-session-29) --- a 31-letter reduction inside the gap (three
of the 34 drafted were originally year-precision placeholders
dated after the 28 July marker; their corrected dates pull them
inside the gap).

\textbf{Cowork session 29 --- 34 letters drafted across two waves
(seven workers total):}

\textbf{Wave 1 (4 workers, 21 letters --- the \textit{Ad Brutum}
sweep, all 43 BC):}
\begin{itemize}
\item \textbf{Worker A (\textit{ad-brutum} 01-03, 01-05, 02-01,
02-02, 02-04 --- 5 Cicero-to-Brutus letters of April-May 43 BC):}
the Mutina-period cluster, with the famous war-arithmetic letters;
includes the §3 daggered crux \textit{†eam semel cepit, mihi crede,
non erit id. Apr.†} in 02-04 (preserved under daggers), the §3
lacuna ``* *'' at the end of 02-02, the Lex Iulia citation
\texttt{QVI PETET CVIVSVE RATIO HABEBITVR} in 01-05 (preserved
small-caps), and the \textit{auspicia ad patres redire} interregnum
mechanism. PM flag: 02-01 Perseus dateline is \textit{ex. m. Mart.
ant in. Apr.}, broader than meta's day-precision \mbox{-0043-04-13}
--- meta kept for stability.
\item \textbf{Worker B (\textit{ad-brutum} 01-02, 01-09, 01-10,
01-12, 01-14 --- 5 Cicero-to-Brutus letters, May-July 43 BC):}
\textbf{01-09 (Cicero, Rome, early July 43 BC --- \textbf{MAJOR
DATE CORRECTION}: \texttt{-0043-02-26} year-precision $\rightarrow$
\texttt{-0043-07} month-precision, per Perseus \textit{in. Quint.}
--- the consolation letter for Brutus on the death of Porcia)};
01-10 with the corrupt Perseus reading \textit{dolebiwn} (read as
\textit{dolebam}); 01-12 with the Servilia/Junia plea for Lepidus's
children; 01-14 with the famous closing on the Ides of March vs
``coming in good time.''
\item \textbf{Worker C (\textit{ad-brutum} 02-03, 02-05, 01-06,
01-08, 01-11 --- 5 mixed Cicero/Brutus letters, March-June 43 BC):}
\textbf{02-03 (Brutus, Dyrrachium, 1 April 43 BC --- \textbf{DATE
CORRECTION}: \texttt{-0043-03-32} broken date $\rightarrow$
\texttt{-0043-04-01} day-precision, per Perseus \textit{i K. Apr.})};
02-05 the famous Cicero-on-Mutina letter (14 April, ``what is being
decided in this war is whether we are to exist or not'');
01-06 (Brutus, \textbf{ex castris ad imam Candaviam} per its own
subscript, not Romae as Perseus header says --- flagged); 01-11
with the small Perseus lacuna \textit{statuit id sibi * *}.
\item \textbf{Worker D (\textit{ad-brutum} 01-01, 01-04, 01-07,
01-13, 01-17, 01-18 --- 6 letters with \textbf{five major date
corrections}):}
\begin{itemize}
\item \textbf{01-01: \texttt{-0043-06-18} year-precision $\rightarrow$
\texttt{-0043-04-13} day-precision} (Perseus dateline \textit{eodem
die quo ep. 2a}, i.e. the same day as 2.1).
\item \textbf{01-04: \texttt{-0043-09-21} year-precision $\rightarrow$
\texttt{-0043-05-13} day-precision} (Perseus dateline \textit{iii
ante prid. id. Mai.}, printed \textit{iii antprid.} due to OCR).
01-04 contains the only Greek of the whole \textit{Ad Brutum}
batch: \textit{e)mfatikw/teron} (\textit{emphatikoteron}, ``to put
it more emphatically'') in 01-01 §1; rendered \textit{[Greek:
emphatikoteron]} per STYLE.md.
\item \textbf{01-17: \texttt{-0043-10-06} year-precision $\rightarrow$
\texttt{-0043-05-15} month-precision} (Perseus dateline \textit{m.
Maio, ut videtur}). \textbf{01-17 is the FAMOUS LETTER FROM BRUTUS
TO ATTICUS} (\texttt{Brutus Attico salutem}, not to Cicero), the
single-most politically charged surviving document of Brutus's
side, in which he formulates the five-point indictment of Cicero's
deference to Octavian. The closing taunt \textit{nos Idibus
Martiis... vos Nonis Decembribus} (``we on the Ides of March...
you on the Nones of December'') preserved as the rhetorical
centerpiece.
\item \textbf{01-18: \texttt{-0043-11-07} year-precision $\rightarrow$
\texttt{-0043-07-27} day-precision} (Perseus dateline \textit{vi K.
Sex.}, confirmed by closing subscript \textit{vi Kal. Sextilis}).
This pulls 01-18 from late autumn 43 BC up to one day before the
session marker (28 July), a substantial chronological move.
\item 01-07 (Brutus, in castris, 23 June 43 BC) and 01-13 (Brutus,
in castris, 1 July 43 BC) confirmed against Perseus datelines; no
correction needed.
\end{itemize}
\end{itemize}

\textbf{Wave 2 (3 workers, 13 letters --- scattered \textit{Ad
Familiares} 46-43 BC):}
\begin{itemize}
\item \textbf{Worker E (\textit{Fam.} 7.19, 7.24, 7.25, 7.26, 7.28
--- 5 letters of 46-44 BC, the Trebatius / Fadius Gallus / Curius
cluster):} 7.19 (Cicero, near Regium, 29 July 44 BC, to Trebatius
--- minor closing-subscript discrepancy \textit{v K. Sextil.} vs
header \textit{iv K. Sext.}); 7.24, 7.25 (Cicero, Tusculum,
August 45 BC, to Fadius Gallus --- with the \textit{gelōta
sardanion} ``a Sardonic laugh'' Greek of 7.25, the Tigellius/
Sardinian-slaves pun, the \textit{manum de tabula} / \textit{in
catomum Catonianos} jokes about Caesar's return); 7.26 (Cicero,
Tusculum, intercalary 46 BC, to Fadius Gallus --- the famous
DIETARY LETTER on Cicero's illness from ``greens, herbs and roots''
at an augural dinner, with \textbf{four Greek phrases}:
\textit{strangourika kai dysenterika pathē}, \textit{dysenterian},
\textit{litotēta}, \textit{diarroia} --- the medical-legal
parody-vocabulary of the letter); 7.28 (Cicero, Rome, c. August 46
BC, to Curius --- with the Ennius \textit{Thyestes} tag \textit{ubi
nec Pelopidarum} flagged as an allusion candidate).
\item \textbf{Worker F (\textit{Fam.} 7.29, 7.30, 7.31, 7.33 ---
4 letters with \textbf{two date corrections}):}
\textbf{7.29 (M'. Curius, Patrae, 29 October 45 BC, to Cicero ---
DATE CORRECTION: \texttt{-0045-11-01} day-precision $\rightarrow$
\texttt{-0045-10-29} day-precision, per Perseus \textit{iiii K.
Nov.})}; 7.30 (Cicero, Rome, early Jan 44 BC, to Curius --- with
the Ennius-Iphigenia tag \textit{ubi nec Pelopidarum nomen nec
facta audiam}, the half-day Caninius consulship \textit{scito
neminem prandisse}); \textbf{7.31 (Cicero, Rome, c. February 44 BC,
to Curius --- \textbf{MAJOR DATE CORRECTION}: \texttt{-0044-12-04}
year-precision $\rightarrow$ \texttt{-0044-02-15} month-precision,
per Perseus \textit{ut Febr. a. 710})}; 7.33 (Cicero, Tusculum,
mid-July 46 BC, to Volumnius Eutrapelus --- with the corrupt Greek
\textit{Emeisi} marked as \textit{[Greek corrupt: lectio incerta]},
the Accius \textit{Philoctetes} quotation \textit{pinnigero, non
armigero}, and the politically charged \textit{deponere illam iam
personam} abdication-of-public-life note under Caesar).
\item \textbf{Worker G (\textit{Fam.} 9.8, 9.14, 9.24, 15.20 --- 4
letters, including the \textbf{ACADEMICA DEDICATION} 9.8 and the
\textit{res publica istic est} TREBONIUS letter):} \textbf{9.8
(Cicero, Tusculum, 11-12 July 45 BC, to Varro --- the
\textbf{DEDICATION LETTER FOR THE \textit{ACADEMICA}}: the
\textit{quattuor admonitores} (the four books of the work
personified) image preserved; the programmatic letter on
philosophical dedication and reciprocal literary munus)}; 9.14
(Cicero, Pompeii, 3 May 44 BC, to Dolabella, addressed
\texttt{CICERO DOLABELLAE CONSVLI SVO S.} --- with the
\textit{amare / diligere} distinction in §5, the legal sense of
\textit{cernere} (acceptance of inheritance), and the Homeric
\textit{regum regi} (Agamemnon = \textit{anax andron}) flagged);
9.24 (Cicero, Rome, c. February 43 BC, to Papirius Paetus --- with
the substantial Greek-dining-vocabulary paragraph contrasting
\textit{sumpo/sia} and \textit{su/ndeipna} ``drinkings-together
/ dinings-together'' against Latin \textit{convivia}
``livings-together,'' the philological centerpiece of the letter;
candidate for a glossary entry on Roman dining vocabulary);
\textbf{15.20 (Cicero, Rome, c. April 44 BC, to \textbf{TREBONIUS}
(\texttt{M. CICERO S. D. C. TREBONIO}) --- \textbf{not Vatinius as
the launch prompt speculated}, recipient corrected from Latin
salutation: the famous epigram \textit{res enim publica istic est}
``for the Republic is over there'' rendered as the political center
of the letter, strong translator-notes candidate)}.
\end{itemize}

\textbf{Metadata corrections committed to \texttt{meta/works.yaml}
during session 29 (8 date corrections + 2 location-string
normalisations):}
\begin{itemize}
\item \textit{Ad Brutum} 1.1: \texttt{date} \mbox{-0043-06-18}
year-precision $\rightarrow$ \mbox{-0043-04-13} day-precision,
\texttt{location\_written} normalised from \texttt{eodem die quo
ep. 2a.} to \texttt{Romae}.
\item \textit{Ad Brutum} 1.4: \texttt{date} \mbox{-0043-09-21}
year-precision $\rightarrow$ \mbox{-0043-05-13} day-precision,
\texttt{location\_written} normalised from \texttt{Dyrrachi iii
antprid.} (OCR artifact) to \texttt{Dyrrachi}.
\item \textit{Ad Brutum} 1.9: \texttt{date} \mbox{-0043-02-26}
year-precision $\rightarrow$ \mbox{-0043-07-01} month-precision,
\texttt{location\_written} normalised from \texttt{Romae. in.
Quint. ...ut} to \texttt{Romae}.
\item \textit{Ad Brutum} 1.17: \texttt{date} \mbox{-0043-10-06}
year-precision $\rightarrow$ \mbox{-0043-05-15} month-precision,
\texttt{location\_written} \texttt{m.} (junk) $\rightarrow$
\texttt{null}.
\item \textit{Ad Brutum} 1.18: \texttt{date} \mbox{-0043-11-07}
year-precision $\rightarrow$ \mbox{-0043-07-27} day-precision.
\item \textit{Ad Brutum} 2.3: \texttt{date} \mbox{-0043-03-32}
broken-date $\rightarrow$ \mbox{-0043-04-01} day-precision,
\texttt{location\_written} normalised from \texttt{Dyrrach} to
\texttt{Dyrrachi}.
\item \textit{Fam.} 7.29: \texttt{date} \mbox{-0045-11-01}
day-precision $\rightarrow$ \mbox{-0045-10-29} day-precision (per
Perseus \textit{iiii K. Nov.}).
\item \textit{Fam.} 7.31: \texttt{date} \mbox{-0044-12-04}
year-precision $\rightarrow$ \mbox{-0044-02-15} month-precision
(per Perseus \textit{ut Febr. a. 710}).
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Ad Brutum} 1.17 \textit{Idibus Martiis /
Nonibus Decembribus} taunt.} The closing rhetorical reversal
(``you on the Nones of December'' = the date of Cicero's
suppression of the Catilinarian conspiracy) is Brutus's most
politically pointed surviving epigram, deployed against Cicero's
deference to Octavian. The whole letter is the corpus's most
direct critique by Brutus of Cicero's policy; its mid-May 43 BC
date (corrected from October) places it in the same political
moment as Brutus's growing distrust of Octavian's loyalty to the
Senate. Translator-note candidate for the political register.
\item \textbf{The \textit{Ad Brutum} 2.4 \textit{†eam semel cepit,
mihi crede, non erit id. Apr.†} crux.} A daggered passage of
Perseus's text, on which editions differ. Preserved under daggers
in the English; flagged in the parallel JSON; a recurring crux
worth a sustained translator-note when the apparatus pass arrives.
\item \textbf{The \textit{Ad Brutum} 2.3 broken-date repair.}
\texttt{-0043-03-32} (March 32, impossible) was clearly an OCR/
transcription error; Perseus dateline \textit{i K. Apr.} +
closing subscript \textit{Kalend. Apr. Dyrrhachio} fixes it
unambiguously to 1 April 43 BC. The kind of metadata error that
the chronological-gap warning surfaces when a clean session-29
review looks at it.
\item \textbf{The \textit{Ad Familiares} 7.26 dietary-letter
parody-vocabulary.} \textit{strangourika kai dysenterika pathē},
\textit{dysenterian}, \textit{litotēta}, \textit{diarroia} ---
four Greek medical phrases deployed in mock-clinical register over
a comic story about Cicero being made ill not by rich Caesarian
food but by ``greens, herbs and roots'' served at an augural
dinner. The lex-sumptuaria/terra-nata joke is the structural
centerpiece. A clear sustained-translator-note candidate when the
apparatus pass arrives.
\item \textbf{The \textit{Ad Familiares} 9.24 Greek-dining-
vocabulary paragraph.} \textit{sumposia / syndeipna} (``drinkings-
together / dinings-together'') against Latin \textit{convivia}
(``livings-together''), with Cicero explicitly preferring the
Latin compound because it captures the social-not-just-bodily
nature of the dinner. The philological centerpiece of a late
letter to Paetus on the eve of the Mutina war.
\item \textbf{The \textit{Ad Familiares} 15.20 \textit{res publica
istic est} epigram.} ``For the Republic is over there'' --- to
Trebonius, governor of Asia, one of the Ides-of-March
conspirators. The compactest summary of Cicero's despair of Rome
in spring 44 BC: with the tyrannicides scattered to their
provinces, what remains of public life is wherever they happen to
be, not at Rome.
\item \textbf{The \textit{Ad Familiares} 9.8 \textit{quattuor
admonitores} image.} The four books of the \textit{Academica}
personified as four ``prompters'' or ``reminders'' to Varro --- the
programmatic move that converts the work's dialogue-form into a
literary munus to the dedicatee, framing Varro himself as the
expected reciprocator. Worth a sustained translator-note when the
philosophical-works apparatus pass arrives.
\item \textbf{Three \textit{Ad Brutum} 43 BC year-precision dates
corrected to specific months/days from Perseus datelines.} 1.1
(June 18 $\rightarrow$ April 13), 1.4 (Sept 21 $\rightarrow$ May
13), 1.17 (Oct 6 $\rightarrow$ May 15), 1.18 (Nov 7 $\rightarrow$
July 27): four placeholder dates that were apparently book-
position-based guesses, now anchored to Perseus's TEI
\texttt{<date when="...">} attributes. The pattern (later-numbered
letters in the manuscript ordering sometimes dating EARLIER than
earlier-numbered letters) is normal for the late \textit{Ad
Brutum} corpus, which is not chronologically ordered.
\end{itemize}

\textbf{Suggested next translation batch} (when session 29 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 29:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice S' continuation (71 pending letters earlier
than the -0043-07-28 10.24 marker, down from 102 at the start of
session 28 and 84 at the start of this session):} the next
natural clusters are (a) the remaining 44 BC scattered
\textit{Fam.} letters not yet drafted (\textit{Fam.} 4.3, 4.4,
4.12, 4.13, 4.14, 4.15, 6.20, 6.22 --- 8 letters, the
Servius-Sulpicius-on-the-death-of-Tullia letter 4.5 should already
be drafted; check); (b) the remaining \textit{Att.} 12 / 13 /
14 / 15 letters of post-Tullia mourning and 44 BC; (c) further
\textit{Q. fr.} letters not yet covered.
\item \textbf{Slice F (the four no-Perseus deferred letters):}
\textit{Fam.} 11.8, 11.17, 11.28 (all 43 BC) and \textit{Fam.}
5.10, plus the \textit{Ad Brutum} no-Perseus deferred (01-15,
01-16, 02-06, 02-07, 02-08 --- 5 letters whose
\texttt{latin\_source\_url} points to thelatinlibrary.com; require
manual Latin sourcing from Shackleton Bailey / Teubner / OCT).
Held as a single-session manual-fetch batch.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, one per session, not in parallel):}
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} 429+ entity stubs
in \texttt{data/entities.json} remain ripe for an aggressive
parallel apparatus pass.
\item \textbf{\textit{Fam.} 13.9 file rename} (carried over from
session 28): the four files under the \texttt{005bc-} prefix
should be renamed to \texttt{050bc-}. The sandbox cannot delete
files, so Alexander handles this at handoff or in a follow-up
session.
\end{itemize}


\textbf{Translation state (post-Cowork-session-28):} \textbf{846 /
958 works drafted (\~88.3\%)}. \textbf{Latest drafted by deep
chronology is unchanged} from session 27: \textit{Ad Familiares}
10.24 (Plancus's camp in Gaul, 28 July 43 BC) remains the marker,
because every one of the 33 letters drafted this session is dated
earlier than that. Session 28 \textbf{opened the chronological-gap
sweep (Slice S')}, drafting 33 letters across two parallel waves
(eight workers total): the remaining \textit{Ad Familiares} 13
commendations (9 letters), the remaining \textit{Ad Familiares} 16
Tiro correspondence (9 letters), the opening of the \textit{Ad
Atticum} 12 cluster (12 letters spanning 46 BC into the post-Tullia
mourning of 45 BC), and three of the \textit{Ad Familiares} 7
Trebatius letters of 44 BC. The chronological-gap warning falls
from \textbf{134} pending-earlier-than-marker (post-session-27) to
\textbf{102} (post-session-28) --- a 32-letter reduction inside the
gap (the 33rd, \textit{Fam.} 13.09 to Crassipes, was redated from
the broken \mbox{-0005-02-22} placeholder to \mbox{-0050-01-15}
[winter 51/50 BC at Tarsus], so it remains inside the gap zone).

\textbf{Cowork session 28 --- 33 letters drafted across two
parallel waves (eight workers total):}

\textbf{Wave 1 (4 workers, 18 letters):}
\begin{itemize}
\item \textbf{Worker A (\textit{Fam.} 13.4, 13.5, 13.7, 13.8 ---
the four mid-October 45 BC commendations to Caesarian land
commissioners):} 13.4 (Cicero, Rome, mid-Oct 45 BC, to Q. Valerius
Orca, legatus pro praetore in Africa --- the substantial
commendation for the Volaterrans, with the \textit{quasi divino
consilio} ``by a kind of providential design'' translator-note
candidate); 13.5 (same date, same recipient, the second
commendation for C. Curtius); 13.7 (same date, to C. Cluvius, the
commendation for Atella, with the \textit{negotium \ldots non
iudicium} ``a commission, not a discretion'' rhetorical pivot
flagged); 13.8 (same date, to M. Rutilius, for C. Albinius, with
the Sullan-sales argument from Caesar's own interest preserved
compactly).
\item \textbf{Worker B (\textit{Fam.} 13.9, 13.15, 13.48, 13.50,
13.60 --- 5 scattered commendations, late-50s through 44 BC):}
\textbf{13.9 (Cicero, Tarsus, winter 51/50 BC, to Crassipes ---
\textbf{MAJOR DATE CORRECTION}: \texttt{-0005-02-22} year-precision
placeholder $\rightarrow$ \texttt{-0050-01-15} month-precision, per
Perseus \textit{Tarsi vel ex. a. 703 (51) vel in. a. 704 (50)} ---
the meta date was an apparent typo of \texttt{-0050} for
\texttt{-0005})}; \textbf{13.15 (Cicero, Rome, end May 45 BC, to
Caesar --- the famous \textbf{HOMERIC COMMENDATION} for the younger
Precilius, the corpus's most literary commendation: \textbf{seven
Greek phrases}, including \textit{Iliad} 9.587
$(\dot{\alpha}\lambda\lambda$' $\dot{\epsilon}\mu\delta\nu$ $o\dot{\upsilon}$ $\pi o\tau\epsilon$ $\theta\upsilon\mu\delta\nu$),
\textit{Iliad} 22.304-5
$(\mu\dot{\eta}$ $\mu\dot{\alpha}\nu$ $\dot{\alpha}\sigma\pi o\upsilon\delta\dot{\iota}$),
\textit{Iliad} 6.208 / 11.784
($\alpha\dot{\iota}\dot{\epsilon}\nu$ $\dot{\alpha}\rho\iota\sigma\tau\epsilon\dot{\upsilon}\epsilon\iota\nu$),
and Euripides fr. 905 Nauck
($\mu\iota\sigma\tilde{\omega}$ $\sigma o\varphi\iota\sigma\tau\dot{\eta}\nu$);
\textbf{date corrected} from \texttt{-0045-08-28} year-precision
$\rightarrow$ \texttt{-0045-05-31} month-precision, per Perseus
\textit{ex. m. Mai. a. 709 (45)})}; \textbf{13.48 (Cicero, Rome,
autumn 47 BC, to C. Sextilius Rufus, quaestor of Cyprus --- the
single-section short commendation; \textbf{date corrected} from
\texttt{-0047-05-05} year-precision $\rightarrow$
\texttt{-0047-10-15} month-precision, per Perseus
\textit{autumno anni 707 (47)})}; 13.50 (Cicero, Rome, January 44
BC, to Acilius proconsul of Achaia, the second Curius commendation,
with the proverbial \textit{sartum et tectum} ``patched and
roofed'' preserved); \textbf{13.60 (Cicero, Rome \textit{post
reditum}, late 46 BC, to C. Munatius --- \textbf{date corrected}
from \texttt{-0046-05-17} year-precision $\rightarrow$
\texttt{-0046-11-15} month-precision, per Perseus \textit{post
reditum fortasse ex. a. 708 (46)}; one minor OCR artifact noted in
the fetched Latin, \textit{honam} for \textit{bonam})}.
\item \textbf{Worker C (\textit{Fam.} 16.17, 16.19, 16.22, 16.26
--- 4 Tiro letters of the 45 BC cluster + 1 from 44 BC):} 16.17
(Cicero, Astura, 29 July 45 BC, to Tiro --- with the rare Greek
verb $\dot{\alpha}\varphi\omega\mu\dot{\iota}\lambda\eta\sigma\alpha$
\textit{aph\=omil\=esa} = ``prised myself loose,'' translator-note
candidate); 16.19 (Cicero, Tusculum, August 45 BC, to Tiro --- short
no-Greek note); 16.22 (Cicero, Astura, 27 July 45 BC, to Tiro ---
with the obscure \textit{quadrimo Catone} ``four-year-old Cato''
reference to the lost \textit{Cato} laudatio, and the
Demetrius/Phalereus/Billienus pun); 16.26 (Q. Cicero \textit{the
brother}, place uncertain, July 44 BC, to Tiro --- salutation
\texttt{QVINTVS TIRONI SV0 P. S. D.} with OCR-quirky \texttt{0}
preserved per transmitted-form policy).
\item \textbf{Worker D (\textit{Fam.} 16.21, 16.23, 16.24, 16.25,
16.27 --- 5 Tiro letters of 44 BC, including the two letters from
M. Cicero filius in Athens):} \textbf{16.21 (\textbf{M. Cicero
filius (the son)}, Athens, c.~15 July 44 BC, to Tiro --- THE
\textbf{MAJOR ATHENS-STUDENT LETTER}, the longest in the batch
(\~735 words, multi-section); \textbf{six Greek phrases} including
\textit{philologia}, \textit{suz\=et\=esis},
\textit{hupomn\=emata}, \textit{sumphilologein} --- the son's
performative Greek register about his philosophy and rhetoric
studies under Cratippus, with the affectionate-teasing image of his
slave Anteros buying farm gear ``saving seeds in a corner of his
cloak'')}; 16.23 (Cicero, Tusculum, 28 May 44 BC, to Tiro --- with
the proverbial $\gamma\dot{o}\nu\upsilon$ $\kappa\nu\dot{\eta}\mu\eta\varsigma$
\textit{gonu kn\=em\=es} ``the knee is closer than the shin''
self-interest proverb, and the corrupt \textdagger{}n
preserved as \textdagger{}N); 16.24 (Cicero, Arpinum, 11 Nov 44
BC, to Tiro --- with the \textit{prora et puppis} ``stem and
stern'' Greek-via-Latin proverb); 16.25 (M. Cicero filius, Athens,
September 44 BC, to Tiro --- the shorter son's-letter); 16.27 (Q.
Cicero \textit{the brother}, place uncertain, December 44 BC, to
Tiro --- with ``Caesena'' and ``Cossutian shops'' as proverbial
bywords for worthless property).
\end{itemize}

\textbf{Wave 2 (4 workers, 15 letters):}
\begin{itemize}
\item \textbf{Worker E (\textit{Att.} 12.2, 12.3, 12.4, 12.5 ---
the opening of the \textit{Att.} 12 cluster, April-July 46 BC,
Tusculum):} 12.2 (Cicero, Rome, before mid-April 46 BC --- the
Balbus-builds-while-Africa-burns banter, three Greek phrases
including $\beta\epsilon\beta\dot{\iota}\omega\tau\alpha\iota$
\textit{bebi\=otai} ``one has been done with living''); 12.3
(Cicero, Tusculum, 11 June 46 BC --- the long letter on
$\dot{\alpha}\gamma o\eta\tau\epsilon\dot{\upsilon}\tau\omega\varsigma$
\textit{ago\=eteut\=os} ``without enchantment,'' the technical
debt-settlement vocabulary \textit{hasta} / \textit{delegatio a
mancipe} / \textit{Vettieni condicio semissem}, and the
\textit{Metonis annus} ``Metonic year'' joke); \textbf{12.4 (Cicero,
Tusculum, 15 June 46 BC --- the \textbf{CATO LAUDATIO LETTER}: the
famous tricolon on Cato \textit{foresaw / fought / died-to-not-see}
preserved; the $\pi\rho\dot{o}\beta\lambda\eta\mu\alpha$
$\dot{A}\rho\chi\iota\mu\dot{\eta}\delta\epsilon\iota o\nu$
``Archimedean problem'' Greek phrase)}; \textbf{12.5 (Cicero,
Tusculum, mid-July 46 BC --- the densest Greek passage of the
batch, with the Pindaric tag $\ddot{\alpha}\mu\pi\nu\epsilon\upsilon\mu\alpha$
$\sigma\epsilon\mu\nu\dot{o}\nu$ $\dot{A}\lambda\varphi\epsilon\iota o\tilde{\upsilon}$
\textit{ampneuma semnon Alpheiou} (Pindar \textit{Olympian} 1, of
the Syracusan Arethusa) Cicero quotes back from Atticus's own
letter; allusions-sidecar candidate)}.
\item \textbf{Worker F (\textit{Att.} 12.6, 12.7, 12.8, 12.9, 12.10
--- 5 letters, including the \textbf{INTERCALARY-MONTH DATE
CORRECTIONS}):} \textbf{12.6, 12.7, 12.8 (Cicero, Tusculum, m.
intercalari 46 BC --- THESE THREE LETTERS ALL FALL IN THE
\textbf{CAESARIAN INTERCALARY MONTH} of 46 BC (the famous
\textit{annus confusionis ultimus} 67-day intercalation between Nov
and Dec 46 BC before the Julian calendar started 1 Jan 45 BC);
\textbf{major meta-date corrections}: 12.6 \texttt{-0046-07-03}
$\rightarrow$ \texttt{-0046-11-15}, 12.7 \texttt{-0046-08-04}
$\rightarrow$ \texttt{-0046-11-20}, 12.8 \texttt{-0046-09-05}
$\rightarrow$ \texttt{-0046-11-25}, all per Perseus \textit{m.
interc. post a. 708 (46)}; the location\_written for all three
extended to \texttt{in Tusculano (m. intercalari)}; 12.6 contains
the Eupolis/Aristophanes self-correction to the \textit{Orator},
12.8 contains the \textit{fenicularium / Martium campum} pun on the
Spanish ``Fennel-field'' (Munda) vs Rome's election campus)}; 12.9
(Cicero, Astura, 27 July 45 BC, to Atticus --- short post-Tullia
withdrawal-register letter, with the
$\ddot{\omega}$ $\dot{\alpha}\pi\epsilon\rho\alpha\nu\tau o\lambda o\gamma\dot{\iota}\alpha\varsigma$
$\dot{\alpha}\eta\delta o\tilde{\upsilon}\varsigma$
\textit{aperantologias a\=edous} ``unending tedious chatter''
Greek; the sly Macedonian \textit{Amyntae filius} sneer for some
local pretender); \textbf{12.10 (Cicero, Astura, 28 July 45 BC, to
Atticus --- with the \textbf{textual crux} \textdagger{}testamento\textdagger{}
preserved under daggers, the philosophical-consolation
\textit{impetret ratio quod dies impetratura est} ``that reason
should win the point that time would win in the end'' rendered with
its weight, and the $\dot{\epsilon}\pi\iota\delta\dot{\eta}\mu\iota o\nu$
\textit{epid\=emion} ``local infection'' on a household death)}.
\item \textbf{Worker G (\textit{Att.} 12.11, 12.12, 12.1 --- 3
letters, with the \textbf{POST-TULLIA MOURNING-FANUM LETTER}
12.12):} 12.11 (Cicero, Tusculum, intercalary month 46 BC, to
Atticus --- with the single Greek $\sigma\upsilon\mu\pi\dot{\alpha}\sigma\chi\omega$
\textit{sumpasch\=o} ``share her feeling'' and the elliptical
``alteram vero illam'' on a rejected marriage candidate kept
elliptical per STYLE.md letters policy); \textbf{12.12 (Cicero,
Astura, 16 March 45 BC, to Atticus --- THE \textbf{POST-TULLIA
MOURNING / FANUM LETTER}: spare, weighty, on the planned shrine
(\textit{fanum}) for Tullia and the island-vs-\textit{horti}
debate; \textbf{five Greek phrases} including
$\dot{\alpha}\pi o\theta\dot{\epsilon}\omega\sigma\iota\nu$
\textit{apoth\=eosin} ``consecration,''
$\dot{\epsilon}\kappa\tau o\pi\iota\sigma\mu\dot{o}\varsigma$
\textit{ektopismos} ``remoteness,''
$\mu\epsilon\theta\alpha\rho\mu\dot{o}\sigma o\mu\alpha\iota$
\textit{metharmosomai} ``make the adjustment,'' and
$\dot{\alpha}\nu\epsilon\mu\dot{\epsilon}\sigma\eta\tau o\nu$
$\gamma\dot{\alpha}\rho$ \textit{anemes\=eton gar} ``for that gives
no offense''; the legal-technical \textit{Balbi regia condicio est
delegandi} ``Balbus's terms for assigning the debt are princely''
preserved)}; 12.1 (Cicero, Arpinum, 24 Nov 46 BC, to Atticus ---
the \textbf{NUMBERING-ANOMALY LETTER}: 12.1 is dated later than
12.2-12.8 because Perseus places it Nov 46 BC after the
intercalary-month cluster; flagged in the headnote; with the
$\gamma\epsilon\rho o\nu\tau\iota\kappa\dot{o}\nu$ ``the mark of an
old man'' Greek and the \textit{garrimus quicquid in buccam}
``chatter whatever first comes to mind'' idiom rendered by
function).
\item \textbf{Worker H (\textit{Fam.} 7.20, 7.21, 7.22 --- 3
letters of the Trebatius cluster, June-July 44 BC):} 7.20 (Cicero,
Velia, 20 July 44 BC, to Trebatius --- with the Greek title
\textit{Nicon's} $\Pi\epsilon\rho\dot{\iota}$ $\pi o\lambda\upsilon\varphi\alpha\gamma\dot{\iota}\alpha\varsigma$
\textit{peri polyphagias} ``On Overeating,'' and the
\textit{Velia/Lupercal} affection-of-friend wordplay); 7.21
(Cicero, Tusculum, late June 44 BC, to Trebatius --- with the
\textit{sponsio} formula \texttt{SI BONORVM TVRPILIAE
POSSESSIONEM\ldots} preserved in \texttt{\textbackslash{}textsc} as
a quoted legal formula, on \textit{testamenti factio}); 7.22
(Cicero, Tusculum, June 44 BC, to Trebatius --- the jurists' joke
where Cicero ``yields to Scaevola and Testa,'' i.e. to Trebatius
himself, since \textit{Testa} is Trebatius's cognomen). \textbf{NOTE:}
\textit{Fam.} 7.19 was assigned to Worker H but the Latin was not
pre-fetched; it remains pending and was correctly skipped.
\end{itemize}

\textbf{Metadata corrections committed to \texttt{meta/works.yaml}
during session 28 (7 date corrections + 3 location-string
extensions):}
\begin{itemize}
\item \textit{Fam.} 13.9: \texttt{date} \mbox{-0005-02-22}
year-precision $\rightarrow$ \mbox{-0050-01-15} month-precision,
\texttt{date\_precision} \texttt{year} $\rightarrow$ \texttt{month},
\texttt{location\_written} normalised from the corrupt
\texttt{', ut videtur, Tarsi vel'} to \texttt{Tarsi}, per Perseus
\textit{Tarsi vel ex. a. 703 (51) vel in. a. 704 (50)}. The
\texttt{-0005} year was almost certainly a typo for \texttt{-0050}.
\textbf{File-rename note for handoff:} the Latin/English/headnote/
parallel-JSON files are still at the \texttt{005bc-} prefix
(workers correctly used the existing prefix to match the Latin
filename); Alexander may rename these to \texttt{050bc-} at
handoff, and update the four \texttt{*\_file:} paths in works.yaml
to match.
\item \textit{Fam.} 13.15: \texttt{date} \mbox{-0045-08-28}
year-precision $\rightarrow$ \mbox{-0045-05-31} month-precision,
per Perseus \textit{ex. m. Mai. a. 709 (45)}.
\item \textit{Fam.} 13.48: \texttt{date} \mbox{-0047-05-05}
year-precision $\rightarrow$ \mbox{-0047-10-15} month-precision,
per Perseus \textit{autumno anni 707 (47)}.
\item \textit{Fam.} 13.60: \texttt{date} \mbox{-0046-05-17}
year-precision $\rightarrow$ \mbox{-0046-11-15} month-precision,
per Perseus \textit{post reditum fortasse ex. a. 708 (46)}.
\item \textit{Att.} 12.6: \texttt{date} \mbox{-0046-07-03}
year-precision $\rightarrow$ \mbox{-0046-11-15} month-precision,
\texttt{location\_written} extended to \texttt{in Tusculano (m.
intercalari)}, per Perseus \textit{m. interc. post a. 708 (46)}.
\item \textit{Att.} 12.7: \texttt{date} \mbox{-0046-08-04}
year-precision $\rightarrow$ \mbox{-0046-11-20} month-precision,
\texttt{location\_written} extended likewise, per Perseus
\textit{m. interc. post a. 708 (46)}.
\item \textit{Att.} 12.8: \texttt{date} \mbox{-0046-09-05}
year-precision $\rightarrow$ \mbox{-0046-11-25} month-precision,
\texttt{location\_written} extended likewise, per Perseus
\textit{m. interc. post a. 708 (46)}.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Fam.} 13.15 Homeric cento for Caesar.}
Seven Greek tags (\textit{Iliad} 9.587, 17.591, 22.304-5, 1.343/
3.109, 6.208/11.784; \textit{Odyssey} 1.302/3.200; Euripides fr.
905 Nauck) embedded in a single commendation for the younger
Precilius. The corpus's only commendation that proceeds by Homeric
quotation; the politically delicate-to-Caesar register is the
point. The Pindaric register of \textit{Att.} 12.5 is the
adjacent example of how Cicero deploys high-Greek when he wants to
soften a request.
\item \textbf{The \textit{Att.} 12.5 Pindaric quotation.}
$\ddot{\alpha}\mu\pi\nu\epsilon\upsilon\mu\alpha$
$\sigma\epsilon\mu\nu\dot{o}\nu$ $\dot{A}\lambda\varphi\epsilon\iota o\tilde{\upsilon}$
\textit{ampneuma semnon Alpheiou} ``the holy breathing-place of
Alpheus,'' from Pindar \textit{Olympian} 1, of the Syracusan
Arethusa spring. Cicero is quoting Atticus back at himself (``ut
scribis''), inside an embedded metaphor for relief from
mourning-cares. Allusions-sidecar candidate.
\item \textbf{The 46 BC intercalary-month cluster.} \textit{Att.}
12.6, 12.7, 12.8 (and 12.11) all carry Perseus \textit{m. interc.
post a. 708 (46)} datelines, meaning Caesar's 67-day intercalation
between November and December 46 BC. This is the
\textit{ultimus annus confusionis} before the Julian calendar took
effect on 1 January 45 BC. The placeholder meta dates
(\texttt{-0046-07-03}, \texttt{-0046-08-04}, \texttt{-0046-09-05})
were summer/autumn anchors not supported by any source; the
corrections cluster them in mid-to-late November 46 BC. Worth a
brief headnote convention going forward: ``the intercalary period
of 46 BC.''
\item \textbf{The \textit{Att.} 12.4 Cato tricolon.} The famous
\textit{providet, gerit, occidit} construction on the younger
Cato --- ``he foresaw, he fought, he died not to see'' --- preserved
without breaking the three-clause architecture in English.
Cicero's own laudatio \textit{Cato} (lost) is the rhetorical
fountainhead for this passage; the \textit{Fam.} 16.22
\textit{quadrimo Catone} ``four-year-old Cato'' reference is from
the same lost work.
\item \textbf{The \textit{Fam.} 16.21 son-in-Athens register.}
M. Cicero filius writes in a performative-philosophical Greek-laced
register about his studies under Cratippus, with six Greek tags
including \textit{philologia}, \textit{suz\=et\=esis},
\textit{hupomn\=emata}, \textit{sumphilologein}. The register is
the point: a college-age son writing to his father's freedman in
the high-style of a philosophy student, with an affectionate
undertone (the slave Anteros's farm-gear thrift is the warm
domestic image). \textit{Fam.} 16.25 is the shorter sister-letter.
\item \textbf{The corpus-wide Cicero-to-Tiro register.} Across the
nine Tiro letters drafted this session (16.17, 19, 21, 22, 23, 24,
25, 26, 27): warm but never sentimental, often hurried, sometimes
abrupt. The diction is plain (per STYLE.md), the affection comes
through structure, and the health-anxieties are direct. Worth
flagging as a single voice-policy for the corpus.
\item \textbf{The \textit{Att.} 12.10 \textit{impetret ratio quod
dies impetratura est} formulation.} ``That reason should win the
point that time would win in the end.'' One of the early
post-Tullia philosophical-consolation formulations Cicero develops
in the Astura letters; the same therapeutic premise (Stoic
\textit{ratio} accelerating what time will accomplish anyway) runs
through the \textit{Tusculans} (begun later that year). Worth a
sustained translator-note.
\item \textbf{The \textit{Att.} 12.12 fanum project.} The decision
on where to site Tullia's shrine --- island vs. \textit{horti} ---
crystallised in this letter, written daily to Atticus from Astura.
``\textit{Insula Arpinas habere potest germanam}
$\dot{\alpha}\pi o\theta\dot{\epsilon}\omega\sigma\iota\nu$'' is
the structural centre; the Greek \textit{apoth\=eosin}
``consecration'' carries the technical religious weight that
\textit{fanum} would lose in flat English. Allusions-sidecar
candidate (the \textit{apoth\=eosis} vocabulary is Hellenistic-cult
language).
\item \textbf{The \textit{Fam.} 16.22 \textit{quadrimo Catone}
reference.} ``On the four-year-old Cato'' --- a now-lost childhood
anecdote of the younger Cato from Cicero's own lost laudatio
\textit{Cato}; one of the few residues of that lost work in the
surviving letters. Worth flagging in a future fragments-of-lost-
works pass alongside \textit{Att.} 12.4's tricolon.
\item \textbf{The \textit{Fam.} 7.22 \textit{ego tamen Scaevolae
et Testae adsentior} joke.} Cicero's gag against Trebatius the
jurist: he produces three big juristic names supporting his side,
then ``yields to Scaevola and Testa'' --- but \textit{Testa} is
Trebatius's cognomen, so the punchline is that Cicero is yielding
to Trebatius himself. Preserved by keeping ``Scaevola and Testa''
untouched in English with the headnote unpacking the joke.
\item \textbf{The corpus-wide commendation-formula register.} Of
the nine \textit{Fam.} 13 commendations drafted this session, the
recurring vocabulary --- \textit{commendare}, \textit{necessitudo},
\textit{negotium}, \textit{officium}, \textit{liberalitas} --- has
been kept consistent: \textit{commendare} = ``commend'' or
``recommend'' (the genre verb); \textit{necessitudo} = ``ties''
(plural) or ``connection,'' not ``necessity''; \textit{negotium} =
``commission'' / ``business,'' usually preferring the more concrete
sense; \textit{officium} = ``service'' (rather than ``duty,'' which
moralises Roman political vocabulary). Recommended for a
glossary-policy note.
\end{itemize}

\textbf{Suggested next translation batch} (when session 28 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 28:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice S' continuation (the chronological-gap sweep,
102 pending letters earlier than the -0043-07-28 10.24 marker, down
32 from the start of this session):} the natural next clusters are
(a) the \textit{Ad Brutum} correspondence (18 pending letters in
the cluster, all 43 BC, the most politically substantial remaining
letters in the gap zone --- Cicero's last surviving correspondence,
through November 43); (b) the remaining \textit{Att.} 12 / 13
letters in the post-Tullia mourning period (mid-March 45 BC into
summer 45 BC, the daily-letter regime from Astura); (c) the
remaining 44 BC scattered \textit{Fam.} letters (7.19, 7.24, 7.25,
7.26, 7.28, 7.29, 7.30, 7.31, 7.33; 9.08, 9.14, 9.24; 6.20, 6.22;
4.03, 4.04, 4.12, 4.13, 4.14, 4.15; 15.20).
\item \textbf{Slice F (the four no-Perseus deferred letters):}
\textit{Fam.} 11.8, 11.17, 11.28 (all 43 BC), and the
\textit{Fam.} 5.10 placeholder, plus \textit{Att.} 13.15, 13.18,
13.36 and \textit{Fam.} 9.25 from session 18's placeholder backlog.
Manual sourcing required. Best held as a single-session
batch with Alexander manually supplying the Latin from Shackleton
Bailey / Teubner / OCT.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, one per session not in parallel):}
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} 429+ entity stubs
in \texttt{data/entities.json} remain ripe for an aggressive
parallel apparatus pass.
\item \textbf{\textit{Fam.} 13.9 file rename:} the four files
under the \texttt{005bc-} prefix should be renamed to
\texttt{050bc-} now that the date is corrected to -0050-01-15.
This is a four-file rename (\texttt{latin/} +
\texttt{english/} + \texttt{headnotes/} +
\texttt{data/parallel/letters/}) plus a four-line
\texttt{*\_file:} path update in works.yaml; the sandbox cannot
delete files, so Alexander handles this at handoff or in a
follow-up session.
\end{itemize}


\textbf{Translation state (post-Cowork-session-27):} \textbf{813 /
958 works drafted (\~84.9\%)}. \textbf{Latest drafted by deep
chronology is unchanged} from session 26: \textit{Ad Familiares}
10.24 (Plancus's camp in Gaul, 28 July 43 BC) remains the marker.
Session 27 \textbf{opened and drove the entire \textit{Ad
Familiares} book 12 cluster}, the Cassius / Trebonius / Cornificius
/ Lentulus correspondence covering 46 BC through July 43 BC. All
\textbf{30 letters of book 12 are now drafted} (12.1--12.30, end to
end). The chronological-gap warning falls from \textbf{163}
pending-earlier-than-marker (post-session-26) to \textbf{134}
(post-session-27) --- a clean 29-letter reduction, with the
thirtieth letter (the corrected-date 12.7) re-entering the gap zone
after its meta date was moved from \mbox{-0043-08-04} year-precision
to \mbox{-0043-03-07} day-precision.

\textbf{Cowork session 27 --- 30 letters drafted across two
parallel waves (nine workers total):}

\textbf{Wave 1 (4 workers, 16 letters):}
\begin{itemize}
\item \textbf{Worker A (\textit{Fam.} 12.17, 12.18, 12.19, 12.20, 4
letters --- the early Cornificius cluster 46--44 BC):} 12.17
(Cicero, Rome, mid-Sept 46 BC, to Cornificius --- the opening
``warm-up'' letter of the long Cornificius correspondence,
established now as proconsul-collega); 12.18 (Cicero, Rome, end
Sept / early Oct 46 BC, to Cornificius --- continuation, with the
obiter dictum that ``civil-war victors have to humour their
partisans'' rendered without softening); 12.19 (Cicero, Rome, Dec
46 BC, to Cornificius --- with the \textbf{textual crux} on
\textit{Syriam} where Perseus's transmitted text names Syria as
Cornificius's province, in apparent conflict with historical
attestation that he governed Africa Vetus --- flagged as a
candidate translator-note); 12.20 (Cicero, Rome, 2 September 44 BC,
to Cornificius --- the short note famously dated to the same day
as Cicero's \textit{First Philippic}, with the \textit{†ut es}
obelized crux preserved and Cicero's parenthetical sign-off
\textit{haec scripsi in senatu} ``this I scribbled while in the
Senate''; one Greek word $\dot{\upsilon}\pi o\mu\nu\eta\mu\alpha\tau\iota\sigma\mu\acute{o}\nu$ = ``memorandum'').
\item \textbf{Worker B (\textit{Fam.} 12.1, 12.16, 12.22, 12.2, 4
letters --- the opening Cassius and Trebonius cluster, May--Oct 44
BC):} \textbf{12.1 (Cicero, Pompeian villa, 3 May 44 BC, to Cassius
--- the \textbf{FAMOUS POST-IDES POLITICAL DIAGNOSIS}: \textit{non
regno sed rege liberati videmur} ``we seem to have been liberated
not from the kingship but from the king,'' rendered fresh from the
Latin; the diagnosis Cicero will repeat across the rest of 44 BC
that the Liberators stopped one act too short; with the strong
\textit{tabulae figuntur} ``edicts are posted up'' and the
\textit{chirographa} = Antony's notorious Caesarian \textit{acta})};
\textbf{12.16 (Trebonius, Athens, 25 May 44 BC, to Cicero --- the
last surviving letter to Cicero from Trebonius before his murder
the following January; affectionate tone about young Marcus
Cicero's studies in Athens; \textbf{one Greek word}
$\epsilon\dot{\upsilon}\theta\upsilon\rho\rho\eta\mu o\nu\acute{\epsilon}\sigma\tau\epsilon\rho o\varsigma$
= ``more outspoken''; with the formal \textit{S. v. b.} = \textit{si
vales bene est} opening preserved)}; 12.22 (Cicero, Rome, after 19
September 44 BC, to Cornificius --- \textit{tyrannoctoni}
``tyrant-slayers,'' Cicero's pointed Greek-cum-Latin coinage for
the Liberators, kept in English as the load-bearing political
neologism it is); \textbf{12.2 (Cicero, Rome, between 19 Sept and 5
Oct 44 BC, to Cassius --- the corrosive Antony letter, with the
swap of \textit{nequior}/\textit{nequissimum} where Antony is ``far
more worthless than the very man you called the most worthless
ever killed,'' the structural antithesis preserved in English; the
recurring \textit{homo gladiator} contemptuous epithet rendered
``gladiator'' consistently across this cluster)}.
\item \textbf{Worker C (\textit{Fam.} 12.3, 12.23, 12.21, 12.24, 4
letters --- Oct 44--Jan 43 BC):} 12.3 (Cicero, Rome, 2--6 Oct 44 BC,
to Cassius --- the short follow-up to 12.2, with the
\textit{favente magis quam sperante} ``favouring more than hoping''
landing); 12.23 (Cicero, Rome, c.~9 Oct 44 BC, to Cornificius ---
on Cannutius and the political mood after Antony's open break);
12.21 (Cicero, Rome, uncertain month 44 BC, to Cornificius --- the
shortest letter in the cluster, a one-section commendation;
\textbf{meta-entry flagged}: \texttt{date: -0044-10-18} carries
\texttt{date\_precision: year} which is internally inconsistent
with Perseus's \textit{mense incerto}); 12.24 (Cicero, Rome, 24
Jan 43 BC, to Cornificius --- with the anaphoric tricolon
\textit{hoc est animi, hoc est ingeni tui, hoc eius spei\ldots}
``this is the mark of your spirit, this of your character, this of
the hope\ldots'').
\item \textbf{Worker D (\textit{Fam.} 12.4, 12.5, 12.11, 12.25, 4
letters --- Feb--Mar 43 BC):} 12.4 (Cicero, Rome, c.~1 Feb 43 BC,
to Cassius --- with the dinner-conceit \textit{reliquiae}
``leftovers'' from the Ides-of-March wish-not-quite-fulfilled);
12.5 (Cicero, Rome, c.~5 Feb 43 BC, to Cassius --- with the
\textit{praesidium} ``bulwark'' of Servius Sulpicius's death and
the closing \textit{lumen eluceat} ``the light shines forth''
peroration); \textbf{12.11 (C. Cassius proconsul, in camp at
Tarichea/Taricheae in Galilee, 7 March 43 BC, to Cicero ---
\textbf{textual variant flagged}: the Perseus dateline reads
\textit{in castris Tadolicis} but the body subscription reads
\textit{ex castris taricheis}; ``Tadolicis'' is a manuscript
corruption for ``Taricheis''; preserved both forms with a headnote
note)}; \textbf{12.25 (Cicero, Rome, 19 March 43 BC, to Cornificius
--- a \textbf{MAJOR POLITICAL LETTER}: contains a \textbf{Terence
\textit{Andria} 189 quotation} \textit{hic dies aliam vitam
defert, alios mores postulat} ``this day brings another life,
demands other ways,'' flagged as an allusions-sidecar candidate;
the \textit{Minotauri, id est Calvisi et Tauri} ``the Minotaurs,
that is, Calvisius and Taurus'' pun preserved; the famous
Philippic-grade insult \textit{ructantem et nauseantem} ``belching
and retching'' against Antony rendered literal; the dating to the
Quinquatrus festival noted in the headnote)}.
\end{itemize}

\textbf{Wave 2 (5 workers, 14 letters --- including the two
long-form Lentulus dispatches):}
\begin{itemize}
\item \textbf{Worker E (\textit{Fam.} 12.26, 12.6, 12.27, 12.12, 4
letters --- Mar--May 43 BC):} 12.26 (Cicero, Rome, spring 43 BC, to
Cornificius --- a short recommendation, salutation preserved as
the OCR-quirky \texttt{CICERO COR ni FICIO S.}); \textbf{12.6
(Cicero, Rome, late Mar / early Apr 43 BC, to Cassius ---
\textbf{the disambiguation crux}: the letter mentions ``Brutus''
twice, once meaning M. Brutus (the eastern partner) and once
meaning D. Brutus (the Mutina general); disambiguated in the
headnote)}; 12.27 (Cicero, Rome, spring 43 BC, to Cornificius ---
the \textit{summa severitas summa cum humanitate iungatur} ``the
strictest gravity joined to the highest cultivation'' as a
catalogue of Cornificius's office-character); \textbf{12.12
(\textbf{C. Cassius proconsul, in camp in Syria, 7 May 43 BC, to
Cicero --- the \textbf{MAJOR CASSIUS DISPATCH} reporting on
Cassius's takeover of Dolabella's army; the politically loaded
claim \textit{te hortante et auctore} ``with you to urge me on and
to authorise me'' that Cicero himself sanctioned Cassius's eastern
command --- the legal centre of gravity of the whole letter; the
\textit{proluissa} corruption in §2 is treated as a misreading of
\textit{promissa} ``what I had promised them''; salutation
preserved as the OCR-quirky \texttt{CASSIVS PROCOS. S. D. M.
CICERONI SV0} (SVO for ``suo''))}.
\item \textbf{Worker F (\textit{Fam.} 12.14, 1 long letter):}
\textbf{12.14 (P. Cornelius Lentulus Spinther the younger,
proquaestor, Perga in Asia Minor, 29 May 43 BC, to Cicero --- 8
sections, \textbf{the first of two LENTULUS LONG-FORM DISPATCHES}
on the eastern provinces after Dolabella's murder of Trebonius;
\textbf{one Greek phrase} $\pi\alpha\tau\rho\acute{\iota}\delta\alpha$
$\dot{\epsilon}\mu\dot{\eta}\nu$ $\mu\tilde{\alpha}\lambda\lambda o\nu$
$\varphi\iota\lambda\tilde{\omega}\nu$ = ``loving my country more
[than my own]'' at §7 (a tragic / Homeric commonplace, not a
verbatim citation); \textbf{textual crux} at §3 with an obelized
passage \textit{† nec me meae ullae privatim iniuriae umquam
malus animus eorum \ldots} rendered by sense; flagged); \textbf{the
\textbf{section count was 8, not 12} --- Perseus's TEI carries 8
numbered sections for this letter, contrary to early estimates;
\textbf{meta-date correction}: \texttt{-0043-06-01} day $\rightarrow$
\texttt{-0043-05-29} day, per Perseus \textit{iiii K. Iun.})}.
\item \textbf{Worker G (\textit{Fam.} 12.15, 1 long letter):}
\textbf{12.15 (P. Cornelius Lentulus Spinther the younger,
proquaestor pro praetore, Perga, §§1--6 written 29 May 43 BC, §7
postscript added 2 June 43 BC, to the Senate, consuls, praetors,
tribunes, and Roman People --- the \textbf{FORMAL SENATORIAL
DISPATCH}, the longer of the two Lentulus letters; the long-form
opening salutation \textit{S. v. l. v. v. b. e. v.} = \textit{si
vos liberique vestri valetis, bene est; ego exercitusque valemus}
``if you and your children are well, it is well; I and the army
are well'' rendered in full; \textbf{textual cruxes}: \texttt{Hs
navibus} (§2) with the \texttt{Hs} numeral corruption, and a
daggered clause in §4 \textit{† haec sive timore \ldots noluerunt †}
preserved under daggers in the English; the slogan-language
\textit{concordia ordinum} ``concord of all orders'' and
\textit{singularis civis et ducis} ``that singular citizen and
commander'' (of Cassius); \textbf{meta-date correction}:
\texttt{-0043-06-05} day $\rightarrow$ \texttt{-0043-06-02} day,
per Perseus \textit{iiii Non. Iun. a. 711 (43)} for the postscript
date)}.
\item \textbf{Worker H (\textit{Fam.} 12.28, 12.8, 12.30, 12.13, 4
letters --- Mar--June 43 BC):} \textbf{12.28 (Cicero, Rome, c.~22
March 43 BC, to Cornificius --- \textbf{major meta-date correction}:
\texttt{-0043-05-25} year-precision $\rightarrow$
\texttt{-0043-03-22} day-precision, per Perseus \textit{paulo post
xiii K. April. a. 711 (43)} ``a little after 20 March 43 BC''
--- the meta date was wrong by roughly two months; with the
preserved-as-transmitted \texttt{HS X\_X\_} = HS XX m = 2{,}000{,}000
sesterces and \texttt{HS D\_C\_C\_} = HS DCC m = 700{,}000
sesterces, rendered in English as plain numerals)}; 12.8 (Cicero,
Rome, c.~9 June 43 BC, to Cassius --- short, with the
\textit{scelus \ldots\ levitatem et inconstantiam} tricolon of
Antony's character); \textbf{12.30 (Cicero, Rome, a little after 9
June 43 BC, to Cornificius --- a substantial letter rebuking
Cornificius for stripping his own legates of their lictors, with
the antithesis ``men worthy of honour were not to be compared with
men worthy of disgrace,'' and the \textit{sine tributo} ``without
a special levy'' on the suspended Roman direct tax)}; \textbf{12.13
(C. Cassius Parmensis, Cyprus / Crommyuacris, 13 June 43 BC, to
Cicero --- the \textbf{ATTRIBUTION CRUX} where the salutation
\texttt{C. CASSIVS Q. S. D. M. CICERONI} reveals the sender to be
\textbf{C. Cassius Parmensis} (the future tyrannicide's namesake),
not C. Cassius Longinus; \textit{one Greek word}
$\pi\acute{\alpha}\lambda\tau\omega\iota$ (\textit{paltōi}, dative
of $\pi\acute{\alpha}\lambda\tau o\nu$ ``javelin'') = ``at a
javelin's cast,'' with the \textbf{textual crux} that the Latin
also transmits \textit{a milibus passuum xx} ``20 miles away'' in
the same clause, an internal inconsistency that standard editors
resolve by retaining only the Greek distance --- flagged as a
translator-note candidate)}.
\item \textbf{Worker I (\textit{Fam.} 12.9, 12.10, 12.29, 12.7, 4
letters --- June--Aug 43 BC):} 12.9 (Cicero, Rome, between 16 and
29 June 43 BC, to Cassius --- short, on Cassius's expected 41 BC
consulship); 12.10 (Cicero, Rome, c.~1 July 43 BC, to Cassius ---
the \textit{levitate Lepidi} ``Lepidus's inconstancy'' and the
\textit{sine capite, sine auctore, rumore nuntio} ``without a
definite head, without a named author, only rumour reporting
rumour'' tricolon on the rumour-mill in Rome); 12.29 (Cicero,
Rome, spring 43 BC, to Cornificius --- on Lamia and the
\textit{magno theatro spectata est} ``witnessed by a great
audience'' theatre-metaphor; \textbf{meta-entry flagged}: meta has
\texttt{date: -0043-06-26} with \texttt{date\_precision: year} ---
internally inconsistent and conflicts with Perseus's \textit{vere
a. 711} ``spring 43 BC''); \textbf{12.7 (Cicero, Rome, c.~7 March
43 BC, to Cassius --- \textbf{major meta-date correction}:
\texttt{-0043-08-04} year-precision $\rightarrow$
\texttt{-0043-03-07} day-precision, per Perseus \textit{circ. Non.
Mart. a. 711 (43)} ``c.~7 March 43 BC'' --- the meta date was
wrong by roughly five months; with the spatial figure \textit{tanta
contentione quantum forum est} ``with such intensity as the Forum
is wide,'' preserved literally)}.
\end{itemize}

\textbf{Metadata corrections committed to \texttt{meta/works.yaml}
during session 27 (4 date corrections):}
\begin{itemize}
\item \textit{Fam.} 12.7: \texttt{date} \mbox{-0043-08-04}
year-precision $\rightarrow$ \mbox{-0043-03-07} day-precision, per
Perseus \textit{circ. Non. Mart. a. 711 (43)}. The meta was wrong
by roughly five months.
\item \textit{Fam.} 12.14: \texttt{date} \mbox{-0043-06-01}
day-precision $\rightarrow$ \mbox{-0043-05-29} day-precision, per
Perseus \textit{iiii K. Iun. a. 711 (43)} = 29 May 43 BC. The meta
was 3 days late.
\item \textit{Fam.} 12.15: \texttt{date} \mbox{-0043-06-05}
day-precision $\rightarrow$ \mbox{-0043-06-02} day-precision, per
Perseus \textit{iiii Non. Iun. a. 711 (43)} = 2 June 43 BC for the
postscript date of completion. The meta was 3 days late.
\item \textit{Fam.} 12.28: \texttt{date} \mbox{-0043-05-25}
year-precision $\rightarrow$ \mbox{-0043-03-22} day-precision, per
Perseus \textit{paulo post xiii K. April. a. 711 (43)} ``a little
after 20 March 43 BC.'' The meta was wrong by roughly two months.
\end{itemize}

\textbf{Metadata candidates flagged but \textit{not} corrected
this session (left for next Cowork PM or Alexander):}
\begin{itemize}
\item \textit{Fam.} 12.21: \texttt{date: -0044-10-18} carries
\texttt{date\_precision: year} which is internally inconsistent
(a day-precision date with a year-precision flag) and conflicts
with Perseus's \textit{mense incerto a. 710 (44)}. Recommend
normalising the \texttt{date:} to a year-marker like
\texttt{-0044-01-01} or sharpening the precision flag.
\item \textit{Fam.} 12.29: \texttt{date: -0043-06-26} carries
\texttt{date\_precision: year} which is similarly internally
inconsistent and conflicts with Perseus's \textit{vere a. 711}
``spring 43 BC.'' Recommend normalising the \texttt{date:} to
something like \texttt{-0043-04-01} with
\texttt{date\_precision: season} (or year-marker).
\item \textit{Fam.} 12.22: meta \texttt{date: -0044-09-19}
day-precision; Perseus dateline is \textit{post xiii K. Oct. a. 710
(44)} ``after 19 September'' --- a range whose lower bound is
19 Sept. The day-precision \texttt{19 Sept} treats the lower bound
as exact; defensible but not the dateline's claim.
\item \textit{Fam.} 12.2: similar range-endpoint issue; meta has
\texttt{-0044-10-05} day-precision but Perseus is the range
\textit{inter xiii K. et iii Non. Oct. a. 710 (44)} = 19 Sept to 5
Oct. The day-precision pin to the upper bound is defensible but
not the dateline's claim.
\item \textit{Fam.} 12.11: \texttt{location\_written: in castris
Tadolicis} is a manuscript-corruption form of the body's
\texttt{ex castris taricheis} (Tarichea/Taricheae in Galilee).
Recommend normalising to the correct toponym; the file name and
content do not need to change.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Fam.} 12.1 \textit{non regno sed rege
liberati videmur} formulation.} ``We seem to have been liberated
not from the kingship but from the king.'' The diagnostic sentence
of the Cassius correspondence; rendered fresh from the Latin, with
the \textit{regno/rege} antithesis preserved as
\textit{kingship/king} rather than (e.g.) \textit{rule/ruler},
which loses the etymological weight.
\item \textbf{The \textit{Fam.} 12.1 catalogue of Antony's
overreach.} \textit{tabulae figuntur, immunitates dantur, pecuniae
maximae discribuntur, exsules reducuntur, senatus consulta falsa
deferuntur} ``edicts are posted up, exemptions are granted, vast
sums of money are assigned, exiles are recalled, forged senatorial
decrees are produced'' --- the five-element asyndeton kept intact
in English; the Caesarian \textit{acta} apparatus that justified
everything Antony did in the months after the Ides.
\item \textbf{The \textit{Fam.} 12.2 \textit{nequior /
nequissimum} swap.} ``Far more worthless than the very man you
called the most worthless ever killed.'' The comparative/superlative
hinge is the load-bearing structural figure; preserved across the
English clause in spite of needing two ``worthless'' words.
\item \textbf{The corpus-wide \textit{tyrannoctoni} convention.}
Cicero's pointed Greek-cum-Latin coinage for the Liberators
(\textit{Fam.} 12.22 §1) rendered ``tyrant-slayers'' across the
late-44 / early-43 Cassius correspondence; not domesticated to
``assassins'' or expanded into ``the tyrannicides of the Ides of
March,'' since the precise neologism is the political claim.
\item \textbf{The \textit{Fam.} 12.12 \textit{te hortante et
auctore} claim.} ``With you to urge me on and to authorise me''
--- Cassius's politically loaded claim in his own dispatch that
Cicero authorised his eastern command. The \textit{auctor} verb
matters because it has the technical political-legal weight of
``sanctioning'' a command (\textit{auctoritas senatus}), not
merely ``urging.'' Worth a sustained note.
\item \textbf{The \textit{Fam.} 12.13 attribution.} The salutation
\texttt{C. CASSIVS Q. S. D. M. CICERONI} reveals the sender to be
\textbf{C. Cassius Parmensis} (the future tyrannicide's namesake,
the same Cassius Parmensis whom Octavian would have killed at
Athens in 30 BC), not C. Cassius Longinus. ``Cassius noster'' in
the body of 12.13 refers to Longinus. Worth a sustained note ---
the corpus's only surviving letter from Cassius Parmensis.
\item \textbf{The \textit{Fam.} 12.13 \textit{paltōi} crux.} ``At
a javelin's cast away.'' Editors split: some (Shackleton Bailey)
read $\pi\acute{\alpha}\lambda\tau\omega\iota$ as a corrupt
place-name \textit{Paltus}; the Greek-distance reading is the
older editorial tradition. The transmitted Latin also carries
\textit{a milibus passuum xx} ``20 miles away'' in the same
clause; the two distances are internally inconsistent and
mainstream editions retain only the Greek. The English follows
the editorial solution.
\item \textbf{The \textit{Fam.} 12.14 §7 \textit{patrida emēn
mallon philōn} Greek phrase.} ``Loving my country more [than my
own].'' A tragic / Homeric commonplace, not a verbatim citation
of any known author; the Greek phrase signals a literary register
that Lentulus the younger consciously deploys in this otherwise
plain-prose dispatch.
\item \textbf{The \textit{Fam.} 12.15 \textit{S. v. l. v. v. b. e.
v.} long-form senatorial salutation.} \textit{Si vos liberique
vestri valetis, bene est; ego exercitusque valemus} = ``If you
and your children are well, it is well; I and the army are well''
--- the formal address from a provincial commander to the Senate
and Roman People, abbreviated in the MSS but rendered in full in
the English per STYLE.md's policy on epistolary openings.
\item \textbf{The \textit{Fam.} 12.19 \textit{Syria} crux.} The
Perseus text explicitly states Caesar assigned \textit{Syria} to
Cornificius (\textit{Syriamque provinciam tibi tributam}), but
the historical record is that Cornificius governed Africa Vetus.
Some editors retain the MS reading (taking it as a slip in Cicero
or in transmission); others emend. The English preserves the
transmitted reading; flagged.
\item \textbf{The \textit{Fam.} 12.25 Terence \textit{Andria} 189
quotation.} \textit{hic dies aliam vitam defert, alios mores
postulat} ``this day brings another life, demands other ways.''
A quotation flagged as an allusions-sidecar candidate; the
\textit{Andria} reference is the only verbatim Terence citation
encountered in this batch of letters.
\item \textbf{The corpus-wide \textit{homo gladiator} epithet for
Antony.} Across \textit{Fam.} 12.22 and 12.2 (and the wider 44--43
BC Cassius correspondence), \textit{gladiator} is rendered
\textit{gladiator} (not ``thug,'' ``ruffian,'' ``cutthroat''),
since the recurring image is the point --- the contemptuous
working-class slur on a Roman aristocrat, a slur Cicero deploys
repeatedly through the Philippics.
\item \textbf{The Tarichea/Taricheae toponym crux in \textit{Fam.}
12.11.} Perseus's dateline reads \textit{in castris Tadolicis}
(MS corruption); the body subscription reads \textit{ex castris
taricheis} (the correct toponym, in Galilee). The MS form
``Tadolicis'' is preserved in the English headnote alongside the
standard form ``Tarichea.''
\end{itemize}

\textbf{Suggested next translation batch} (when session 27 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 27:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice V continuation: \textit{Fam.} 13 (commendations
book).} Book 12 is now wholly closed (all 30 letters drafted).
\textit{Fam.} 13 (the long commendations book) is the next major
sub-sequence inside the gap zone, with 79 letters of which most
remain pending; many are short formal letters of recommendation
and are extremely parallel-dispatchable (3--5 per worker, similar
to the Cornificius cluster). One caveat: \textit{Fam.} 13.49
already has the placeholder stub from session 18 awaiting manual
Latin sourcing.
\item \textbf{Slice S' (the chronological-gap sweep, 134 pending
letters earlier than the -0043-07-28 10.24 marker, down 29 from
the start of this session):} substantial backlog remains in
\textit{Att.} 13 (the death-of-Tullia cluster), the \textit{Fam.}
5 sub-cluster (5.15--5.18 plus 5.10a/5.10b), the \textit{Ad Brutum}
correspondence, the four broken-source \textit{Ad M.~Brutum}
letters (1.16, 2.6, 2.7, 2.8), and the three \textit{Fam.} 11
deferred letters (11.8, 11.17, 11.28) needing manual sourcing.
\item \textbf{Slice F (the three \textit{Fam.} 11 deferred
letters):} 11.8, 11.17, 11.28. Manual sourcing required.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, one per session not in parallel):}
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} 429 entity stubs
in \texttt{data/entities.json} remain ripe for an aggressive
parallel apparatus pass.
\end{itemize}


\textbf{Translation state (post-Cowork-session-26):} \textbf{783 /
958 works drafted (\~81.7\%)}. \textbf{Latest drafted by deep
chronology is unchanged} from session 25: \textit{Ad Familiares}
10.24 (Plancus's camp in Gaul, 28 July 43 BC) remains the marker,
because every one of the 26 letters drafted this session
(\textit{Fam.} 11.1--11.7, 11.9--11.16, 11.18--11.27, 11.29) is
dated on or before 15 July 43 BC. Session 26 \textbf{opened and
drove the \textit{Ad Familiares} book 11 cluster}, the Decimus
Brutus / Mutina-campaign correspondence plus the appendix to book
11 (the famous \textit{Fam.} 11.27 Cicero-to-Matius letter and the
short \textit{Fam.} 11.29 to Oppius). The chronological-gap
warning falls from \textbf{189} pending-earlier-than-marker
(post-session-25) to \textbf{163} (post-session-26) --- a clean
26-letter reduction, the session's full output landing inside the
gap.

\textbf{Cowork session 26 --- 26 letters drafted across two
parallel waves (seven workers total):}

\textbf{Wave 1 (4 workers, 16 letters --- the opening \textit{Fam.}
11 cluster, Mar 44 BC -- mid-May 43 BC):}
\begin{itemize}
\item \textbf{Worker A (\textit{Fam.} 11.1, 11.2, 11.29, 11.3, 4
letters):} 11.1 (D. Brutus, Rome, 16 March 44 BC --- the day after
the Ides, post-Hirtius meeting; the despondent strategy letter to
M. Brutus and Cassius proposing a \textit{legatio libera} out of
Italy, with \textit{novissima auxilia} ``the last resorts''); 11.2
(Brutus and Cassius as praetors, Lanuvium, end of May 44 BC, to
consul Antony --- the short public protest letter about
\textit{de reponenda ara}, the makeshift altar to \textit{divus
Iulius} that Dolabella had torn down); \textbf{11.29 (Cicero,
Tusculan villa, c.~end June / early July 44 BC, to C. Oppius ---
the firm short letter on Cicero's withdrawal from Caesarian
\textit{officia}, with the strong landing \textit{ipse me hominem
non putabo} ``I shall not count myself a human being'' and the
\textit{consulere dignitati meae} formulation); \textbf{meta-date
corrected -0044-07-15 day $\rightarrow$ -0044-07-01 month}, per
Perseus \textit{vel ex. m. Iun. vel in. Quint. a. 710 (44)}, a
range across two months incompatible with day-precision)};
\textbf{11.3 (Brutus and Cassius as praetors, Naples, 4 August 44
BC, to consul Antony --- the famous indignant reply to Antony's
edict; the load-bearing antithesis \textit{neque quam diu vixerit
Caesar sed quam non diu regnarit fac cogites} ``do not contemplate
how long Caesar lived, but how short a time he reigned''; opening
with the formal \textit{S. v. b.} = \textit{si vales, bene est}
preserved in the salutation; closing \textit{Pr. non. Sext.}
preserved in the Roman-calendar dating-formula)}.
\item \textbf{Worker B (\textit{Fam.} 11.27, 11.4, 11.5, 11.6, 4
letters):} \textbf{11.27 (M. Cicero to C. Matius, Tusculan villa,
30 August 44 BC, $\sim$1090-word \textbf{MAJOR PHILOSOPHICAL
LETTER} --- the corpus's single best treatment of friendship under
tyranny; Cicero defends his long \textit{amicitia} with Matius
while still defending his hostility to Caesar; the architectural
\textit{vetustas habet aliquid commune cum multis, amor non habet}
``long standing has something in common with many; affection does
not''; the catalogue of virtues \textit{gravitas, constantia
\ldots\ lepos, humanitas, litterae}; the conditional admission
\textit{si Caesar rex fuerit} ``if Caesar was a king'' followed by
the parenthetical \textit{quod mihi quidem videtur} ``which to me
at least he seems to have been''; the philosophical kernel
\textit{libertatem patriae vitae amici anteponendam} ``the liberty
of one's country is to be set above the life of a friend''; \textbf{one
Greek phrase} $\varphi\iota\lambda\sigma\sigma\omicron\varphi\omicron\acute{\upsilon}\mu\epsilon\nu\alpha$
(\textit{philosophoumena}, ``these works of philosophy'') at §5)};
11.4 (D. Brutus IMP. CONS. DESIG., Cisalpine Gaul, mid-October
$\sim$end-November 44 BC, to Cicero --- short report from the
province, with \textit{nomen imperatorium captans} ``chasing the
title of imperator''); 11.5 (Cicero, Rome, 9 December 44 BC, to D.
Brutus --- the active correspondence opens; \textit{iste} for
Antony rendered ``that man,'' \textit{dominatu regio} ``a king's
domination''); 11.6 (Cicero, Rome, 20 December 44 BC, to D. Brutus
--- on the senate session and the consul-elect plans, with the
strong religious \textit{nefas esse duxi} ``I judged it impious''
and the Philippic-period hyperbolic \textit{divinis in rem p.
meritis} ``divine services to the state'').
\item \textbf{Worker C (\textit{Fam.} 11.7, 11.9, 11.10, 11.11, 4
letters):} \textbf{11.7 (Cicero, Rome, year-precision in meta but
\textbf{Perseus dateline corrupt} (\textit{xiii K. bu a. 710
(44)}); content (Martian and Fourth legions already declared
Antony a public enemy) places this in late December 44 or early
January 43; standard editorial reading is \textit{xiii K. Jan.} =
20 December 44 BC; flagged as a meta candidate for redate but
\textbf{left at -0044 year-precision} this session pending human
review of the Perseus reading)}; 11.9 (D. Brutus, in camp at
Regium Lepidi, 29 April 43 BC, to Cicero --- short dispatch with
the famous \textit{hominem ventosissimum} of Lepidus, rendered
``that most weathercock of men''); \textbf{11.10 (D. Brutus, in
camp at Dertona, 5 May 43 BC, to Cicero --- longer dispatch with
\textbf{textual cruxes flagged}: §1 obelized passage \textit{†sit
an hoc temporis videatur dici causat,} rendered minimally and
flagged in sidecar \texttt{notes}; §5 manuscript figure \textit{HS
mihi fuit pecuniae cccc amplius} (400{,}000 sesterces, implausibly
small for a man of Decimus's standing; Shackleton Bailey emends to
HS|XL| = 40 million); transmitted figure translated as-is, flagged
in sidecar \texttt{notes})}; 11.11 (D. Brutus, in camp on the
Statiellan border, 6 May 43 BC, to Cicero --- the day-after
follow-up, with the salutation preserving the as-transmitted
\texttt{IMR COS. DES.} OCR corruption for \texttt{IMP. COS. DES.}).
\item \textbf{Worker D (\textit{Fam.} 11.13, 11.12, 11.19, 11.20,
4 letters):} 11.13 (D. Brutus, in camp at Pollentia, 12 May 43 BC,
to Cicero --- with the rare technical detail \textit{ergastula
solvit} ``broke open the slave-barracks''); 11.12 (Cicero, Rome,
13 May 43 BC, to D. Brutus --- the political future-perfect
\textit{is bellum confecerit, qui Antonium oppresserit} ``he will
have finished the war who crushes Antonius''); 11.19 (D. Brutus,
Vercellae, 21 May 43 BC, to Cicero --- the Vicetia
\textit{vernarum causa} case, with \textit{verna} as a technical
term for ``home-born slave''); \textbf{11.20 (D. Brutus, Eporedia,
24 May 43 BC, to Cicero --- THE \textbf{FAMOUS OCTAVIAN-QUOTATION
LETTER}: \textit{laudandum adulescentem, ornandum, tollendum}
``the young man must be praised, decorated, and lifted up,'' with
the deliberate \textit{tollendum} pun (= ``raise'' / ``remove'')
preserved in English through Brutus's gloss \textit{se non esse
commissurum ut tolli possit} ``he would not allow it to come about
that he be lifted out of the way''; quoted with the same triple
gerundive by Velleius Paterculus 2.62.6; a corpus-level testimonium
candidate)}.
\end{itemize}

\textbf{Wave 2 (3 workers, 10 letters --- the closing \textit{Fam.}
11 cluster, late May -- mid-July 43 BC):}
\begin{itemize}
\item \textbf{Worker E (\textit{Fam.} 11.23, 11.14, 11.18, 11.26,
4 letters):} 11.23 (D. Brutus, Eporedia, 25 May 43 BC, to Cicero
--- with the horsemanship idiom \textit{si frenum momorderis} ``if
you take the bit between your teeth''); \textbf{11.14 (Cicero,
Rome, 29 May 43 BC, to D. Brutus --- \textbf{two Greek phrases}:
$\check{o}\varrho\gamma\alpha\nu\omicron\nu$ (\textit{organon},
``instrument'', fully naturalised in English) and
$\sigma\kappa\iota\alpha\mu\alpha\chi\acute{\iota}\alpha\iota$
(\textit{skiamachiai}, ``shadow-boxing'', rendered with Greek
marginalia per STYLE.md); flagged for the corpus-wide Greek
catalogue. Perseus marks a textual corruption with daggers around
\textit{ut omnium animi relaxati sint, meaeque illae vehementes
contentiones tamquam skiamaxi/ai esse videantur}, flagged inline
as \texttt{[the text is corrupt here]} and noted in sidecar)};
\textbf{11.18 (Cicero, Rome, 1 June 43 BC, to D. Brutus --- the
desperate-phase opener after Lepidus's 30 May defection;
\textbf{Perseus dateline transmitted in corrupt form \textit{x iiii
K. Iun.}} (literally 19 May, impossible for the contents);
standard editorial reading is \textit{prid. K. Iun.} = 31 May / 1
June 43 BC; meta -0043-06-01 day-precision retained per the
Shackleton Bailey reading; corruption noted in headnote and
sidecar; with the optatistic-superlative \textit{optatissima
pace} ``the most longed-for peace'')}; 11.26 (D. Brutus, in camp
on the march to Cularo (modern Grenoble), 3 June 43 BC, to Cicero
--- on the distinction between \textit{mihi stipendium dent an
decernant} ``grant me pay or only decree it'').
\item \textbf{Worker F (\textit{Fam.} 11.21, 11.24, 11.25, 3
letters):} \textbf{11.21 (Cicero, Rome, 4 June 43 BC, to D. Brutus
--- substantial reply on the senate aftermath of Lepidus's
defection; the Segulius \textit{revolutionaries-and-feasters}
extended metaphor \textit{ligurrirent} ``were nibbling after''
preserving the kitchen-image extension)}; \textbf{11.24 (Cicero,
Rome, 6 June 43 BC, to D. Brutus --- short reply with the
political watchman-metaphor \textit{vigiliam meam tibi tradere}
``hand over my watch to you'' preserving the guard-register
under Brutus's coming consulship; Cicero quotes Brutus's own
proverb \textit{frenum momordi} ``I have champed the bit'' back at
him)}; \textbf{11.25 (Cicero, Rome, 18 June 43 BC, to D. Brutus
--- \textbf{one Greek phrase} $\lambda\alpha\kappa\omega\nu\iota\sigma\mu\acute{o}\nu$
(\textit{lakonismon}, ``Laconic brevity'', accusative); the
diagnostic phrase \textit{intestinum urbis malum} ``that inward
evil of the city'' for the unnamed Octavian-manoeuvre referent)}.
\item \textbf{Worker G (\textit{Fam.} 11.15, 11.22, 11.16, 3
letters):} 11.15 (Cicero, Rome, 29 June 43 BC, to D. Brutus ---
the playful close \textit{magistro brevitatis} ``master in
brevity''); 11.22 (Cicero, Rome, c.~14 July 43 BC, to D. Brutus
--- the short recommendation for Appius Claudius, with the
delicate hedge \textit{etsi minus veram causam habebis, tamen vel
probabilem aliquam poteris inducere} ``even if you find your hand
short of a wholly true ground, still you will be able to bring
forward one at least that has the look of truth''); \textbf{11.16
(Cicero, Rome, 15 July 43 BC, to D. Brutus --- the recommendation
for L. Lamia, with the bold \textit{equitum centurias tenes, in
quis regnas} ``the centuries of the knights are in your hand ---
you are king there''; one of the latest surviving letters in the
D. Brutus correspondence, mid-July 43 BC; Perseus dateline is
unusually broad \textit{inter ex. m. Apr. et in. Quint.} (end of
April to early July) but content and ordering support the meta
date)}.
\end{itemize}

\textbf{Letters deferred for manual sourcing or future review:}
\begin{itemize}
\item \textbf{\textit{Fam.} 11.8 and 11.17:} both carry
\textit{only} a \texttt{latinlibrary.com} URL in \texttt{works.yaml}
(no Perseus TEI). Skipped for this session; need manual sourcing
from Teubner / Loeb / OCT.
\item \textbf{\textit{Fam.} 11.28:} this is Matius's famous reply
to 11.27 (the second half of the famous Cicero-Matius exchange).
Perseus produced suspiciously short output (107 chars) suggesting
the letter is not present in the TEI under \texttt{n="28"} (a
likely TEI-numbering anomaly similar to \textit{Fam.} 13.49); the
Latin Library fallback returned the whole \textit{Fam.} 11 book
file ($\sim$46k chars) rather than the single letter. The Latin
file at \texttt{latin/letters/043bc-ad-familiares-11-28.tex} has
been overwritten with a \texttt{\% PLACEHOLDER} stub explaining
the issue. The entry remains pending. \textbf{The 11.27/11.28 pair
is one of the most famous in the corpus}; restoring 11.28 should
be a near-term priority.
\end{itemize}

\textbf{Metadata corrections committed to \texttt{meta/works.yaml}
during session 26 (2 date corrections):}
\begin{itemize}
\item \textit{Fam.} 11.2: \texttt{date} \mbox{-0044-05-15}
month-precision $\rightarrow$ \mbox{-0044-05-31} month-precision,
per Perseus \textit{Scr. Lanuvi ex. m. Mai. a. 710 (44)} = ``end
of May 44 BC.'' The 15 May placeholder was the year-precision
default; the Perseus dateline sharpens to the end of the month.
\item \textit{Fam.} 11.29: \texttt{date} \mbox{-0044-07-15}
day-precision $\rightarrow$ \mbox{-0044-07-01} month-precision,
per Perseus \textit{Scr. vel ex. m. Iun. vel in. Quint. a. 710
(44)} = ``end of June or early July 44 BC,'' a range across two
months that is explicitly incompatible with day-precision.
\end{itemize}

\textbf{Metadata candidates flagged but \textit{not} corrected
this session (left for next Cowork PM or Alexander):}
\begin{itemize}
\item \textit{Fam.} 11.7: \texttt{date} \mbox{-0044-04-16}
year-precision is almost certainly wrong on the month. Perseus
dateline is corrupt in transmission (\textit{xiii K. bu a. 710 (44)}
--- the month-abbreviation is unreadable). Standard editorial
reading (Shackleton Bailey) is \textit{xiii K. Jan.} = 20 December
44 BC, supported by the letter's contents (Martian and Fourth
legions already declared Antony a public enemy in November 44).
Recommend updating to \mbox{-0044-12-20} day-precision when the
Perseus reading is human-verified.
\item \textit{Fam.} 11.15: \texttt{date} \mbox{-0043-06-29}
day-precision; Perseus gives a range \textit{inter viii et iii K.
Quint. a. 711 (43)} = 24--29 June, technically incompatible with
day-precision but the meta sits at the late end of the range; not
worth correcting unless a strict-validator convention is
preferred.
\item \textit{Fam.} 11.16: \texttt{date} \mbox{-0043-07-15}
day-precision; Perseus gives an unusually broad range \textit{inter
ex. m. Apr. et in. Quint. a. 711 (43)} = end of April to early
July. Content and ordering support a July 43 BC placement;
day-precision is generous; not worth correcting at this stage.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Fam.} 11.27 \textit{vetustas / amor}
opening axiom (§2).} ``Long standing has something in common with
many; affection does not.'' The architectural antithesis on which
the entire Cicero-Matius letter turns; \textit{amor} is
companionate-political here, not erotic, and the cognate weight in
``affection'' (rather than ``love'') lets the Latin breathe. Worth
a sustained note.
\item \textbf{The \textit{Fam.} 11.27 catalogue of virtues (§6).}
\textit{gravitas, constantia \ldots\ lepos, humanitas, litterae}
rendered ``judgement, weight, constancy \ldots\ charm, humanity,
learning.'' The \textit{gravitas} as ``weight'' (rather than the
flatter ``seriousness'' or ``dignity'') preserves the Latin's
physical-metaphor charge; the catalogue is one of the most
compressed Ciceronian taxonomies of personal virtue in the corpus.
\item \textbf{The \textit{Fam.} 11.27 \textit{si Caesar rex
fuerit} concession (§8).} The conditional-with-future-perfect is
committal; the parenthetical \textit{quod mihi quidem videtur}
makes Cicero's actual view unmistakable. Rendered ``if Caesar was
a king (which to me at least he seems to have been)'' to land that
admission.
\item \textbf{The \textit{Fam.} 11.27 philosophical kernel (§8).}
\textit{libertatem patriae vitae amici anteponendam} ``the liberty
of one's country is to be set above the life of a friend.'' The
Stoic-Republican axiom on which the letter rests; cognate-weighty
on every term.
\item \textbf{The \textit{Fam.} 11.20 \textit{laudandum,
ornandum, tollendum} testimonium.} The famous triple gerundive,
preserved in English through Brutus's gloss to maintain the
\textit{tollere} pun (= ``raise'' / ``remove''). Velleius Paterculus
2.62.6 quotes it with the same wording; allusion-sidecar candidate
and a corpus-level note in its own right.
\item \textbf{The corpus-wide \textit{iste} convention.} Across the
late-44 / early-43 letters to D. Brutus (11.5 §2 in particular),
\textit{iste} for Antony carries a stable contemptuous third-person
charge approximated in English by ``that man.'' Worth a single
sustained note covering the entire correspondence rather than
flagging at each instance.
\item \textbf{The corpus-wide \textit{dignitas} convention.}
Rendered consistently as ``standing'' across this session
(\textit{Fam.} 11.4 §1, 11.5 §3, 11.6 §1, 11.27 §7, 11.29 §1).
Worth a single sustained note.
\item \textbf{The \textit{Fam.} 11.3 \textit{neque quam diu vixerit
Caesar sed quam non diu regnarit} antithesis.} Resisted the more
famous English shapes (Shuckburgh, Shackleton Bailey) and rendered
fresh from the Latin: ``do not contemplate how long Caesar lived,
but how short a time he reigned.''
\item \textbf{The \textit{Fam.} 11.10 §5 manuscript figure
\textit{HS \ldots\ cccc}.} 400{,}000 sesterces, implausibly small
for a man of Decimus's standing; Shackleton Bailey emends to HS|XL|
= 40 million. Transmitted figure translated as-is, flagged in
sidecar \texttt{notes}.
\item \textbf{The \textit{Fam.} 11.10 §1 obelized passage
\textit{†sit an hoc temporis videatur dici causat,}.} Perseus
marks the syntax as broken with daggers; the rendering supplies
the general sense (``though whether this is even a fit moment to
be saying so, I leave aside'') without conjecture, flagged in
sidecar.
\item \textbf{The \textit{Fam.} 11.11 \texttt{IMR COS. DES.} OCR
corruption} in the salutation, preserved as-transmitted in the
\texttt{\textbackslash ciceroLetterOpener} per fetch convention.
Same family as the \textit{Fam.} 10.34 \texttt{PONL MAX.}
corruption noted in session 25.
\end{itemize}

\textbf{Suggested next translation batch} (when session 26 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 26:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice V opening: \textit{Fam.} 12 to Cassius.} Book
11 is now substantively closed (24 of 29 letters drafted; 11.8,
11.17, 11.28 deferred for manual sourcing). The next active
sub-sequence is \textit{Fam.} 12, the Cassius correspondence (and
the related Cornificius-in-Africa cluster also archived in book
12), covering early 43 BC through to Cassius's eastern campaign.
Parallel-dispatchable at 3--4 per worker, similar to the Plancus
and D. Brutus correspondences. \textit{Fam.} 12.1 is the
chronologically next pending letter inside the gap zone.
\item \textbf{Slice S' (the chronological-gap sweep, 163 pending
letters earlier than the -0043-07-28 10.24 marker, down 26 from
the start of this session):} substantial backlog remains --- the
\textit{Att.} 13.36 metadata followup, the two pending
\textit{Att.} 13.15 / 13.18 placeholder stubs awaiting manual
Latin from session 18, the remaining \textit{Fam.} 5 sub-cluster
(5.15--5.18, all 45 BC, parallel-dispatchable), the \textit{Fam.}
5.10a/5.10b split work flagged in session 20, the \textit{Ad
Brutum} correspondence, plus the four Ad M.~Brutum letters with
broken sources (1.16, 2.6, 2.7, 2.8) flagged by the
post-session-23 infrastructure pass.
\item \textbf{Slice F (the three \textit{Fam.} 11 deferred
letters):} 11.8, 11.17, 11.28. Need manual sourcing
(Teubner / Loeb / OCT) since Perseus TEI does not carry them
correctly. The 11.27/11.28 Cicero-Matius pair is the highest
priority of the three --- a high-canon literary loss without 11.28.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} 429 entity stubs
in \texttt{data/entities.json} remain after the session-23-followup
43-stub pilot --- ripe for an aggressive parallel apparatus pass.
\end{itemize}


\textbf{Translation state (post-Cowork-session-25):} \textbf{757 /
958 works drafted (\~79.0\%)}. \textbf{Latest drafted by deep
chronology is unchanged} from session 24: \textit{Ad Familiares}
10.24 (Plancus's camp, 28 July 43 BC) remains the marker, because
all eleven letters drafted this session (\textit{Fam.}
10.25--10.35) fall \emph{earlier} than that marker. Session 25
\textbf{closed book 10 of the \textit{Ad Familiares}}: every letter
in the canonical Plancus / Pollio / Lepidus / Galba book-10 cluster
is now drafted. The chronological-gap warning falls from
\textbf{200} pending-earlier-than-marker (post-session-24) to
\textbf{189} (post-session-25) --- a clean 11-letter reduction, the
session's full output landing inside the gap.

\textbf{Cowork session 25 --- 11 letters drafted in one parallel
wave (four workers):}
\begin{itemize}
\item \textbf{Worker A (\textit{Fam.} 10.25--10.27, 3 letters):}
10.25 (Cicero, Rome, 26 May 43 BC, to Furnius --- pushing Plancus's
legatus to keep Plancus active; the \textit{quasi legitimi temporis}
hedge on the Sullan biennium between aedileship and praetorship);
10.26 (Cicero, Rome, late June 43 BC, to C. Furnius --- the
post-supplicationes ``cheapest and most common'' praetorship complaint
\textit{magistratus levissimi et divulgatissimi} and the closing pun
\textit{vince igitur et vale} ``win, then, and farewell''); 10.27
(Cicero, Rome, 20 March 43 BC evening, to Lepidus --- the chilly
formal letter to Lepidus months before defection, with the
\textit{impotentissimi dominatus} ``utterly intolerable despotism''
and the famous \textit{mortem servituti anteponant} ``set death
before servitude'' formulation).
\item \textbf{Worker B (\textit{Fam.} 10.28--10.31, 4 letters):}
\textbf{10.28 (Cicero, Rome, ca.~2 February 43 BC, to Trebonius ---
the famous \textit{quam vellem ad illas pulcherrimas epulas me
Idibus Martiis invitasses!}\ ``how I wish you had invited me to
that most beautiful banquet on the Ides of March'' opening; the
banquet metaphor sustained through \textit{reliquiarum nihil
haberemus} ``there would be no leftovers''; Cicero's most explicit
retroactive regret at being excluded from the assassination plot)};
10.29 (Cicero, Rome, 6 July 43 BC, to ``Appius'' --- very short
letter of recommendation, recipient probably Appius Claudius Pulcher);
\textbf{10.30 (Galba to Cicero, in camp at Mutina, 15 April 43 BC ---
the major first-person dispatch on the battle of Forum Gallorum
fought 14 April; rare military-Latin register, blow-by-blow account
with cohorts, legions, the \textit{evocati} ``re-enrolled veterans,''
and the Caesarian/Octavian praetorian cohort; a corpus-level witness
to a Roman battle by an eyewitness participant)}; \textbf{10.31
(Pollio to Cicero, Corduba, 16 March 43 BC --- Pollio's first
surviving letter to Cicero from Spain, on his political balancing
act, his refusal to march without senatorial order, with the
characteristically dense Pollionian period in \S2 and the technical
\textit{vindicare in libertatem} ``vindicate into liberty'')}.
\item \textbf{Worker C (\textit{Fam.} 10.32--10.33, 2 letters,
both Pollio from Corduba):} \textbf{10.32 (Pollio, Corduba, 8 June
43 BC --- the famous \textit{Balbus minor} exposé, the longest
Pollio letter in the collection, cataloguing Quaestor Balbus's
outrages in Spain: forced gladiatorial spectacles, Roman citizens
\textit{defodit in ludo et vivum combussit} ``buried in the arena
and burnt alive,'' the Itucca speech delivered in both Latin and
Greek as if Balbus were a Diadoch king, the \textit{quattuorviratum
sibi prorogavit} self-extended four-year magistracy, the
\textit{`C. R. natus sum'} Verrine-echo abbreviation of
\textit{civis Romanus natus sum}; Pollio's prose at its most
caustic and accumulative)}; \textbf{10.33 (Pollio, Corduba, late
May / early June 43 BC --- Pollio's reflective piece on his
position, with the daggered crux \textit{† Hirtino is autem
proelio} preserved as ``in the Hirtian battle,'' the famous
formulation \textit{neque desse neque superesse rei p. volo}
``I wish neither to fail the commonwealth nor to outlive it,'' and
the standard epistolary abbreviation \textit{S. v. h. e. e. q. v.}\
expanded in the body; \textbf{meta-date corrected -0043-06-13 day
$\rightarrow$ -0043-06-01 month-precision} per Perseus
\textit{vel ex. m. Maio vel in. Iun.}\ which is incompatible with
day-precision)}.
\item \textbf{Worker D (\textit{Fam.} 10.34--10.35, 2 letters,
both Lepidus from camp at Pons Argenteus):} 10.34 (Lepidus to
Cicero, in camp at the Pons Argenteus, 18 May 43 BC --- the short
private letter in the days before defection, still deploying the
official titles \texttt{IMP. ITER. PONT. MAX.}\ (Perseus transmits
the corrupt reading \texttt{PONL MAX.}, preserved as-transmitted
in the salutation per fetch convention; the headnote restores
\textit{Pontifex Maximus} in prose); Perseus TEI for letter n=``34''
yields \textbf{only the short private letter}, not the standard
Shackleton Bailey 10.34A/B split --- the longer dispatch is not
present in our source); \textbf{10.35 (Lepidus to the Senate and
Roman People, in camp at the Pons Argenteus, 30 May 43 BC --- the
famous official defection-defense letter by which Lepidus was
declared a public enemy, with the load-bearing exculpatory
\textit{seditione facta \ldots\ coegit} ``an uprising having broken
out \ldots\ compelled me,'' the technical-legal request
\textit{misericordiam \ldots\ sceleris loco ne ponatis} ``do not
count our pity as a crime,'' and the deflection of agency through
\textit{fortuna proprium consilium extorsisset} ``fortune wrung
from my hands a policy of my own''; the salutation runs
\texttt{M. LEPIDVS IMP. ITER. PONT. MAX. PR. TR. PL. SENATVI POPVLO
PLEBIQVE ROMANAE} preserved in full)}.
\end{itemize}

\textbf{Metadata corrections committed to \texttt{meta/works.yaml}
during session 25 (2 date-precision corrections):}
\begin{itemize}
\item \textit{Fam.} 10.26: \texttt{date\_precision} \texttt{day}
$\rightarrow$ \texttt{month}, per Perseus \textit{inter viii et iii
K. Quint. a. 711 (43)} = ``between 24 and 29 June 43 BC,'' a 6-day
range incompatible with day-precision. Date kept at \mbox{-0043-06-29}
as the upper bound.
\item \textit{Fam.} 10.33: date \mbox{-0043-06-13} day-precision
$\rightarrow$ \mbox{-0043-06-01} month-precision, per Perseus
\textit{vel ex. m. Maio vel in. Iun. a. 711 (43)} = ``either end of
May or beginning of June,'' explicitly a range across two months.
The 13 June day-precision was plainly wrong.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Fam.} 10.27 \textit{mortem servituti
anteponant} formulation.} ``Set death before servitude'' rendered
without softening; one of Cicero's clearest single statements of
the Republican principle at issue against Antony / the impending
Lepidus defection. The companion \textit{impotentissimi dominatus}
``utterly intolerable despotism'' uses the old sense of
\textit{impotens} (ungovernable, intolerable), not the modern
``powerless.'' Worth a sustained translator-note.
\item \textbf{The \textit{Fam.} 10.28 \textit{quam vellem ad illas
pulcherrimas epulas me Idibus Martiis invitasses!}} The corpus's
most explicit retroactive endorsement of the assassination plot.
Render carefully against the canonical Shuckburgh / Shackleton
Bailey phrasings, which sometimes stick. The banquet metaphor
sustained through \textit{reliquiarum nihil haberemus}
``there would be no leftovers'' --- the table-register kept rather
than smoothed to ``remnants / scraps.'' Worth a sustained note.
\item \textbf{The \textit{Fam.} 10.30 Galba battle dispatch as
corpus-level military witness.} The rare technical-Latin register,
the \textit{evocati} ``re-enrolled veterans,'' the corrupt
\texttt{to cohors praetoria} in \S4 read minimally as ``and the
praetorian cohort,'' and the careful day-arithmetic placing the
battle on a.~d.~xviii K.~Mai.\ (14 April) and the dispatch on
a.~d.~xvii K.~Mai.\ (15 April). Worth a corpus-level note on the
letter as eyewitness Roman battle-narrative.
\item \textbf{The \textit{Fam.} 10.31 \textit{vindicare in
libertatem}.} The technical legal-political idiom (recovering by
formal claim) preserved with the Latinate cognate ``vindicate into
liberty'' rather than the flatter ``deliver / restore into
liberty.'' Worth a textual-political note.
\item \textbf{The \textit{Fam.} 10.32 \textit{`C. R. natus sum'}
Verrine echo.} Balbus's victims appealing as Roman citizens to be
spared the arena --- the abbreviated \textit{civis Romanus natus
sum} formula that Cicero made famous in the second Verrine.
Allusion-sidecar candidate.
\item \textbf{The \textit{Fam.} 10.32 \textit{defodit in ludo et
vivum combussit}.} ``Buried in the arena and burnt alive'' rendered
to preserve the implied sequence (up to the neck, then incinerated);
the standard reading. The Pollionian Latin pun on
\textit{peculiatus / peculatus} in \S1 unrecoverable in English;
rendered ``featherbedded'' for the contemptuous force only.
\item \textbf{The \textit{Fam.} 10.33 \textit{neque desse neque
superesse rei p. volo}.} ``I wish neither to fail the commonwealth
nor to outlive it'' --- the famous Pollio formulation, with the
wordplay on \textit{deesse / superesse} preserved through
``fail / outlive.'' Worth a sustained note as one of the most-cited
single phrases in Pollio's surviving prose.
\item \textbf{The \textit{Fam.} 10.34 \texttt{PONL MAX.}\ OCR
corruption.} Perseus TEI transmits the salutation with
\texttt{PONL MAX.}\ for \texttt{PONT. MAX.} --- preserved
as-transmitted in the \texttt{\textbackslash ciceroLetterOpener}
per fetch convention; restored in the headnote prose. Worth a
textual-source note for the scholar profile.
\item \textbf{The \textit{Fam.} 10.35 \textit{seditione facta
\ldots\ coegit} as the formal defection-defense.} The load-bearing
exculpatory phrase by which Lepidus deflects agency, and on which
the Senate's declaration of him as public enemy turned. The
technical-legal request \textit{sceleris loco ne ponatis} ``do not
count [our pity] as a crime'' is the very legal category the
Senate did then impose. Worth a sustained corpus-level note as
the single best example of formal Roman official-defense prose.
\item \textbf{The \textit{Fam.} 10.34 transmission gap (10.34B
absent).} Standard editions split this slot into 10.34A (private
letter to Cicero) and 10.34B (the longer dispatch); Perseus's TEI
yields only 10.34A. Worth a metadata note flagging that future
manual sourcing may add a 10.34B file.
\end{itemize}

\textbf{Suggested next translation batch} (when session 25 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 25:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice U' opening: \textit{Fam.} 11 to Decimus
Brutus.} Book 10 is now closed. The next active sub-sequence is
\textit{Fam.} 11, the Decimus Brutus correspondence, covering the
Mutina campaign from Decimus's perspective. Parallel-dispatchable
at 3--4 per worker, similar to the Plancus correspondence pattern.
\textit{Fam.} 11.1 is the chronologically next pending letter
inside the gap zone.
\item \textbf{Slice S (the chronological-gap sweep, 189 pending
letters earlier than the -0043-07-28 10.24 marker):} substantial
backlog --- the \textit{Att.} 13.36 metadata followup, the two
pending \textit{Att.} 13.15 / 13.18 placeholder stubs awaiting
manual Latin from session 18, the remaining \textit{Fam.} 5
sub-cluster (5.15--5.18, all 45 BC, parallel-dispatchable), the
\textit{Fam.} 5.10a/5.10b split work flagged in session 20, the
early-43 BC \textit{Fam.} 12 (Cassius correspondence) and
\textit{Ad Brutum} correspondence, plus the four Ad M.~Brutum
letters with broken sources (1.16, 2.6, 2.7, 2.8) flagged by the
post-session-23 infrastructure pass.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} 429 entity stubs
in \texttt{data/entities.json} remain after the session-23-followup
43-stub pilot --- ripe for an aggressive parallel apparatus pass.
\end{itemize}


\textbf{Translation state (post-Cowork-session-24):} \textbf{746 /
958 works drafted (\~77.9\%)}. \textbf{Latest drafted by deep
chronology advanced} from \textit{Ad Atticum} 16.15 (Arpinum, 9
December 44 BC) to \textit{Ad Familiares} 10.24 (Plancus's camp in
Gaul, 28 July 43 BC) --- a roughly seven-month advance that opens
\textbf{Slice U}, the \textit{Fam.} 10 Plancus correspondence, and
drives it from 10.1 through 10.24. Session 24 drafted \textbf{24
letters in two parallel waves (six workers total)} --- the entire
opening two-thirds of Cicero's epistolary campaign to keep
L.~Munatius Plancus, governor of Transalpine Gaul, loyal to the
Senate through the Mutina war and Lepidus's defection. The
chronological-gap warning now reports \textbf{200 pending works
dated earlier than the latest-drafted (10.24 at -0043-07-28)}, up
from 115 immediately after session 23; the gap inflation reflects
the marker advance from 9 Dec 44 BC to 28 Jul 43 BC exposing
previously-above-marker letters --- the 24 drafted this session
went forward chronologically into the Plancus correspondence
rather than into the earlier-dated backlog.

\textbf{Cowork session 24 --- 24 letters drafted across two
parallel waves (six workers):}

\textbf{Wave 1 (4 workers, 16 letters --- the opening \textit{Fam.}
10 cluster, Sept 44 BC -- mid-May 43 BC):}
\begin{itemize}
\item \textbf{Worker A (\textit{Fam.} 10.1--10.4, 4 letters):} 10.1
(Rome, shortly after 19 September 44 BC, the opening letter of
the correspondence --- Cicero on Antony's tyranny and Plancus's
coming consulship as the only hope, \textit{nec senatus nec
populus vim habet ullam nec leges ullae sunt nec iudicia});
10.2 (Rome, 5 October 44 BC, on the Sept/Oct Senate sessions and
the chamber surrounded by armed men --- \textit{ubi me et melius
et propius audiant armati quam senatores}); 10.3 (Rome, 10
December 44 BC, on the \textit{nimis servire temporibus}
diagnosis and the \textit{orbitas} of the republic bereaved of
its leading men); 10.4 (Plancus to Cicero, from Transalpine
Gaul, end of December 44 BC --- the first surviving Plancus
reply, opening the correspondence Plancus side).
\item \textbf{Worker B (\textit{Fam.} 10.5--10.8, 4 letters):}
10.5 (Cicero, Rome, mid-December 44 BC); 10.6 (Cicero, Rome, 20
March 43 BC, with the \textit{magnus consul et consularis}
anaphora); 10.7 (Plancus, Gaul, a little after mid-March 43 BC,
with the chiasmus \textit{nec defensorem mihi paravi quam
praedicatorem meritorum meorum esse volui}); \textbf{10.8 (the
substantial Plancus public dispatch to senate and people, Gaul,
mid-March 43 BC, with the candid \textit{simulasse / dissimulasse}
admission of his two-faced political holding pattern and the
\textit{omnem impetum belli in me convertere} heroic-stance
close; the salutation \texttt{PLANCVS IMR COESIG. COS. PR. TR.
PL. SENATVI POPVLO PLEBIQVE ROMANAE} is the full official
address \textbf{meta-date corrected -0043-01-01 year $\rightarrow$
-0043-03-18 month} per Perseus \textit{paulo post med. Mart.})}.
\item \textbf{Worker C (\textit{Fam.} 10.9--10.12, 4 letters):}
10.9 (Plancus, Narbonensis, 26 April 43 BC); 10.10 (Cicero, Rome,
30 March 43 BC, with the apparent corruption \textit{patriae
cantas} silently rendered ``love of country''); \textbf{10.11
(Plancus, Allobrogan country, end of April 43 BC, the substantial
\textit{tuum munus tuere} ``look after your own creation'' letter
to Cicero on having vouched for him politically)}; \textbf{10.12
(Cicero, Rome, 11 April 43 BC, the major letter celebrating
Plancus's loyalty just announced to the Senate, with the tricolon
\textit{brevia, fucata, caduca} ``short-lived, painted, fragile''
on the empty insignia of office, and the \textit{pullariorum
admonitu} chicken-keepers-as-auspicial-officers detail)}.
\item \textbf{Worker D (\textit{Fam.} 10.13--10.16, 4 letters):}
\textbf{10.13 (Cicero, Rome, 11 May 43 BC; Greek epithet
\textit{ptolipo/rqion} ``sacker of cities'' --- Homer applied to
Plancus)}; 10.14 (Cicero, Rome, 5 May 43 BC); \textbf{10.15
(Plancus, on the Isère in Gallia Narbonensis cis Isaram, c.~13
May 43 BC, with the dated march --- Isère crossing 12 May,
brother's dispatch 13 May --- \textbf{meta-date corrected
-0043-08-08 year $\rightarrow$ -0043-05-13 day} per Perseus
\textit{circ. iii Id. Mai.})}; \textbf{10.16 (Cicero, Rome, late
May 43 BC, with the famous \textit{ipse tibi sis senatus} ``be
your own senate'' authorization, \textbf{location-field cleanup
\texttt{Romae ctrc} $\rightarrow$ \texttt{Romae}})}.
\end{itemize}

\textbf{Wave 2 (2 workers, 8 letters --- the Lepidus-defection
cluster, mid-May -- 28 July 43 BC):}
\begin{itemize}
\item \textbf{Worker E (\textit{Fam.} 10.17--10.20, 4 letters):}
\textbf{10.17 (Plancus, on the road to Lepidus, 19 May 43 BC,
\textbf{meta-date corrected -0043-06-01 day $\rightarrow$
-0043-05-19 day} per Perseus \textit{xv K. Iun.}; daggered crux
\textit{\dag{}de tribus fratribus Segaviano\dag{}} on an
unrecoverable tribal-name reference preserved with the dagger)};
\textbf{10.18 (Plancus, in camp on the march from the Isère to
Forum Voconi, 18 May 43 BC, with the famous \textit{Ventidi
mulionis castra} ``the muleteer Ventidius's camp'' taunt at
Ventidius Bassus's youth driving mules, and the \textit{intra
cutem subest vulneris} ``a wound festering beneath the skin''
image; \textbf{location-field cleanup \texttt{ab Isara
\textbf{itiitere} Forum Voconi $\rightarrow$ itinere})}; 10.19
(Cicero, Rome, c.~26 May 43 BC, short); 10.20 (Cicero, Rome, 29
May 43 BC, with the clipped half-quotation of the Greek proverb
\textit{his ad eundem} pointing to $\delta\grave{\iota}\varsigma$
$\pi\rho\grave{\text{o}}\varsigma$ $\tau\grave{\text{o}}\nu$
$\alpha\grave{\text{u}}\tau\grave{\text{o}}\nu$ $\lambda\acute{\iota}\theta$o$\nu$
``twice against the same stone'').
\item \textbf{Worker F (\textit{Fam.} 10.21--10.24, 4 letters):}
\textbf{10.21 (Plancus, camp in Allobrogan country, c.~15 May 43
BC, on the Isara bridge and Laterensis's warning of Lepidus's
imminent defection; \textbf{location-field cleanup \texttt{in
castris pnd} $\rightarrow$ \texttt{in castris})}; 10.22 (Cicero,
Rome, late June 43 BC); \textbf{10.23 (Plancus, Cularo in
Allobrogan country, 6 June 43 BC, the major Plancus dispatch on
Lepidus's defection at the Isara, the corpus's clearest
first-person account of the moment the Senate-Plancus-Lepidus
plan collapsed, with a fuller two-paragraph headnote per its
historical weight)}; \textbf{10.24 (Plancus, in camp, 28 July 43
BC, the deteriorating-situation letter as Octavian pivots toward
the consulship and the Triumvirate looms; daggered crux
\textit{\dag{}talis victoriae\dag{}} in \S3 on the
\textit{a-victory-of-such-a-kind} preserved with the dagger;
fuller two-paragraph headnote)}.
\end{itemize}

\textbf{Metadata corrections and location/recipient cleanups
committed to \texttt{meta/works.yaml} during session 24 (3 date
corrections + 3 location/recipient cleanups):}
\begin{itemize}
\item \textit{Fam.} 10.8: date \mbox{-0043-01-01} year-precision
$\rightarrow$ \mbox{-0043-03-18} month-precision per Perseus
\textit{paulo post med. Mart. a. 711 (43)}. The year-precision
placeholder was plainly wrong; this is the headline correction.
\item \textit{Fam.} 10.15: date \mbox{-0043-08-08} year-precision
$\rightarrow$ \mbox{-0043-05-13} day-precision per Perseus
\textit{circ. iii Id. Mai. a. 711 (43)}, confirmed by the
in-letter datelines of the Isère crossing.
\item \textit{Fam.} 10.17: date \mbox{-0043-06-01} day-precision
$\rightarrow$ \mbox{-0043-05-19} day-precision per Perseus
\textit{xv K. Iun. a. 711 (43)}.
\item \textit{Fam.} 10.16: \texttt{location\_written} \texttt{Romae
ctrc} $\rightarrow$ \texttt{Romae} (OCR-bleed of \textit{circ.}\
from the dateline header into the location field).
\item \textit{Fam.} 10.18: \texttt{location\_written} \texttt{in
castris ex itiitere ab Isara Forum Voconi} $\rightarrow$
\texttt{in castris ex itinere ab Isara Forum Voconi} (OCR doubling
\textit{itinere} $\rightarrow$ \textit{itiitere}).
\item \textit{Fam.} 10.21: \texttt{location\_written} \texttt{in
castris pnd} $\rightarrow$ \texttt{in castris} (OCR-bleed of
\textit{pnd Id. Mai.}\ from the dateline header).
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Fam.} 10.1 opening as the corpus's
clearest single-sentence diagnosis of 44 BC.} \textit{quae potest
enim spes esse in ea re p., in qua hominis impotentissimi atque
intemperantissimi armis oppressa sunt omnia, et in qua nec
senatus nec populus vim habet ullam nec leges ullae sunt nec
iudicia nec omnino simulacrum aliquod ac vestigium civitatis?}
The asyndetic tricolon-then-tetracolon on the absence of senate,
people, laws, courts, then ``not even any image or trace of a
state'' is the canonical Ciceronian late-44 diagnosis. Worth a
sustained translator-note.
\item \textbf{The \textit{Fam.} 10.2 \textit{summa impunitate
gladiorum} image.} ``In such utter impunity of swords'' --- the
literal-shocking rendering preserved over the more idiomatic
``with swords drawn and unaccountable.'' Worth a note on the
preservation of the harsh Latin metaphor.
\item \textbf{The \textit{Fam.} 10.6 \textit{magnus consul et
magnus consularis} anaphora.} The repeated adjective makes the
antithesis with the immediately-following \textit{summa
deformitas} structural; the English keeps the repetition.
\item \textbf{The \textit{Fam.} 10.7 \textit{defensor / praedicator}
chiasmus.} Plancus's chiastic boast \textit{nec te magis in culpa
defensorem mihi paravi quam praedicatorem meritorum meorum esse
volui} preserved in the English by flipping order: ``herald of my
deserts no less than advocate of my faults.''
\item \textbf{The \textit{Fam.} 10.8 \textit{simulasse /
dissimulasse} pair.} Plancus's candid admission of two-faced
behaviour preserved through the etymological pair (``feigned\ldots
dissembled''); the political implication (that he had been lying
to Antony's circle while building his force) handled in the
headnote rather than glossed in body.
\item \textbf{The \textit{Fam.} 10.10 \textit{patriae cantas / caritas}
corruption.} Silently rendered ``the love of country'' rather
than daggered, on the assumption that \textit{cantas} is a clear
copyist's slip for \textit{caritas}. Worth a textual note for the
scholar profile.
\item \textbf{The \textit{Fam.} 10.11 \textit{tuum munus tuere}
metaphor.} ``Look after your own creation'' for Cicero's having
vouched for Plancus politically --- the language of patronage and
sponsorship made into a creator-and-creation image.
\item \textbf{The \textit{Fam.} 10.12 tricolon \textit{brevia,
fucata, caduca}.} ``Short-lived, painted, fragile'' on the empty
insignia of office, with \textit{fucata} (literally ``dyed,
rouged'') preserved as ``painted'' to keep the cheap-cosmetic
metaphor. The accompanying \textit{pullariorum admonitu}
chicken-keepers-as-auspicial-officers reference is a glossary-realia
candidate.
\item \textbf{The \textit{Fam.} 10.13 Homeric epithet
\textit{ptolipo/rqion} for Plancus.} Cicero applies Homer's
formulaic epithet for Odysseus / Achilles to Plancus as a
sacker-of-cities flattery on his coming consulship. Allusion-sidecar
candidate.
\item \textbf{The \textit{Fam.} 10.16 \textit{ipse tibi sis
senatus}.} ``Be your own senate'' as constitutional authorization
for Plancus to act independently when the Senate cannot meet.
The most-cited line of the entire Plancus correspondence; worth
a sustained note on the constitutional implications.
\item \textbf{The \textit{Fam.} 10.18 \textit{Ventidi mulionis
castra} taunt.} ``The muleteer Ventidius's camp'' --- the
famous-from-Suetonius taunt at Ventidius Bassus's youth driving
mules, here in its earliest surviving Latin attestation. Worth a
glossary-realia note on Ventidius's rise from muleteer to consul.
\item \textbf{The \textit{Fam.} 10.18 \textit{intra cutem subest
vulneris} image.} ``A wound festering beneath the skin'' --- the
strongest single phrase in Plancus's voice, on Lepidus's
secretly-collapsed loyalty. Worth a note on Plancus's prose
register.
\item \textbf{The \textit{Fam.} 10.20 \textit{his ad eundem}
clipped Greek proverb.} The Latin half-quotation pointing to
the Greek $\delta\grave{\iota}\varsigma$
$\pi\rho\grave{\text{o}}\varsigma$ $\tau\grave{\text{o}}\nu$
$\alpha\grave{\text{u}}\tau\grave{\text{o}}\nu$ $\lambda\acute{\iota}\theta$o$\nu$
``twice against the same stone'' --- the underlying Greek noted in
the sidecar JSON. Worth an allusion-sidecar entry and a
translator-note on Cicero's habit of clipped half-quoted Greek
proverbs.
\item \textbf{The \textit{Fam.} 10.23 Plancus dispatch as the
corpus's clearest first-person account of Lepidus's defection.}
The 6 June 43 BC dispatch from Cularo is the single best
contemporary witness to the moment the Senate-Plancus-Lepidus
plan collapsed on the Isara. Worth a sustained corpus-level
translator-note on its evidentiary value.
\item \textbf{The \textit{Fam.} 10.24 \textit{\dag{}talis
victoriae\dag{}} daggered crux.} The §3 daggered crux preserved
in the English as ``a victory of such a kind'' with the daggers;
the precise sense of Plancus's hedge on the desired/feared
victory is unrecoverable. Worth a textual note for the scholar
profile.
\end{itemize}

\textbf{Suggested next translation batch} (when session 24 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 24:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice U continuation: \textit{Fam.} 10.25--10.35 (11
remaining Plancus / book-10 letters).} The Plancus correspondence
runs through 10.34, plus 10.35 (Lepidus to Senate, late May 43
BC, bound at the close of book 10). Parallel-dispatchable at 3--4
per worker; about 3 worker-batches' worth of material to finish
book 10. \textit{Fam.} 10.25 is the chronologically next pending
letter.
\item \textbf{Slice U' opening: \textit{Fam.} 11 to Decimus
Brutus.} Once book 10 closes, the chronologically next active
sub-sequence is \textit{Fam.} 11, the Decimus Brutus
correspondence, also covering the Mutina campaign. Parallel-
dispatchable similarly. \textit{Fam.} 11.1 is the next-pending
after book 10 closes.
\item \textbf{Slice S (the chronological-gap sweep, 200 pending
letters earlier than the new -0043-07-28 marker):} substantial
backlog --- the \textit{Att.} 13.36 metadata followup (no Perseus
URL --- check whether it merges with 13.35 per Shackleton Bailey),
the two pending \textit{Att.} 13.15 and 13.18 placeholder stubs
(awaiting manual Latin from session 18), the remaining
\textit{Fam.} 5 sub-cluster (5.15--5.18, all 45 BC,
parallel-dispatchable), and the \textit{Fam.} 5.10a/5.10b split
work flagged in session 20. The 10.24 marker advance to 28 July
exposes the early-43 BC \textit{Fam.} 12 and \textit{Ad Brutum}
correspondence as above-marker as well.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has \~429 stub entries needing real summaries
after the session-23-followup 43-stub pilot --- ripe for an
aggressive parallel pass.
\end{itemize}


\textbf{Infrastructure session (2026-05-19, after session 23):} An
infrastructure-only pass landed four standalone improvements
between session 23's translation work and the next translation
session. No new translations; no chronology pointer change.

\textbf{1. Metadata audit + safe-fix scripts}
(\texttt{scripts/audit\_metadata.py},
\texttt{scripts/fix\_metadata\_safe.py}) --- the audit script parses
each Latin file's \texttt{\% Dateline (Perseus):} comment, checks
\texttt{location\_written} and \texttt{recipient} fields for
OCR-bleed of date tokens or salutation suffixes, and runs Roman date
arithmetic to compare the computed Julian date against
\texttt{meta/works.yaml}. The safe-fix script applies the
high-confidence subset of corrections (trailing salutation tokens
stripped from recipients, trailing date-bleed stripped from
locations, seven year-precision $\rightarrow$ month- or day-precision
date corrections). 375 changes applied; field-hygiene flag count
fell from 224 to 23 (\~90\% reduction). The remaining 23 are
OCR-corrupted fragments like \texttt{vh}, \texttt{mcd},
\texttt{t\%u} that need Shackleton Bailey manual review and were
deliberately left for a human pass. The audit report is regenerated
to \texttt{meta/audit-report.md} on each script run.

\textbf{2. Translator-notes backlog flush.} 23 sessions'
\textbf{Translator-notes worth logging} sections accumulated in
PROGRESS.md but were never written into the canonical
\texttt{data/translator-notes.jsonl}. Three parallel sub-agents
extracted them in chunks (lines 100--2500, 2500--5000,
5000--7445), each writing to a temporary staging JSONL. The
results were merged with deduplication-by-content and appended to
\texttt{data/translator-notes.jsonl}: \textbf{290 new entries}
landed, bringing the total from 16 to 306. The temporary
\texttt{data/\_tmp\_notes\_batch\{1,2,3\}.jsonl} files were
overwritten with \texttt{\% PLACEHOLDER} stubs (sandbox cannot
delete); \texttt{scripts/cowork\_handoff.sh} now strips them at
handoff time.

\textbf{3. Perseus source-availability audit script}
(\texttt{scripts/audit\_perseus\_sources.py}) --- categorises every
pending work as \texttt{ok}, \texttt{placeholder},
\texttt{unfetched-ok}, \texttt{unfetched-missing}, or
\texttt{no-perseus}. Fetches each Perseus TEI \textbf{once per
book-file} (cached in \texttt{/tmp/cicero-perseus-cache/}) and
scans for \texttt{<div type="textpart" subtype="letter" n="N">} to
verify the textpart exists. Found a previously-undetected gap:
\textbf{4 Ad M. Brutum letters (1.16, 2.6, 2.7, 2.8) have only the
404'd Latin Library fallback URL --- no Perseus source}. These
need manual Latin sourcing before the chronology reaches July 43
BC. Output at \texttt{meta/perseus-audit.md} +
\texttt{meta/perseus-audit.json}.

\textbf{4. Entity-stub enrichment pilot (43 stubs).} The first
batched apparatus pass: a single sub-agent enriched 43 of 472
entity stubs in \texttt{data/entities.json} --- all 24 gods, 6
laws, all 3 festivals, the 1 institution, 5 famous Romans
(Alexander, Cato Censorius, Mithridates VI, Antiochus III, generic
Gracchi), and 6 major geographies (Achaia, Aegyptus, Asia, Britain,
Cilicia, Cnidus). 5 of the listed 50 IDs didn't exist in
entities.json (\texttt{law:lex-aurelia},
\texttt{law:lex-cornelia-de-iurisdictione},
\texttt{law:lex-iulia-de-civitate}, \texttt{law:lex-papia},
\texttt{text:annales-maximi}); they were skipped per the agent's
brief. Stub count: \textbf{472 $\rightarrow$ 429}. File integrity
verified (831 total entries unchanged, only \texttt{summary} fields
on the 43 targets modified). This is the pilot for the
\~8-session apparatus pass forecast in
\texttt{OPERATING\_PLAN.md}; remaining stubs (429) can be cleared
at the rate of 50 per pilot-style session or batched more
aggressively.

\textbf{Validation after the infrastructure pass:} 958 entries, 8
warnings (orphan Latin file from session 1, 7 chronological-gap
entries --- both pre-existing and unaffected by infrastructure
work).

\textbf{Suggested follow-ups specific to this infrastructure work:}
\begin{itemize}
\item Fix the 4 Ad Brutum source URLs from the
  \texttt{perseus-audit.md} report. Perseus TEI for Ad M. Brutum is
  at \texttt{phi0474.phi058.perseus-lat2.xml} (book 1) and
  \texttt{phi0474.phi059.perseus-lat2.xml} (book 2); the works.yaml
  entries currently only carry the 404'd Latin Library fallback.
\item Re-run \texttt{scripts/audit\_metadata.py} after any future
  works.yaml hand-edits; the report acts as a regression check.
\item Continue entity-stub enrichment: 429 stubs remain. The
  next-batch suggestion is to clear the In Verrem witness cluster
  (the bulk of remaining person-stubs) plus the remaining 100+
  Sicilian and provincial place-stubs.
\end{itemize}


\textbf{Translation state (post-Cowork-session-23):} 722 / 958 works
drafted (\~75.4\%). \textbf{Latest drafted by deep chronology
advanced} from \textit{Ad Atticum} 16.3 (Pompeianum, 17 July 44
BC) to \textit{Ad Atticum} 16.15 (Arpinum, 9 December 44 BC) ---
the entire remainder of the surviving Atticus correspondence
through to its final letter. \textbf{Session 23 drafted all 13
pending letters of \textit{Att.} 16 (16.4--16.16) in a single
parallel wave of four workers.} This closes the book and brings
the Atticus correspondence to its complete drafted state through
December 44 BC. The chronological-gap warning now reports
\textbf{115 pending works dated earlier than the latest-drafted
(16.15 at -0044-12-09)}, down from 118 immediately after session
22; the marker advance from -0044-10-25 to -0044-12-09 surfaced
additional pending letters but the 13 letters drafted this session
net to a modest reduction.

\textbf{Cowork session 23 --- 13 letters drafted in one parallel
wave (four workers):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 16.4--16.6, 3 letters, 9--25
July 44 BC, Puteolanum / Vibo Valentia):} 16.5 (9 July, Puteolanum,
the playful exchange about Brutus's mistaken expectation of an
Accius \textit{Brutus} at his games, with the clustered Greek
epithets \textit{am\=ym\=on / ambrotos} ``matchless / divine'' in
Homeric-rank wordplay; the brilliant self-deprecating close ``Look
around you --- only do it before I blush''); 16.4 (10 July, Puteolanum,
the bitter ``or whatever title they go by'' refusing to dignify
Antony and Dolabella with the consular title; ``the Nones of July''
play on the renamed \textit{Quintilis}); 16.6 (25 July, Vibo Valentia,
the \textit{ocellos Italiae, villulas meas} ``little eyes of Italy,
my own small villas'' diminutives carrying a probable Catullus 31
echo --- allusion-sidecar candidate; \textit{dolichon ploon} ``long
voyage'' opening the journey-letters proper).
\item \textbf{Worker B (\textit{Att.} 16.7--16.9, 3 letters, 19
August -- 4 November 44 BC, navigans / Puteolanum):} \textbf{16.7
(the famous turnabout letter, written while sailing back up the
coast from Leucopetra after the meeting with Brutus at Velia,
recounting the storm-driven return, the Olympia-reproach insinuation
that Cicero was running off to spectate the games, and the Senate
session of 1 August where Piso was abandoned --- the corpus's
clearest first-person account of the decision to return and make
the political fight that becomes the Philippics; seven Greek phrases
including the Homeric-resonant \textit{anemes\=eta} ``past blame,''
\textit{euthanasian} ``a good ending,'' and the medical
\textit{peirazesthai paralysei} on Pilia's stroke; lacuna at §2
in the manuscript preserved as a numbering gap)}; 16.8 (the
\textit{vide nomen, vide aetatem} ``look at the name, look at the
age'' Octavian-paradox compressed to four words, the apostrophe
\textit{o Brute, ubi es?}\ ``O Brutus, where are you?,'' and the
archaic numeral \textit{ci\b{$\supset$} ci\b{$\supset$} ci\b{$\supset$}}
= 3,000 for Octavian's veterans); 16.9 (very short, the doubled
\textit{iam iamque video bellum} ``already, already I see war'').
\item \textbf{Worker C (\textit{Att.} 16.10--16.13, 4 letters,
5--13 November 44 BC, Puteolanum / Sinuessanum / Aquinum):} 16.10
(Sinuessanum, very short, plain Roman date-arithmetic); \textbf{16.11
(\textbf{the long political-strategy letter}, Puteolanum, 5 Nov ---
the Second Philippic pamphlet under Sextus Peducaeus's
\textit{samizdat} circulation referred to as \textit{nostrum
opus} ``my work,'' the Heraclitus B49 tag \textit{heis emoi
murioi} ``one man is to me ten thousand,'' the Iliad 7.93
\textit{aidesthen men an\=enasthai} ``ashamed to refuse'' applied
to Octavian's overtures, plus eighteen Greek phrases including
\textit{P\=eplographia}, \textit{H\=erakleideion},
\textit{taxiarch\=es}, the dense \textit{ta peri tou kath\=ekontos}
and \textit{prosph\=on\=o} dedications on \textit{De Officiis}
under composition --- corpus-level hinges)}; \textbf{16.12 (very
short, Puteolanum, 13 Nov; \textbf{location-field cleanup
\texttt{in Puteolano vht} $\rightarrow$ \texttt{in Puteolano}};
section-1 stray \textit{frustra me istic} \textbf{t} \textit{esse}
preserved as a textual oddity)}; 16.13 (Aquinum, 10 Nov, two
Homeric tags from the same Odyssey 3 passage --- \textit{dolichon
ploon hormainonta} and \textit{par' \=enemoenta Mimanta} ---
worth a translator-note on Cicero's epistolary citation habit;
section 3 opens with a manuscript lacuna preserved as
\texttt{* * *}).
\item \textbf{Worker D (\textit{Att.} 16.14--16.16, 3 letters,
middle November -- 9 December 44 BC + the chronologically misplaced
16.16):} \textbf{16.14 (Arpinum, \textbf{date correction
\mbox{-0044-07-19} $\rightarrow$ \mbox{-0044-11-15},
\texttt{date\_precision} \texttt{year} $\rightarrow$ \texttt{month}}
per Perseus \textit{medio mense Novembri}; two Greek phrases
\textit{kath\=ekon} ``duty/the proper'' and \textit{hypomn\=ema}
``memorandum''; the cryptic closing \textit{avi tui pronepos
scribit ad patris mei nepotem\ldots aedem Opis explicaturum}
``your grandfather's great-grandson writes to my father's grandson
\ldots will open the temple of Ops'' --- a Roman family riddle
transparent to Atticus but opaque now, worth a translator-note;
\S2 missing from Perseus preserved as a numbering gap)};
\textbf{15-Dec 16.15 (Arpinum, \textbf{the last surviving Atticus
letter chronologically, the close of the Atticus archive}; four
Greek phrases including the famous outburst against Octavian
\textit{m\=ede s\=othei\=en hypo ge toioutou} ``may I never be
saved by the likes of him'' --- bitterly ironic in light of the
Second Triumvirate proscriptions a year later, definite
translator-note --- and the comic-stage \textit{Stratullax}
``strutter'' applied to Antony as a comic-soldier-type; four
daggered cruxes preserved as defensively translated stretches};
\textbf{location-field cleanup \texttt{in Arpinati ante}
$\rightarrow$ \texttt{in Arpinati}})}; \textbf{16.16 (Tusculanum,
3--6 July 44 BC, \textbf{chronologically much earlier than the
surrounding book-16 cluster, bound at the close of book 16 by the
manuscript transmission}; Perseus's TEI carries \textbf{only the
brief four-sentence cover-note}; the standard composite editions
attach 16.16A--E forwarded letters to Plancus, Capito, Cupiennius
\textit{et al.}\ which are \textbf{not present in our source} and
were not invented; \textbf{recipient-field cleanup \texttt{suo
DIC. ATTICO} $\rightarrow$ \texttt{ATTICO}}, the OCR-contaminated
salutation rendered as the standard \textit{CICERO ATTICO salutem}
opener in the English file)}.
\end{itemize}

\textbf{Date corrections and location/recipient cleanups committed
to \texttt{meta/works.yaml} during session 23 (one date correction
+ three location/recipient cleanups):}
\begin{itemize}
\item \textit{Att.} 16.14: date \mbox{-0044-07-19} $\rightarrow$
\mbox{-0044-11-15} and \texttt{date\_precision} \texttt{year}
$\rightarrow$ \texttt{month}, per Perseus \textit{medio mense
Novembri a. 710 (44)}. The year-precision placeholder was
plainly wrong; this is the headline correction.
\item \textit{Att.} 16.12: \texttt{location\_written} \texttt{in
Puteolano vht} $\rightarrow$ \texttt{in Puteolano} (OCR-bleed of
the dateline's corrupt \texttt{vht Id. Nov.}\ into the location
field). The dateline itself remains \texttt{vht Id. Nov.}\ in the
Latin-file comment header; reading as \texttt{Id. Nov.}\ = 13
November, which matches the meta-entry date \mbox{-0044-11-13}.
\item \textit{Att.} 16.15: \texttt{location\_written} \texttt{in
Arpinati ante} $\rightarrow$ \texttt{in Arpinati} (OCR-bleed of
the dateline's \textit{ante v Id. Dec.}\ ``before 9 December''
into the location field).
\item \textit{Att.} 16.16: \texttt{recipient} \texttt{suo  DIC.
ATTICO} $\rightarrow$ \texttt{ATTICO} (OCR-contaminated salutation
\textit{CICERO suo salutem DIC. ATTICO} cleaned to the standard
form; the worker's English file renders the opener as \textit{CICERO
ATTICO salutem}).
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The Att.\ 16.6 \textit{ocellos Italiae, villulas
meas} echo of Catullus 31.} The diminutives ``little eyes of
Italy, my own small villas'' carry the Catullan \textit{Sirmio,
insularum ocelle} as a probable allusion --- the bay-of-Naples
estate-talk drawing on the Sirmio territory of intimate ownership.
Worth a high-certainty allusion-sidecar entry.
\item \textbf{The Att.\ 16.7 Leucopetra turnabout as the corpus's
clearest first-person account of the decision that produces the
Philippics.} The letter combines the storm-driven return, the
Velia meeting with Brutus, and the Olympia-reproach insinuation
into a single narrative arc; the implicit answer to the
\textit{o Brute, ubi es?}\ apostrophe in 16.8. Worth a sustained
corpus-level translator-note on the Velia-meeting hinge.
\item \textbf{The Att.\ 16.7 \textit{anemes\=eta} Homeric register.}
``Past blame'' / ``not such as to draw nemesis'' --- a markedly
epic-register Greek choice for a letter whose subject is whether
his return from Leucopetra was honourable or shameful. Worth a
translator-note on Cicero's reach for Homer when the question is
his own honour.
\item \textbf{The Att.\ 16.8 \textit{ci\b{$\supset$}
ci\b{$\supset$} ci\b{$\supset$}}\ = 3,000 archaic Roman numeral.}
The antiquarian apostrophus numeral form is preserved in Perseus
and rendered ``three thousand veterans'' in the English. Worth a
glossary-realia note on the apostrophus numeral system and its
survival in epistolary Latin.
\item \textbf{The Att.\ 16.11 corpus-level \textit{De Officiis}
notice and the Second Philippic \textit{samizdat}.} The double-
hinge letter: \textit{ta peri tou kath\=ekontos\ldots prosph\=on\=o}
``on the proper duties\ldots I dedicate'' marks \textit{De Officiis}
in active dedication, while \textit{nostrum opus} ``my work''
circulating among Sextus Peducaeus's circle marks the Second
Philippic in pre-publication pamphlet form. Worth a sustained
corpus-level note on these two parallel literary projects
through November 44.
\item \textbf{The Att.\ 16.11 Heraclitus B49 \textit{heis emoi
murioi} citation.} ``One man is to me ten thousand'' --- the
philosophical-justification fragment Cicero deploys to make his
political stance bear weight. High-certainty allusion-sidecar
entry candidate for the Heraclitus fragment.
\item \textbf{The Att.\ 16.13 doubled Odyssey 3 citations
(\textit{dolichon ploon hormainonta}, \textit{par' \=enemoenta
Mimanta}).} Two phrases from \textit{Odyssey} 3.169--172 in the
same letter --- Cicero's epistolary citation habit at its densest.
Worth a translator-note on Cicero's distinctive Homeric
mosaic-citation style and an allusion-sidecar entry for both.
\item \textbf{The Att.\ 16.14 \textit{avi tui pronepos
\ldots aedem Opis explicaturum} family riddle.} ``Your
grandfather's great-grandson writes to my father's grandson\ldots
will open the temple of Ops.'' The Roman-family identification
that was transparent to Atticus is now opaque; preserved
literally with a flag in the headnote. Worth a translator-note
on the unrecoverable referent.
\item \textbf{The Att.\ 16.15 \textit{m\=ede s\=othei\=en hypo ge
toioutou} ``may I never be saved by the likes of him''
outburst against Octavian.} Bitterly ironic given the Second
Triumvirate proscriptions a year later that proscribe and kill
Cicero. Worth the most sustained translator-note in the cluster
on Cicero's missed reading of the young heir.
\item \textbf{The Att.\ 16.15 \textit{Stratullax} comic-soldier
applied to Antony.} The obscure comic-stage type (perhaps from a
lost Plautine play) applied to Antony as a strutting-soldier
caricature. Worth a glossary-realia note on the Stratullax type
and its application.
\item \textbf{The Att.\ 16.16 Perseus-TEI truncation versus modern
composite editions.} A corpus-level note on the discrepancy
between Perseus's brief cover-note and the standard Shackleton
Bailey / Tyrrell--Purser composite of 16.16 + 16.16A--E. Worth
flagging in the manifest so the reader of the bound volume sees
the editorial scope.
\end{itemize}

\textbf{Suggested next translation batch} (when session 23 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 23:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice U opening: \textit{Ad Familiares} 10 to
Plancus.} With the Atticus correspondence drafted complete
through 9 December 44 BC, the chronologically next active
sub-sequence is \textit{Fam.} 10, the Plancus correspondence
covering September 44 BC through 43 BC --- Cicero's epistolary
campaign to keep L. Munatius Plancus loyal to the Senate during
the Mutina campaign. About 24 letters, parallel-dispatchable at
3--4 per worker. \textit{Fam.} 10.1 (Romae, 19 September 44 BC,
to Plancus) is the chronologically next pending letter.
\item \textbf{Slice S (the chronological-gap sweep, 115 pending
letters earlier than the new -0044-12-09 marker):} substantial
backlog --- the \textit{Att.} 13.36 metadata-followup (no Perseus
URL --- check whether it merges with 13.35 per Shackleton Bailey),
the two pending \textit{Att.} 13.15 and 13.18 placeholder stubs
(awaiting manual Latin from session 18), the remaining
\textit{Fam.} 5 sub-cluster (5.15--5.18, all 45 BC,
parallel-dispatchable), and the \textit{Fam.} 5.10a/5.10b split
work flagged in session 20. The 16.15 marker advance to 9 December
exposes some early-43 BC letters that may now sit above the marker.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item \textbf{Slice M (entity-stub enrichment):} the entity registry
still has $\sim$472 stub entries needing real summaries --- ripe
for an aggressive parallel pass.
\end{itemize}


\textbf{Translation state (post-Cowork-session-22):} 709 / 958
works drafted (\~74.0\%). \textbf{Latest drafted by deep chronology
advanced} from \textit{Ad Atticum} 15.8 (Tusculanum, 31 May 44 BC)
to \textit{Ad Atticum} 16.3 (Pompeianum, 17 July 44 BC) --- a
seven-week advance that walks the journey out of Tusculum through
Antium, the return to Tusculum, the Arpinum-and-Formiae detour,
and into the opening of \textit{Att.} 16's Puteoli/Pompeii July
sequence. \textbf{Session 22 drafted 24 letters in two parallel
waves (three workers in each wave)} --- the entire remaining
\textit{Att.} 15 cluster from 15.9 through 15.29 (21 letters; the
Tusculanum/Antium June 44 BC daily-letter sequence, including the
historically central 15.11 council-of-Antium letter where Cicero
sits in on Brutus, Cassius, Servilia, Porcia and Tertia debating
whether Brutus should accept the cura annonae, and the famously
out-of-order 15.13 from 25 October 44 BC bound by the manuscript
transmission into the June cluster) and the opening three letters
of \textit{Att.} 16 (16.1--16.3, Puteoli and Pompeii, 8--17 July
44 BC, including 16.1's joke ``could anything be more disgraceful
than `July' for Brutus?'' on the renamed Quinctilis/Iulius). The
chronological-gap warning now reports \textbf{118 pending works
dated earlier than the latest-drafted (15.13 at -0044-10-25)},
down from 130 immediately after wave-1 consolidation; the gap
metric jumped at the start of session 22 because 15.13's October
date became the new latest-drafted, exposing many previously-
above-marker letters; the closing 118 reflects the 24 drafted
this session minus the surface-exposure inflation.

\textbf{Cowork session 22 --- 24 letters drafted across two
parallel waves (six workers):}

\textbf{Wave 1 (3 workers, 12 letters --- the opening Att. 15
June daily-letter cluster):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 15.9--15.12, 4 letters,
2--10 June 44 BC, Tusculanum / Antium):} 15.9 (the Persian
Portico / Eurotas / Lacedaemon ekphrasis with two daggered cruxes
on \textit{legatoriam} and the Lacedaemon clause); 15.10 (the
\textit{Dionis legatio} allusion to Dio the Academic's humiliating
embassy under Ptolemy XII; date editorial choice 5 vs. 6 June
flagged); \textbf{15.11 (\textbf{the historically central
council-of-Antium letter}, the eye-witness report of the
Brutus/Cassius/Servilia/Porcia/Tertia conference debating
whether Brutus should accept the cura annonae or sail east; the
Euripidean \textit{Iphigeneia in Aulis} 956 tag \textit{h\=e
deur' hodos soi ti dynatai nyn, theoprope?} ``what does this
journey of yours hither avail you now, prophet?'' turned by
Cicero from Achilles-to-Calchas into self-address; one daggered
crux at \S2)}; 15.12 (Antium, the first substantial Ciceronian
portrait of the young Octavian's political schooling, four Greek
phrases including \textit{kat\=ech\=esei} ``indoctrination'' --- a
notably Greek-philosophical word for what is being done to him,
\textit{h\=er\=oas} ``heroes'' for the conspirators, and the
mock-tragic \textit{t\=onde aitian t\=on Brout\=on tis echei}
``one of the Bruti bears the blame for this'' applied to Decimus).
\item \textbf{Worker B (\textit{Att.} 15.13--15.16, 4 letters):}
\textbf{15.13 (Puteolanum, 25 October 44 BC --- the famously
out-of-place letter bound by the manuscript transmission into
the June cluster but actually four months later, after the
Philippics had begun); the first explicit announcement of
\textit{De Officiis} in composition --- \textit{philosophoumen
ta peri tou kath\=ekontos} ``we philosophize the proper
duties'' --- and the \textit{prosph\=onoumen} dedication phrase};
15.14 (Tusculanum, 27 June, \textit{synt\Vaxeis} and
\textit{mete\=oros} ``adrift''); 15.15 (Antium, the
\textit{animus/stomachus} courage-versus-spleen pun and two
daggered cruxes); 15.16 (Antium, very short, \textit{pepin\=omen\=os}
``elegantly'' and \textit{prokop\=e} ``progress'').
\item \textbf{Worker C (\textit{Att.} 15.17--15.20, 4 letters,
14--21 June 44 BC, Antium / Antium-to-Tusculum journey /
Tusculanum):} 15.17 (Antium, \textit{philostorg\=os} ``warm of
heart'' twice in one letter and \textit{eupin\=os} ``neatly
turned''; \textbf{date correction \mbox{-0044-06-13}
$\rightarrow$ \mbox{-0044-06-14} per Perseus
\textit{postridie Idus} = the 14th, not the Ides itself; also
location \texttt{in Antiati postr} $\rightarrow$ \texttt{in
Antiati} OCR-bleed; recipient \texttt{ATTlCO} $\rightarrow$
\texttt{ATTICO} lowercase-L typo}); 15.18 (the journey-back
letter, \textit{in itinere ex Antiati in Tusculanum}, the Latin
opens xvii Kal.\ but the dateline gives xvi K.\ Quint.\
--- editorial choice 16 June retained); 15.19 (\textit{erg\=odes
/ anekton} ``laborious / bearable'' antithesis,
\textit{schediasma} ``improvisation, off-the-cuff''); 15.20
(Tusculanum, the lobster-pot \textit{nassa} image preserved
literally, the elliptical \textit{di illi mortuo qui umquam
Buthrotum!} curse over the Buthrotum settler-land issue, and
the closing \textit{mea manu} ``in my own hand'' notice; section
2 absent from the Perseus text, preserved as-is).
\end{itemize}

\textbf{Wave 2 (3 workers, 12 letters --- the closing Att. 15
late-June/early-July cluster + the opening Att. 16 sub-cluster):}
\begin{itemize}
\item \textbf{Worker D (\textit{Att.} 15.21--15.24, 4 letters,
22--27 June 44 BC, Tusculanum):} 15.21 (the 400,000-sesterces
\textit{CCCC} financial notation and the bitter close
\textit{ecquem tu illo certiorem nebulonem?} ``did you ever
know a more thorough fraud than that fellow?''; three Greek
phrases \textit{epoch\=en} ``suspension,'' \textit{akerai\={o}s}
``without compromise,'' \textit{plous} ``voyage''); 15.22
(the \textit{noster Cytherius} Antony-and-Cytheris reference and
the tricolon of sceptic's questions culminating in
\textit{quousque ludemur?} ``how long shall we be played
with?''); 15.23 (Tusculanum, \textbf{location correction
\texttt{in Tusculano viW aut} $\rightarrow$ \texttt{in
Tusculano} OCR-bleed of date numerals \textit{vi aut vii} into
the location field}; the paradox opener \textit{mirifice torqueor,
sine dolore tamen} ``I am racked exceedingly, yet without pain'';
\textit{hypomn\=ema} ``memorandum''); 15.24 (very short, one
daggered crux on the toponym Brutus set out for ---
Lanuvium/Antium/Nesis conjectures).
\item \textbf{Worker E (\textit{Att.} 15.25--15.29, 5 letters,
29 June -- 6 July 44 BC, Tusculanum / Arpinum / Formiae):}
15.25 (very short, one daggered Olympia/mysteries syntax);
\textbf{15.26 (Arpinum, the political reading of Brutus's
\textit{ludi Apollinares} games as a public test of nerve;
\textit{pseudengraph\=oi} ``forged'' and \textit{atop\=otaton}
``most absurd''; section 4 daggered corrupt stretch around
Caerellia and an eighth-share inheritance)}; 15.27 (Arpinum,
\textit{H\=erakleideion} ``in the Heraclidean manner''
[Heraclides Ponticus's dialogue form], the Homeric \textit{aut\=ei
boulysei} ``at the ox-loosing'' [late afternoon] from
\textit{Iliad} 16.779 / \textit{Odyssey} 9.58 --- a high-certainty
allusion-sidecar candidate); 15.28 (very short, paired with 15.27
on the same courier same day); \textbf{15.29 (\textbf{date
correction \mbox{-0044-07-07} $\rightarrow$ \mbox{-0044-07-06}}
per Perseus \textit{prid.\ Non.\ Quint.}\ and the decisive
internal evidence at \S3 \textit{pridie quam hoc scribebam, id
est III Non.}\ ``the day before I was writing this, that is on
the 3rd before the Nones'' --- so writing-date = pridie Non.\ =
6 July; \textbf{location correction \texttt{in Formiano prict}
$\rightarrow$ \texttt{in Formiano} OCR-bleed of \texttt{prid.}\
into the location field}; five Greek phrases including
\textit{am\=echania} ``helplessness,'' \textit{speisasthai}
``to make a treaty,'' \textit{ebdelyttom\=en} ``I was
disgusted'')}.
\item \textbf{Worker F (\textit{Att.} 16.1--16.3, 3 letters,
8--17 July 44 BC, Puteoli / Pompeii --- \textbf{opening of Book
16, the last surviving book of the Atticus correspondence,
running July through early November 44 BC}):} \textbf{16.1
(Puteolanum, the renamed \textit{Quinctilis} $\rightarrow$
\textit{Iulius} joke ``could anything be more disgraceful than
`July' for Brutus?'' on Caesar's calendar rebrand, five Greek
phrases including \textit{l\=eros polus} ``much twaddle'' and
\textit{glischr\=os} ``pinchingly'', and two daggered cruxes)};
16.2 (Puteolanum, the \textit{H\=erakleideion} treatise progress
report and the metrically-accented quasi-versified close
\textit{dum modo doleant aliquid, doleant quidlibet} ``as long
as they suffer something, let them suffer whatever'' --- possibly
Naevius / Accius, unidentified, allusion-sidecar candidate;
\textit{eklogai} ``excerpts'' for the \textit{De Officiis}
material being drawn); 16.3 (Pompeianum, the
\textit{archetypon} ``the original itself'' / \textit{syntagma}
``treatise'' pair, and the embedded Ennian \textit{o Tite, si
quid} tag --- a Tite-praenomen pun playing on Atticus's name,
high-certainty Ennius \textit{Annales} allusion candidate).
\end{itemize}

\textbf{Date corrections and precision changes committed to
\texttt{meta/works.yaml} during session 22 (two date corrections
+ three location/recipient cleanups):}
\begin{itemize}
\item \textit{Att.} 15.17: date \mbox{-0044-06-13} $\rightarrow$
\mbox{-0044-06-14} day-precision (Perseus \textit{postridie Idus}
= the 14th, not the Ides itself).
\item \textit{Att.} 15.17: \texttt{location\_written} \texttt{in
Antiati postr} $\rightarrow$ \texttt{in Antiati} (OCR-bleed of
the dateline's \textit{postridie}).
\item \textit{Att.} 15.17: \texttt{recipient} \texttt{ATTlCO}
$\rightarrow$ \texttt{ATTICO} (lowercase-L for I typo).
\item \textit{Att.} 15.16: \texttt{location\_written} \texttt{in
Antiati iii aut} $\rightarrow$ \texttt{in Antiati} (OCR-bleed of
date numerals \textit{iii aut} into the location field).
\item \textit{Att.} 15.23: \texttt{location\_written} \texttt{in
Tusculano viW aut} $\rightarrow$ \texttt{in Tusculano} (OCR-bleed
of date numerals \textit{vi aut vii} into the location field).
\item \textit{Att.} 15.29: date \mbox{-0044-07-07} $\rightarrow$
\mbox{-0044-07-06} day-precision (Perseus \textit{prid.\ Non.\
Quint.}\ and decisive \S3 internal evidence).
\item \textit{Att.} 15.29: \texttt{location\_written} \texttt{in
Formiano prict} $\rightarrow$ \texttt{in Formiano} (OCR-bleed of
\textit{prid.}\ from the dateline). No file rename needed under
either reading; the \texttt{044bc-} prefix remains correct.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The Att.\ 15.11 \textit{h\=e deur' hodos soi ti
dynatai nyn, theoprope?} (Euripides, \textit{Iphigeneia in
Aulis} 956) self-redeployment.} The line Achilles flings at
Calchas the prophet --- ``what does this journey of yours hither
avail you now?'' --- Cicero turns into a self-question after the
council of Antium fails to clarify Brutus's course. Worth a
corpus-level translator-note both for the Euripidean
identification and for the move from prophet-figure to
political-actor-figure.
\item \textbf{The Att.\ 15.12 portrait of the young Octavian's
political \textit{kat\=ech\=esis}.} Cicero's first substantial
portrait of Octavian's schooling under the Caesarian veterans
deploys \textit{kat\=ech\=esei} --- a markedly Greek-philosophical
word for ``indoctrination / oral instruction'' usually applied
to Stoic or Epicurean catechesis. Cicero is reading the young
heir as a philosophical-pupil-in-formation; the political
implications are sharp and the word-choice doctrinal. Worth a
sustained corpus-level translator-note.
\item \textbf{The Att.\ 15.13 \textit{De Officiis}-in-composition
announcement.} The October-25 dating places this letter four
months later than the surrounding June cluster, and the line
\textit{philosophoumen ta peri tou kath\=ekontos.\
prosph\=onoumen} ``we philosophize the proper duties.\ we
dedicate'' is the first explicit notice of \textit{De Officiis}
under composition --- a corpus-level hinge.
\item \textbf{The Att.\ 15.20 \textit{di illi mortuo qui umquam
Buthrotum!} curse.} The elliptical imprecation against
``whichever dead man'' first proposed the Buthrotian land seizure
preserves the depth of Cicero's frustration with the
veteran-settler programme; the referent (likely a Caesarian
veteran or settler) is unrecoverable. Worth a translator-note
on the ellipsis and a glossary note on the Buthrotum issue.
\item \textbf{The Att.\ 15.27 \textit{aut\=ei boulysei} Homeric
quotation.} High-certainty allusion to \textit{Iliad} 16.779 /
\textit{Odyssey} 9.58 (``at the ox-loosing,'' i.e.\ late
afternoon when oxen are unyoked) --- the more colloquial of
Cicero's Homeric phrase-borrowings. Worth a future allusion-
sidecar entry.
\item \textbf{The Att.\ 16.1 \textit{Iulius}-Quinctilis joke
``could anything be more disgraceful than `July' for Brutus?''}
The renaming of \textit{Quinctilis} (the fifth month) to
\textit{Iulius} after Caesar makes the proper time-marking of
Brutus's \textit{ludi Apollinares} into a political offence;
holding the games in ``July'' rather than \textit{Quinctilis}
silently endorses the Caesarian-calendar rebrand. Worth a
sustained translator-note both on the punning sharpness and on
the corpus-wide question of how Cicero handles month-names in
post-Ides letters.
\item \textbf{The Att.\ 16.2 quasi-versified close \textit{dum
modo doleant aliquid, doleant quidlibet}.} The metrically-
accented phrasing in Perseus suggests a versified citation,
possibly from Naevius or Accius, but unidentified. Worth flagging
as an open allusion-sidecar candidate.
\item \textbf{The Att.\ 16.3 \textit{o Tite, si quid} Ennian
tag.} The high-certainty Ennius \textit{Annales} tag turns on
Atticus's praenomen Titus --- ``O Titus, if anything\ldots''
The vocative play between epic-fragment and personal address is
one of Cicero's recurring Ennian moves; worth a corpus-level
note on the recurrence pattern.
\end{itemize}

\textbf{Suggested next translation batch} (when session 22 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 22:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T continuation: \textit{Att.} 16.4 onward
through 16.16.} Book 16 continues with thirteen more letters
(16.4--16.16), from late-July through early November 44 BC,
covering Cicero's aborted Greek voyage, the return to Rome, the
beginning of the Philippics confrontation with Antony, and the
final close of the Atticus correspondence. Short-to-medium
letters, ideal for parallel dispatch at 3--4 per worker. This
is the natural Slice T continuation and the chronologically
most-current sequence.
\item \textbf{Slice S (the chronological-gap sweep, 118 pending
letters earlier than the new -0044-10-25 marker):} substantial
backlog --- the \textit{Att.} 13.36 metadata-followup (no Perseus
URL --- check whether it merges with 13.35 per Shackleton
Bailey), the two pending \textit{Att.} 13.15 and 13.18
placeholder stubs (awaiting manual Latin from session 18), the
remaining \textit{Fam.} 5 sub-cluster (5.15--5.18, all 45 BC,
parallel-dispatchable), and the \textit{Fam.} 5.10a/5.10b split
work flagged in session 20.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}. None advanced
this session.
\item \textbf{Slice V continuation: the Paetus 45 BC tail.} Only
\textit{Fam.} 9.24 (February 43 BC) and \textit{Fam.} 9.25
(placeholder, no usable Latin) remain in book 9 pending.
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has $\sim$472 stub entries needing real summaries
--- ripe for an aggressive parallel pass.
\end{itemize}


\textbf{Translation state (post-Cowork-session-21):} 685 / 958
works drafted (\~71.5\%). \textbf{Latest drafted by deep chronology
advanced} from \textit{Ad Atticum} 14.9 (Cumanum, 17 April 44 BC)
to \textit{Ad Atticum} 15.8 (Tusculanum, 31 May 44 BC) --- a
six-week advance that walks the post-Ides itinerary forward from
Cumae through Puteoli, the Pompeianum, the Vescinum, Arpinum, and
into the Tusculan villa where the May daily-letter sequence
settles. \textbf{Session 21 drafted 21 letters in two parallel
waves (three workers in wave 1, two in wave 2)} --- the entire
remaining post-Ides \textit{Att.} 14 cluster from 14.10 through
14.22 (13 letters; the Cumanum/Puteolanum/Pompeianum journey-north
sequence of April--May 44 BC, including the famously out-of-order
14.15 dated K. Mart.\ celebrating Dolabella's tearing-down of the
altar/column at Caesar's funeral-pyre site and crucifying the
false-Marius pretenders), and the opening \textit{Att.} 15
sub-cluster 15.1--15.8 (Puteolanum through Vescinum, Arpinum, and
Tusculanum, 17--31 May 44 BC, including 15.1's death of the
doctor Alexio, 15.4's \textit{me Idus Martiae non delectant} ``the
Ides of March do not delight me'' / \textit{excisa enim est arbor,
non evulsa} ``the tree was cut down, not torn up by the roots''
retraction --- the sharpest single recantation of the assassination
in the corpus --- and 15.6's rare embedded verbatim
\textit{Hirtius Ciceroni} sub-letter). The chronological-gap
warning is now \textbf{89 pending works dated earlier than the
latest-drafted} (up from 84 at the end of session 20; the small
net increase reflects the six-week advance into late May exposing
additional earlier-pending letters that were previously above the
marker).

\textbf{Cowork session 21 --- 21 letters drafted across two
parallel waves (five workers):}

\textbf{Wave 1 (3 workers, 13 letters --- the closing Att. 14
post-Ides journey-north sequence):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 14.10--14.13, 4 letters,
19--26 April 44 BC, Cumanum / Puteoli):} 14.10 (Cumanum,
\textit{g\=en pro g\=es} ``one land after another,''
\textit{hyp\=enemios} ``wind-borne,'' and the daggered crux \dag\
\textit{rixothemin} \dag\ probably encoding a quarrel with
Antony); 14.11 (\textit{akolasian} ``licence''); 14.12 (Puteoli,
the truncated tragic tag \textit{ubi nec Pelopidarum, inquit}
``where neither the Pelopidae's name . . .,'' source uncertain
in the Accius/Ennius range); 14.13 (the substantial Antony-letter
reply, with two Homeric quotations --- \textit{Iliad} 9.228--230
adapted as \textit{all' ou daitos erat\=es erga mem\=elen} ``but
the works of the loved banquet have not been our care,'' and
\textit{Iliad} 5.428--429 with the famous Ciceronian
re-pointing of \textit{logoio} for \textit{gamoio} --- Aphrodite's
instruction to leave war for marriage becomes leave war for
speech).
\item \textbf{Worker B (\textit{Att.} 14.14--14.17, 4 letters, 27
April / 1 March / 3--4 May 44 BC):} 14.14 (Cumanum, the
obelised \dag\ \textit{Pherionum more} \dag\ ``Pherionian
fashion'' --- conjectured ``ferryman's'' or a proper-name corruption ---
and the \textit{Brutorum / brutorum} ``Bruti's / brutes'' pun);
\textbf{14.15 (Cumanum, the famously out-of-order K.\ Mart.\ =
1 March 44 BC letter)}, \textit{o mirificum Dolabellam meum!}
celebrating Dolabella's punitive demolition of the altar/column
at Caesar's funeral-pyre site and the punishment of the
false-Marius pretenders \textit{de saxo, in crucem} ``from the
rock --- to the cross''; 14.16 (Puteolanum / hortis Cluvianis,
\textit{aristeian}, \textit{anathe\=or\=esis}, \textit{kata
miton} ``thread by thread,'' and the \textit{tyrotarichum}
``cheese-and-salt-fish'' Paetus-table comic shorthand); 14.17
(Pompeianum, \textit{anekdoton} ``unpublished'' --- the suppressed
political memoir, identity debated between \textit{De Gloria} and
the lost \textit{Secret History} --- and the striking observation
that ``things could be said less dangerously with the tyrant
alive than with him dead'').
\item \textbf{Worker C (\textit{Att.} 14.18--14.22, 5 letters,
9--14 May 44 BC, Pompeianum / Puteolanum):} 14.18 (the locus
desperatus \dag\ \textit{suspendiatus est} \dag\ in \S2
preserved); 14.19 (Pompeianum, the corrupt \dag\ \textit{aritia}
\dag\ in \S1 and \textit{praxin} ``exploit'' twice in \S5); 14.20
(Puteolanum, the rare Atilius iambic-septenarius fragment
\textit{suam quoique sponsam, mihi meam} ``to each his own bride,
mine to me,'' \textit{katholikon the\=or\=ema} ``general
theorem,'' and the teasing \textit{m\=e} near-blasphemy against
Epicurus); 14.21 (Puteolanum, the cluster's densest Greek-phrase
letter --- \textit{huposolokia}, \textit{bebi\=otai},
\textit{pentel\=opion}, \textit{l\=eros polus}, four in one short
letter --- plus the embedded iambic-feel epigram \textit{hoc
metuere, alterum in metu non ponere}); 14.22 (Puteolanum, the
Sophoclean tragic-iambic fragment \textit{allois en esthlois
tond' ap\=othountai psogon} ``in other goods men shake off this
reproach,'' attributed by editors to the lost \textit{Erigone},
plus four Greek phrases including \textit{phainopros\=op\=eteon}
``one must put on a brave face'' and \textit{iteon} ``one must
go,'' the cluster's clearest Stoic-flavoured imperative).
\end{itemize}

\textbf{Wave 2 (2 workers, 8 letters --- the opening Att. 15
sub-cluster 17--31 May 44 BC):}
\begin{itemize}
\item \textbf{Worker D (\textit{Att.} 15.1--15.4, 4 letters, 17,
18, 22, 24 May 44 BC):} 15.1 (Puteolanum, \textbf{the death of
the doctor Alexio}, \textit{ouden} and \textit{to ek toutou}; the
daggered \dag\ \textit{attinet} \dag\ in \S2 and the embedded
comic-iambic verse \textit{quid est aut\'em cur ego pers\'onatus
amb\'ulem?} ``why am I to be the one walking around in a mask?'',
possibly from a lost togata); 15.2 (Vescinum, the corrupt
\textit{pentel\=oipon} ``five-remaining points'' rendered by
surface sense; two daggered Latin loci preserved); \textbf{15.3
(Arpinati, \textbf{date correction committed} from works.yaml's
\mbox{-0044-06-01} to \mbox{-0044-05-22}, Perseus dateline
\textit{in Arpinati xt K.\ Iun.} restored conventionally as
\textit{xi K.\ Iun.} = 22 May, with the May-22 placement
consistent with the manuscript order; location field also
trimmed from ``in Arpinati xt'' to ``in Arpinati''); 15.4
(Arpinati, \textbf{the corpus's sharpest single Ides-of-March
retraction} \textit{me Idus Martiae non delectant. nihil enim
nisi quod illud lubet . . . excisa enim est arbor, non evulsa}
``the Ides of March do not delight me . . .\ for the tree was
cut down, not torn up by the roots,'' plus five Greek phrases
\textit{an\=o}, \textit{aporia}, \textit{mel\=esei},
\textit{parencheir\=esis}, \textit{H\=erakleideion}; daggered
\dag\ \textit{aps condoleo} \dag\ in \S1 preserved by ellipsis).}
\item \textbf{Worker E (\textit{Att.} 15.5--15.8, 4 letters,
27--31 May 44 BC, Tusculanum):} 15.5 (the Cassius-Hirtius letter
opening with the daggered Greek proverb \dag\ \textit{ho
th\=esauros anthrakes} \dag\ ``the treasure is coals,'' Cicero's
mordant Hellenistic-comic shorthand for hopes turning worthless,
deployed for Cassius's request that Cicero use his influence with
Hirtius); \textbf{15.6 (the rare embedded sub-letter --- 15.6
\S2 reproduces verbatim Hirtius's reply \textit{HIRTIVS CICERONI
suo salutem}, not a Brutus/Cassius edict-reply; the
\textit{vesperi} dateline confirms 27 May evening per works.yaml)};
15.7 (very short, no \ciceroSection markers in the Latin,
rendered as single paragraph; the archaic-litigation idiom
\textit{ex iure manum consertum} ``laying-hands-on by formula of
law'' --- the technical opening of a property-suit before the
magistrate --- preserved with a translator-notes candidate on the
Servius jab depending on the formula being only the
\textit{opening} move); 15.8 (the closing \textit{Att.} 15
sub-cluster letter, two daggered Latin passages in \S2 plus the
manuscript slip \textit{K.\ Mart.} for \textit{K.\ Iun.} restored
silently to ``the Kalends of June'').
\end{itemize}

\textbf{Date corrections and precision changes committed to
\texttt{meta/works.yaml} during session 21 (one entry):}
\begin{itemize}
\item \textit{Att.} 15.3: \mbox{-0044-06-01} day-precision
$\rightarrow$ \mbox{-0044-05-22} day-precision per Perseus
\textit{in Arpinati xt K.\ Iun.} (corrupt \textit{xt} restored
conventionally as \textit{xi} = 11 K.\ Iun.\ = 22 May), with the
May-22 placement consistent with the manuscript order between
15.2 (18 May) and 15.4 (24 May). \texttt{location\_written} also
trimmed from ``in Arpinati xt'' to ``in Arpinati'' (the ``xt''
was OCR-bleed of the date numeral into the location field). The
\texttt{044bc-} file-prefix is correct under either reading; no
rename needed.
\end{itemize}

\textbf{Other date / text observations (flagged but not corrected
this session):}
\begin{itemize}
\item \textit{Att.} 14.19: Perseus dateline \textit{i Id.\ Mai.}
literally = pridie Idus = 14 May; works.yaml carries
\mbox{-0044-05-15} (Idibus). Preserved per conventional editorial
choice; defer to Shackleton Bailey. The ``vh'' in
\texttt{location\_written} (``in Pompeiano vh'') is OCR-noise and
should be trimmed in a future cleanup.
\item \textit{Att.} 15.6: Perseus dateline \textit{vi K.\ Iun.\
vesperi} = 27 May evening; works.yaml's \mbox{-0044-05-27} is
already correct (the launch prompt's tentative ``28 May'' was
wrong).
\item \textit{Att.} 15.7: Perseus dateline \textit{v aut iv K.\
Iun.} = 28 or 29 May; works.yaml takes 29 May per editorial
choice, retained.
\item \textit{Att.} 15.8 \S1: the Latin reads \textit{K.\ Mart.}
where context plainly wants \textit{K.\ Iun.}\ --- a manuscript
slip silently restored to ``the Kalends of June'' in the English.
Worth a future translator-notes entry.
\item Multiple daggered cruxes preserved with \dag\ markers:
14.10 \dag\ \textit{rixothemin} \dag, 14.14 \dag\
\textit{Pherionum more} \dag, 14.18 \dag\ \textit{suspendiatus
est} \dag, 14.19 \dag\ \textit{aritia} \dag, 15.1 \dag\
\textit{attinet} \dag, 15.2 multiple, 15.3 \dag\ \textit{malo}
\dag\ and \dag\ \textit{A.\ M.\ C.} \dag, 15.4 \dag\ \textit{aps
condoleo} \dag, 15.5 \dag\ \textit{ho th\=esauros anthrakes}
\dag, 15.8 \dag\ \textit{id quidem mihi videbatur} \dag\ and
\dag\ \textit{ut ille que} \dag. All preserved in body with
daggers and flagged in parallel-JSON notes; aggregate
translator-notes worth a corpus-level pass.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The Att.\ 14.13 Homeric re-pointing
(\textit{logoio} for \textit{gamoio}).} Cicero's substitution of
\textit{logoio} (``of speech'') for the Homeric \textit{gamoio}
(``of marriage'') in \textit{Iliad} 5.428--429 --- Aphrodite's
instruction to Helen to leave the works of war for the works of
marriage becomes Cicero's self-instruction to leave the works of
war for the works of speech --- is one of the corpus's sharpest
single Homeric reapplications and a doctrinal hinge for the
April-44 letters' negotiation of the post-Ides political
withdrawal.
\item \textbf{The Att.\ 14.15 Dolabella-and-the-pyre-altar
celebration as out-of-order chronology.} The K.\ Mart.\ =
1 March 44 BC dating, two weeks before the Ides, sits the letter
chronologically before the Ides cluster but in manuscript order
after the late-April letters because of the manuscript
transmission. The \textit{de saxo, in crucem} asyndeton
compresses the Tarpeian Rock and crucifixion into a single tight
construction --- the punitive register Dolabella adopted against
the false-Marius pretenders, and one of the clearest single
windows onto Cicero's brief Dolabellan enthusiasm before the
April-May letters' disillusionment.
\item \textbf{The Att.\ 14.17 \textit{anekdoton} ``unpublished''
reference as a corpus-level question.} The identity of the
suppressed political work referenced as \textit{anekdoton} ---
debated between \textit{De Gloria} and the lost
\textit{Secret History} --- is a sustained scholarly crux.
Worth a corpus-level note when the apparatus pass runs.
\item \textbf{The Att.\ 14.17 political-register line
\textit{minore periculo \ldots\ vivo tyranno dici potuisse quam
mortuo} ``things could be said less dangerously with the tyrant
alive than with him dead.''} One of the cluster's sharpest single
post-Ides political observations and a candidate for the
volume's chosen pull-quote for the April-44 sequence.
\item \textbf{The Att.\ 14.21 epigram \textit{hoc metuere,
alterum in metu non ponere}.} A rhythmical iambic-feel line in
the manuscripts (some editors print it with metrical accents),
possibly Cicero's own off-the-cuff iambics rather than a
quotation. Worth a sustained translator-notes entry on the
quotation-vs.-own-coinage question.
\item \textbf{The Att.\ 14.22 Sophoclean fragment \textit{allois
en esthlois tond' ap\=othountai psogon} ``in other goods men
shake off this reproach.''} Attributed by editors to the lost
Sophoclean \textit{Erigone}; rendered as a tidy English clause
inside quotation marks. Worth a future allusion-sidecar entry
when that pass runs.
\item \textbf{The Att.\ 15.4 \textit{me Idus Martiae non
delectant. \ldots\ excisa enim est arbor, non evulsa} retraction
as the corpus's sharpest single Ides-of-March recantation.} The
tree-image antithesis (cut down vs.\ torn up by the roots) is
the doctrinal hinge of Cicero's May-44 disillusionment with the
assassination's incompleteness; the rendering ``the tree was cut
down, not torn up by the roots'' preserves the violent extraction
the verb \textit{evellere} insists on. Worth a sustained
corpus-level translator-note both for the rhetorical figure and
for the historical pivot.
\item \textbf{The Att.\ 15.5 \dag\ \textit{ho th\=esauros
anthrakes} \dag\ ``the treasure is coals.''} The Hellenistic-
comic proverb (the tale of digging up a buried treasure to find
only ashes) is mordantly redeployed for Cassius's request that
Cicero use his influence with Hirtius. Worth a translator-note
on the proverb's Aesopian / New-Comedy provenance and Cicero's
choice to wield it in Greek rather than render it in Latin.
\item \textbf{The Att.\ 15.6 \textit{Hirtius Ciceroni} embedded
sub-letter.} One of the rare passages in the entire
correspondence where Hirtius's voice survives verbatim; the
\textit{vesperi} timestamp gives the May-27 evening more granular
detail than usual. Worth a corpus-level note for the doctrinal
weight of Hirtius's words as transmitted by Cicero.
\item \textbf{The Att.\ 15.7 \textit{ex iure manum consertum}
formula as the Servius-jab's load-bearing detail.} The technical
opening-of-a-property-suit formula has to be heard as the
\textit{opening} move, not the substantive proceeding, for the
Servius jab ``not in the formula but in what follows from it''
to land. Worth a glossary note on the formula and a separate
translator-note on the rendering.
\end{itemize}

\textbf{Suggested next translation batch} (when session 21 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 21:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T continuation: \textit{Att.} 15.9 onward
through 15.20 or so.} The Tusculanum daily-letter cluster
continues through early-to-mid June 44 BC, all short letters,
ideal for parallel dispatch at 4--5 letters per worker; this is
the densest single concentration in book 15.
\item \textbf{Slice S continuation (the chronological-gap sweep,
89 pending letters earlier than the new -0044-05-31 marker):}
the \textit{Att.} 13.36 metadata-followup (no Perseus URL ---
check whether it merges with 13.35 per Shackleton Bailey), the
two pending \textit{Att.} 13.15 and 13.18 placeholder stubs
(awaiting manual Latin from session 18), the remaining
\textit{Fam.} 5 sub-cluster (5.15--5.18, all 45 BC,
parallel-dispatchable), and the \textit{Fam.} 5.10a/5.10b split
work flagged in session 20.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}. None advanced
this session.
\item \textbf{Slice V continuation: the Paetus 45 BC tail.}
Only \textit{Fam.} 9.24 (February 43 BC) and \textit{Fam.} 9.25
(placeholder, no usable Latin) remain in book 9 pending.
\item \textbf{Slice P (post-session metadata follow-up):} resolve
\textit{Fam.} 5.10a/5.10b split (supply Latin from Shackleton
Bailey); investigate \textit{Att.} 13.36's missing Perseus URL;
trim the OCR-noise ``vh'' from \textit{Att.} 14.19's
\texttt{location\_written}; consider \texttt{fetch\_latin.py}
scrub for the trailing OCR-bleed of date numerals into location
fields (\textit{Att.} 15.3's ``in Arpinati xt'' was the second
such instance found this session).
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has $\sim$472 stub entries needing real summaries
--- ripe for an aggressive parallel pass.
\end{itemize}


\textbf{Translation state (post-Cowork-session-20):} 664 / 958
works drafted (\~69.3\%). \textbf{Latest drafted by deep chronology
advanced} from \textit{Ad Familiares} 6.17 (Latium, mid-April 44
BC) to \textit{Ad Atticum} 14.9 (Cumanum, 17 April 44 BC) --- a
two-day advance that consolidates the early-post-Ides itinerary
from Matius's suburban villa through Tusculum, Lanuvium, Astura,
Fundi, Formiae, Sinuessa, and into Cumae. \textbf{Session 20
drafted 29 letters in two parallel waves (four workers in wave 1,
two in wave 2)} --- the entire remaining \textit{Att.} 13 cluster
from 13.37 through 13.52 (16 letters; Tusculanum daily-letter
sequence early-to-mid August 45 BC plus the December 45 BC
Puteolanum coda including 13.52's famous record of Caesar's
\textit{epistathmeia} visit on 19 December), the first nine
post-Ides \textit{Att.} 14 letters (14.1--14.9, 7--17 April 44
BC, the journey-south sequence opening with Matius's
``everything is in confusion'' opener), and four 45 BC Vatinius
and Lucceius letters (\textit{Fam.} 5.9, 5.11, 5.13, 5.14, the
post-Tullia consolation cluster plus the Vatinius supplicatio
campaign). The chronological-gap warning is now \textbf{84
pending works dated earlier than the latest-drafted} (down from
108 at the end of session 19; net -24, reflecting the 29
in-cluster letters drafted minus the 5 letters whose dates were
already earlier than 6.17).

\textbf{Cowork session 20 --- 29 letters drafted across two
parallel waves (six workers):}

\textbf{Wave 1 (4 workers, 20 letters --- the closing Att. 13
August/December cluster + the opening Att. 14 post-Ides days):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 13.37--13.42, 6 letters,
2--9 August + late December 45 BC):} 13.37 (\textit{axiopistos},
\textit{phoberon an en}, \textit{anemophoreta}; daggered crux
\dag\ \textit{x x x x} \dag\ around an Epirote name in \S1; the
plain admission of political quietism under Caesar worth a
translator-note); 13.38 (\textit{ouk epestesen},
\textit{poteron e skoliais apatais}, and the Pindar \textit{Nemean}
7.25 tag \textit{dicha moi noos atrekeian eipein} --- ``my mind
is divided on speaking the plain truth''); 13.39 (\textit{skolia},
the Phaedrus title \textit{peri Theon}; one bracketed crux in
\S2 where a second book title has dropped out); 13.40 (the
Parthenon-tableau letter, \textit{euangelia}, \textit{philotechnema},
\textit{kekepphomai}, \textit{ta hola}; two daggered cruxes in
\S1 and \S2 from heavy corruption); 13.41 (\textit{skoliais apatais}
recurring; the soldierly-comic \textit{commeatus} ``leave of absence''
at close); 13.42 (the long Cicero/Quintus father-and-son
confrontation dialogue, the daggered \textit{kai} dangling-Greek,
the \textit{me skordou} ``no garlic'' colloquial in-joke, and the
self-conscious aside ``I borrowed a little something from your style
of speaking: I said nothing''). \textbf{Date precision tightened
in JSON only:} 13.42 from works.yaml's mid-December
placeholder to Perseus \textit{ex.\ m.\ Dec.} ($\approx$ 28
December 45 BC) --- not committed to works.yaml pending Shackleton
Bailey check.
\item \textbf{Worker B (\textit{Att.} 13.43--13.47, 5 letters,
14--21 July + 11--13 August 45 BC):} 13.43 (one-section thank-you,
no Greek); 13.44 (one Greek phrase \textit{mnemonikon hamartema}
``slip of memory''; the cautious phrase \textit{pompa deterret} ``the
procession deters me'' carrying the political reticence about
Caesar's statue in the \textit{ludi}; date ambiguity 20/21 July
flagged but 21 retained); 13.45 (the auction-of-Cicero's-property
letter; \textit{currentem tu quidem} idiom for ``urging on a runner,''
expanded for clarity; one OCR artifact \texttt{XIII. xlv} bleed-through
from Perseus dropped from the English); 13.46 (the Pollex/index
thumb-pun preserved with parenthetical Latin gloss; \textit{HS iↃↃↃ}
= 50,000 sesterces rendered numerically; the famous Caesar reading
Brutus's \textit{Cato} ``and thinking himself eloquent'' line); 13.47
(\textit{edolavi} rendered ``roughed out'' to keep the
carpenter's-axe image; closing \textit{o magistrum molestum!} as
``what a tiresome schoolmaster!'' --- the joke being that Dolabella
is the declamation-pupil, so the master is the one finding his pupil
exhausting).
\item \textbf{Worker C (\textit{Att.} 13.48--13.52, 5 letters, 5--24
August + 19 December 45 BC):} 13.48 (the inheritance-fractions
letter, \textit{ex uncia / ex triente} rendered as Roman shares;
one Greek phrase \textit{alogos}; Perseus dateline garbled
\textit{t\%u Non.\ Sext.} flagged as OCR drift); 13.49 (one Greek
phrase \textit{mempsin anapherei}; closing antithesis
\textit{non omnibus dormire / observare servire est} preserved as
``not bound to sleep for everyone... not bound to dance attendance''); 
13.50 (no Greek; one long German-style period in \S1 reproduced
intact); 13.51 (\textit{pros ison homoion} ``to peer and equal,''
\textit{akolakeutos} ``without flattery''; \dag\ \textit{micillus}
\dag\ preserved as a daggered crux --- editors propose
\textit{Micyllus} the Lucianic cobbler or \textit{Mucius}; the
dagger preserves the question). \textbf{13.52, historically
loaded:} the \textbf{Caesar-at-Puteoli visit on 19 December 45
BC, the only surviving first-person record of Caesar dining with
Cicero}; \textbf{seven Greek phrases} in two sections including
the politically pointed pivot from Latin \textit{hospitium} (peer
guest-friendship) to Greek \textit{epistathmeia} (compulsory
military quartering) --- ``a piece of hospitality --- a billeting,
rather --- that was a burden to me, not a bother''; the exclamatory
\textit{o hospitem mihi tam gravem ametameleton!} rendered
``Oh, what a burdensome guest he was --- and yet I have no regrets''
(rather than the older ``burdensome but not regrettable'');
\textit{hominum ciↃ ciↃ} (Roman numeral CIↃ CIↃ = 2000) rendered
``two thousand men, no less.''
\item \textbf{Worker D (\textit{Att.} 14.1--14.4, 4 letters, 7--10
April 44 BC, the post-Ides retreat):} \textbf{14.1, historically
loaded:} the Matius opener letter, the three-hammer
\textit{nihil perditius; explicari rem non posse; ille gaudens}
rendered ``Nothing could be more lost; the thing cannot be untangled;
he said it, at any rate, with pleasure'' --- the trimeter-feel
preserved; Matius's grim relish kept as Matius's, not a third-party
qualification; Caesar's reported colloquy preserved in
double-quotes per existing convention; 14.2 (the cluster's
two-Greek-tag letter, \textit{phalakoma}/\textit{phalakroma}
``bald-pate'' doublet, the second the standard Attic form; two
daggered cruxes preserved \dag\ ... \dag; Perseus segmentation
skips \S3, preserved as a gap); 14.3 (the Pan-fright letter, four
Greek phrases \textit{panikon}, \textit{diathesin},
\textit{pragmatikon}, \textit{episemasian}; \textit{bellus
architectus} as ``a fine architect''); 14.4 (the
\textit{rem publicam reciperatam} grief-letter, one Greek phrase
\textit{heroes}; works.yaml correctly carries Lanuvium as
\texttt{location\_written}, matching Perseus \textit{Scr.\ Lanuvi
iv Id.\ Apr.\ a.\ 710 (44)} --- no correction needed).
\end{itemize}

\textbf{Wave 2 (2 workers, 9 letters --- Att. 14 continuation +
Fam. 5 gap-fill):}
\begin{itemize}
\item \textbf{Worker E (\textit{Att.} 14.5--14.9, 5 letters, 12--17
April 44 BC):} 14.5 (Astura, the signs/standards wordplay
\textit{signa bella ... non bona / cum signis} preserved as a
triple-pun; five Greek phrases \textit{esitesas},
\textit{mnemonikon hamartema}, \textit{phurmos polus},
\textit{euripista}, \textit{neoterismou}; Perseus dateline
\textit{Scr.\ Asturae it Id.\ Apr.} carries an OCR-typo ``it''
flagged but works.yaml 13 April retained); 14.6 (Fundi, the
\textit{politeuesthai}/\textit{soloikon}/\textit{pepoliteumetha}/
\textit{politikotera} four-word Greek cluster on the same root;
\textit{heroibus nostris} ``our heroes'' affectionate-ironic; the
12 April date is manuscript-order, genuinely earlier than 14.5's
13 April, preserved); 14.7 (Formiae, \textit{pepinomenai} and
\textit{pinos}; the \textit{quod in buccam venerit} idiom rendered
``whatever first comes to mind'' per STYLE.md's explicit example);
14.8 (Sinuessa, no Greek; the aposiopesis \textit{verum tamen---}
preserved as ``And yet ---''; the \textit{in actis esse nostris}
records/journal pun preserved); 14.9 (Cumae, the
\textit{vivit tyrannis, tyrannus occidit!} chiasm preserved as
``the tyranny lives, the tyrant fallen'' --- a candidate
translator-note; the Phaedo-style apostrophe
\textit{o Socrate et Socratici viri!} kept with stagy archaism;
the Pacorus / Caecilius Bassus / Volcatius Tullus / Vetus Syrian-
campaign passage preserved with bare names, prosopography deferred).
\item \textbf{Worker F (\textit{Fam.} 5.9 + 5.11 + 5.13 + 5.14, 4
letters, mid-March through end-October 45 BC, the post-Tullia
consolation cluster + Vatinius supplicatio):} \textit{Fam.} 5.9
(11 July 45 BC, \textbf{INCOMING from Vatinius IMP. at the camp
at Narona}, the supplicatio-angling letter; the
\textit{honor}/\textit{periculum} wordplay between Vatinius's
supplicatio campaign and his 54 BC trial preserved; one Greek-
derived term \textit{anagnostes} ``reader'' for the runaway
slave; the soldier's opening formula \textit{V.\ B.\ E.\ E.\ V.}
= ``If you are well, I am glad; I myself am well'' rendered
explicitly); \textit{Fam.} 5.11 (end of October 45 BC, Rome,
\textbf{OUTGOING from Cicero to Vatinius IMP.}, salutation
\textit{M.\ CICERO VATINIO IMP.\ S.} confirmed --- works.yaml's
\texttt{recipient: VATINIO IMP.} is correct, the prompt's
hypothesis about incoming direction was wrong; the jocular
\textit{duces eum captivum in triumpho} preserved literally as the
triumph-campaign joke); \textit{Fam.} 5.13 (mid-March 45 BC,
Astura or Atticus's Ficuleano, \textbf{Cicero TO L.\ Lucceius},
the grief-reply to Lucceius's consolation; \textit{praeceptorem
fortitudinis} rendered ``my teacher in bravery'' with the
half-smile intact since Cicero is the famous teacher in the
friendship; \textit{membra rei p.} kept as ``limbs of the
commonwealth''); \textit{Fam.} 5.14 (\textbf{9 May 45 BC, Rome,
INCOMING from L.\ Lucceius}, salutation
\textit{L.\ LVCCEIVS Q.\ F.\ M.\ TVLLIO M.\ F.\ S.}; the
soldier's-formula opener \textit{S.\ V.\ B.\ E.\ V.} with one V
dropped, rendered explicitly; the \S2 triple-anaphora
\textit{tu solus ... tu non intelleges ... non intelleges ...}
preserved as three parallel English questions; \textit{convictum
nostrum} rendered ``our company'' not ``conviviality'' --- the
false-cognate trap avoided). \textbf{Date correction committed
to works.yaml:} 5.14 date corrected from \mbox{-0045-05-15} to
\mbox{-0045-05-09} per Perseus \textit{vii Id.\ Mai.\ a.\ 709
(45)} = 9 May (counting inclusively); \texttt{location\_written}
also trimmed from ``Romae vii'' to ``Romae'' (the ``vii'' was OCR-
bleed of the dateline numeral into the location field).
\end{itemize}

\textbf{Date corrections and precision changes committed to
\texttt{meta/works.yaml} during session 20 (one entry):}
\begin{itemize}
\item \textit{Fam.} 5.14: \mbox{-0045-05-15} day-precision
$\rightarrow$ \mbox{-0045-05-09} day-precision per Perseus
\textit{vii Id.\ Mai.\ a.\ 709 (45)} = 9 May counting inclusively
(20 \texttt{vii} = 9, not 15). \texttt{location\_written} also
trimmed from ``Romae vii'' to ``Romae.''
\end{itemize}

\textbf{Other date observations (flagged but not corrected this
session):}
\begin{itemize}
\item \textit{Att.} 13.42: works.yaml carries month-precision
\mbox{-0045-12-15}; Perseus \textit{ex.\ m.\ Dec.\ a.\ 709 (45)}
= closing days of December, so ca.\ 28 December would be more
accurate. Left at month-precision for now; the parallel sidecar
JSON uses 28 December.
\item \textit{Att.} 13.44: Perseus \textit{xiii aut xii K.\ Sext.}
= 20 or 21 July; works.yaml's 21 July retained per conventional
editorial choice.
\item \textit{Att.} 13.45: Perseus Latin file carries an
apparatus-marker bleed-through \texttt{XIII.\ xlv} mid-sentence
(Perseus chapter-marker, not Cicero's text); dropped from the
English. Worth considering a \texttt{fetch\_latin.py} scrub for
\texttt{XIII\.\textbackslash s+xlv} patterns.
\item \textit{Att.} 13.48: Perseus dateline \texttt{t\%u Non.\
Sext.} is corrupted at the day numeral (probably percent-encoded
\textit{v} or \textit{iii}); works.yaml 5 August retained.
\item \textit{Att.} 14.5: Perseus dateline \textit{Scr.\ Asturae
it Id.\ Apr.\ a.\ 710 (44)} carries an OCR-typo ``it'' (for
\textit{iii} or \textit{Id.}); works.yaml 13 April retained per
conventional editorial choice. Body text's \textit{iii Idus} would
give 11 April; defer to Shackleton Bailey.
\end{itemize}

\textbf{Other metadata work and stub-creation this session:}
\begin{itemize}
\item \textit{Fam.} 5.10: Perseus's TEI book 5 jumps from 5.9 to
5.11; the Latin Library fallback dumped the whole book 5 file
($\sim$57\,KB) into \texttt{latin/letters/051bc-ad-familiares-05-10.tex}.
Overwritten with a placeholder stub explaining the situation. The
Latin Library splits 5.10 into ``Xa'' and ``Xb'' (which Shackleton
Bailey numbers as separate letters). The works.yaml entry currently
carries the wrong year (\mbox{-0051-07-01}) since 5.10 to Vatinius
is in fact a 45 BC letter in the Vatinius cluster, but 5.10a/5.10b
in SB are 51 BC letters from Cilicia. \textbf{Followup needed:}
decide whether to split the works.yaml entry into \texttt{ad-
familiares-05-10a} and \texttt{ad-familiares-05-10b}, and supply
the Latin from Shackleton Bailey (Loeb or Cambridge) manually.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The Caesar-at-Puteoli letter (\textit{Att.} 13.52)
as a corpus-level historical pivot.} The Latin
\textit{hospitium}/Greek \textit{epistathmeia} pivot is the
sharpest single political-register line in the 45 BC cluster
--- the moment Cicero codes Caesar's visit as not peer
guest-friendship but military quartering. Worth a sustained
corpus-level note both for the rhetorical move and for the
historical occasion (the only surviving first-person record of
Caesar dining with Cicero). The exclamatory ``Oh, what a
burdensome guest he was --- and yet I have no regrets'' is
chosen over the older ``burdensome but not regrettable'' on
exclamatory-accusative grounds.
\item \textbf{The Matius ``everything is in confusion'' opener
(\textit{Att.} 14.1) as the corpus's threshold to the post-Ides
world.} The three-hammer trimeter-feel
\textit{nihil perditius; explicari rem non posse; ille gaudens}
is the cluster's clearest single window onto the immediate
political mood. Worth a corpus-level note both for the rhetorical
construction and for what Cicero's ear hears in a Caesarian's
mouth on 7 April 44 BC.
\item \textbf{The \textit{vivit tyrannis, tyrannus occidit!}
chiasm (\textit{Att.} 14.9).} A two-clause four-word chiasm
that distinguishes the death of the tyrant from the survival of
the tyranny --- one of the sharpest single rhetorical figures
in the whole post-Ides cluster, and the doctrinal hinge of
Cicero's despair through April 44 BC. Worth a sustained
translator-note on the rendering ``the tyranny lives, the tyrant
fallen.''
\item \textbf{The Pindar \textit{Nemean} 7.25 tag (\textit{Att.}
13.38).} \textit{dicha moi noos atrekeian eipein} ``my mind is
divided on speaking the plain truth'' --- one of the densest
single-letter Pindaric allusions in the corpus. Worth flagging
in a future allusions-pass.
\item \textbf{The \textit{currentem tu quidem} idiom and the
Pollex/index pun.} Two diagnostic short-letter idiom cruxes
worth recording: \textit{currentem hortari} = ``urge on a runner''
(13.45); \textit{Pollex/index} thumb-pun (13.46). Both are the
sort of micro-decision the project's translator-notes apparatus
exists to capture.
\item \textbf{The Vatinius supplicatio campaign (\textit{Fam.}
5.9 + 5.11) as a structural exception.} 5.9 (incoming from
Vatinius) and 5.11 (Cicero's outgoing reply) bracket Vatinius's
mid-45-BC angling for a supplicatio honouring his Illyrian
campaign; the \textit{honor}/\textit{periculum} pun (5.9 \S1)
is the structural hinge.
\item \textbf{The post-Tullia Lucceius exchange (\textit{Fam.}
5.13--5.14) as a two-way consolation cluster.} 5.14 from
Lucceius (incoming, 9 May 45 BC) and 5.13 from Cicero
(outgoing reply, mid-March 45 BC --- the manuscript-order is
not chronological) form an exchange in the Servius Sulpicius
mode but with Lucceius as the addressee; the
\textit{praeceptorem fortitudinis} ``teacher in bravery'' line
in 5.13 is the doctrinal hinge.
\end{itemize}

\textbf{Suggested next translation batch} (when session 20 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 20:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T continuation: \textit{Att.} 14.10 onward
through 14.22, then 15.1 onward.} The post-Ides journey continues
through Cumae, Puteoli, and back toward Astura; 14.10--14.22 are
the densest single concentration in book 14, all short letters,
ideal for parallel dispatch at 4--5 letters per worker.
\item \textbf{Slice S continuation (the chronological-gap sweep,
84 pending letters earlier than the new -0044-04-17 marker):} the
\textit{Att.} 13.36 metadata-followup (no Perseus URL --- check
whether it merges with 13.35 per Shackleton Bailey), the two
pending \textit{Att.} 13.15 and 13.18 placeholder stubs
(awaiting manual Latin from session 18), the remaining
\textit{Fam.} 5 sub-cluster (5.15--5.18, all 45 BC,
parallel-dispatchable), and the \textit{Fam.} 5.10a/5.10b split
work flagged this session.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}. None advanced
this session.
\item \textbf{Slice V continuation: the Paetus 45 BC tail.}
Only \textit{Fam.} 9.24 (February 43 BC) and \textit{Fam.} 9.25
(placeholder, no usable Latin) remain in book 9 pending --- 9.24
moves the marker further forward into 43 BC if picked up early.
\item \textbf{Slice P (post-session metadata follow-up):} resolve
\textit{Fam.} 5.10a/5.10b split (supply Latin from Shackleton
Bailey); investigate \textit{Att.} 13.36's missing Perseus URL;
consider \texttt{fetch\_latin.py} scrub for the Perseus apparatus-
marker bleed-through (\texttt{XIII\.\textbackslash s+xlv} and
similar) found in 13.45.
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has $\sim$472 stub entries needing real summaries
--- ripe for an aggressive parallel pass.
\end{itemize}


\textbf{Translation state (post-Cowork-session-19):} 635 / 958
works drafted (\~66.3\%). \textbf{Latest drafted by deep
chronology advanced significantly} from \textit{Ad Familiares}
9.12 (Cumanum, late November 45 BC) to \textit{Ad Familiares} 6.17
(Latium, mid-April 44 BC) --- a 5-month forward jump into 44 BC,
crossing the Ides of March. \textbf{Session 19 drafted 16 letters
in four parallel workers} --- the remaining \textit{Att.} 13
mid-/late-May Tusculanum daily-letter run (\textit{Att.} 13.21,
13.26--13.35, 11 letters), the Lepta business note from Astura
(\textit{Fam.} 6.19), and the Pompeian-exile / post-Ides cluster
gap-fill (\textit{Fam.} 6.9 to Furfanius, plus the historic
\textit{Fam.} 6.15 to Basilus on the Ides of March itself, plus
the Bithynicus exchange \textit{Fam.} 6.16--6.17). The
chronological-gap warning is now \textbf{108 pending works dated
earlier than the latest-drafted} (vs.\ 106 at the end of session
18; the small net increase reflects the new 5-month advance
exposing additional earlier-pending letters that were previously
above the marker).

\textbf{Cowork session 19 --- 16 letters drafted across one
parallel wave (four workers):}

\textbf{Worker A (\textit{Att.} 13.21, 13.26--13.28, 4 letters,
mid-May / 1 June / 29 July 45 BC):}
\begin{itemize}
\item \textit{Att.} 13.21 (Astura, 29 July 45 BC, the
boxing-and-suspension Sceptic letter): two Greek phrases
\textit{epoch\=ei} (\textgreek{ἐποχῇ}, the Sceptic technical
``suspension of judgement,'' twice) and \textit{probol\=en}
(\textgreek{προβολὴν}, ``boxer's guard''); one daggered crux \dag\
\textit{esset certe ne} \dag\ in \S4 preserved; the
\textit{inhibere}/\textit{inhibitio} debate kept in italicized
Latin in the body since the whole section turns on the Latin verb
--- translator-note candidate.
\item \textit{Att.} 13.26 (Tusculanum, 14 May 45 BC, the
book-13-shelved earliest letter): no Greek; the allusive ``my
desire for the thing you know of'' (\textit{eius rei \ldots\ quam
nosti}) rendered without expansion --- the unspoken referent is
the search for a property for Tullia's shrine, supplied only in
the headnote.
\item \textit{Att.} 13.27 (Tusculanum, 25 May 45 BC, the
\textit{Cato}/\textit{Anticato} sop-letter): \textbf{six Greek
phrases} \textit{kolakeia}, \textit{epiteugma},
\textit{apoteugma}, \textit{parakinduneuein}, \textit{meiligma},
\textit{spoud\=e}; the \textit{Catonis} \textgreek{μείλιγμα}
rendered ``a sop to balance my Cato'' --- the polemic-and-reply
context (Cicero's \textit{Cato} and Caesar's \textit{Anticato})
flagged in the headnote.
\item \textit{Att.} 13.28 (Tusculanum, 1 June 45 BC, the
``letter-to-Caesar'' withdrawal, one of the cluster's most
historically loaded letters): one Greek phrase
\textit{probl\=ema Archid\=emou} (\textgreek{πρόβλημα Ἀρχιδήμου},
Stoic-dialectical ``Archidemus's puzzle''); the bitter
\textit{hunc de pompa Quirini contubernalem} ``this messmate of
Quirinus's procession'' preserved (the irony of Caesar's statue
carried with the gods); HS \overline{DCCC} = 800{,}000 sesterces
rendered numerically; \textit{hoc manu mea} preserved as ``This in
my own hand,'' the autograph-postscript marker. \textbf{Date
discrepancy flagged but NOT corrected:} Perseus dateline reads
\textit{Vii. K. Iun.} which by literal Roman count = 26 May, not 1
June; the editorial tradition's 1 June is preserved in works.yaml
pending a Shackleton Bailey check.
\end{itemize}

\textbf{Worker B (\textit{Att.} 13.29--13.32, 4 letters, 27--29
May 45 BC, Tusculanum):}
\begin{itemize}
\item \textit{Att.} 13.29 (27 May): two Greek phrases
\textit{aphidruma} (\textgreek{ἀφίδρυμα}, ``shrine'') and
\textit{ton typhon mou pros the\=on tropophor\=eson}
(\textgreek{τὸν τῦφόν μου πρὸς θεῶν τροποφόρησον}, ``in the gods'
name, bear with my vanity'' --- Cicero's Greek-coded request that
Atticus indulge his Tullia-shrine preoccupation); one daggered
crux \dag\ \textit{misissem} \dag\ in \S3.
\item \textit{Att.} 13.30 (28 May, the Mummius-commission
research letter): two Greek phrases \textit{kolakeiai}
(\textgreek{κολακεῖαι}, ``flatteries'') and \textit{politikon
syllogon} (\textgreek{πολιτικὸν σύλλογον}, ``political
assembly,'' the Dicaearchus dialogue-design framework). The
Mummian-commission prosopographical hunt (Polybius, Albinus,
Sp.\ Mummius, Tuditanus) opens here and resolves in 13.32. The
Perseus dateline string carries the orphan fragment ``post op
xxxi'' which appears to be a scribal marker; preserved in the
Latin file.
\item \textit{Att.} 13.31 (28 May, same dateline as 13.30): two
Greek phrases \textit{katabase\=os} (\textgreek{καταβάσεως}, ``of
the \textit{Descent},'' title of Dicaearchus's lost work) and
\textit{kekrika} (\textgreek{κέκρικα}, the Greek perfect ``I have
decided,'' marking settled judgement). HS \overline{CXV} =
11{,}500{,}000 sesterces rendered numerically. The ``letter to
Caesar'' (the suppressed advice-letter, the subject of 13.27 and
13.28's \textit{probl\=ema Archid\=emou}) referenced again ---
crossref candidate.
\item \textit{Att.} 13.32 (29 May, the cluster's
Mummius-commission resolution + Dicaearchus-shopping letter):
\textbf{six Greek phrases} \textit{peri psych\=es}
(\textgreek{περὶ ψυχῆς}, ``On the Soul,'' Dicaearchus title);
\textit{katabase\=os}; \textit{Tripolitikon} (book title);
\textit{dia s\=emei\=on} (\textgreek{διὰ σημείων}, ``in
shorthand''); \textit{syllogon}; \textit{pompeusai kai tois
pros\=opois} (\textgreek{πομπεῦσαι καὶ τοῖς προσώποις}, ``stage
our procession with the right cast/characters''). The
\textit{Catulus} and \textit{Lucullus} (earlier two-book
\textit{Academica}) and ``new prefaces'' crossref candidates
deferred to apparatus pass.
\end{itemize}

\textbf{Worker C (\textit{Att.} 13.33--13.35 +
\textit{Fam.} 6.19, 4 letters, early June to late August 45 BC):}
\begin{itemize}
\item \textit{Att.} 13.33 (3 June 45 BC, Tusculanum): three Greek
phrases \textit{dys\=opia} (\textgreek{δυσωπία}, ``embarrassment''),
\textit{katabase\=os}, \textit{eulogon}; \textbf{four daggered
cruxes} \dag\ \textit{H in Capitolio} \dag, \dag\ \textit{exspecto}
\dag\ (governing \textit{katabase\=os}), \dag\ \textit{vide etiam}
\dag, and \dag\ \textit{ea de} \dag\ preserved; a Perseus lacuna
\texttt{* * *} opens \S3.
\item \textit{Att.} 13.34 (27 July 45 BC, Astura, the brief
arrival note): no Greek; the very-short note (``arrived viii Kal.
in the evening; rested three hours at Lanuvium to avoid the
heat'') previewed of the gardens-and-Publilius business; the
``Publilio'' in the Latin is the masculine form (Publilia's
brother/agent), not Publilia herself --- preserved as ``the
business with Publilius.''
\item \textit{Att.} 13.35 (13 July 45 BC, Tusculanum, the
Pomponius-gentilis letter): no Greek; opening \textit{gentilis
tuus urbem auget} flagged in the headnote on the conventional
identification with a Caesarian Pomponius working on Caesar's
urban-renewal plans; treats 13.35 and 13.36 as separate letters
per Perseus's segmentation (Shackleton Bailey's reconstruction
merges them; deferred to a future enrichment pass).
\item \textit{Fam.} 6.19 (late August 45 BC, Astura, to Lepta on
the curatorship of Caesar's planned games): no Greek;
\textit{curatio aliqua munerum regiorum} rendered ``some sort of
curatorship of the royal games'' (\textit{munera regia} as
Caesar's planned spectacles, glossed in the headnote);
\textbf{date precision worth tightening:} works.yaml has month-
precision \mbox{-0045-08-15}; Perseus dateline \textit{ex.\ m.\
Sext.\ a.\ 709 (45)} = closing days of Sextilis, so ca.\ \mbox{-
0045-08-25} would be more accurate. Left at month-precision for
now.
\end{itemize}

\textbf{Worker D (\textit{Fam.} 6.9, 6.15, 6.16, 6.17, 4 letters,
December 46 BC through mid-April 44 BC, the post-Ides cluster):}
\begin{itemize}
\item \textit{Fam.} 6.9 to Furfanius Postumus (early December 46
BC, Rome, the Caecina recommendation): no Greek; the
\textit{cumulus} ``heaping-up'' image kept as the figure of the
letter and registered in the headnote; \textbf{date correction
committed:} \mbox{-0046-10-22} year-precision $\rightarrow$
\mbox{-0046-12-01} month-precision per Perseus dateline (the
OCR-garbled ``ica.\ in.\ Dee.\ a.\ 708 (46)'' resolved as
\textit{circa initium Decembris 708 (46)}); \texttt{location\_
written} also cleaned from ``Romae ica.\ in.\ Dee'' to
``Romae.''
\item \textit{Fam.} 6.15 to L.\ Minucius Basilus (\textbf{15
March 44 BC, Rome --- the Ides of March itself, to one of the
assassins}): no Greek; the entire letter is a single, tightly
chiastic sentence \textit{tibi gratulor, mihi gaudeo; te amo, tua
tueor; a te amari et quid agas quidque agatur certior fieri volo}
rendered preserving the six-clause sequence and the I/you
interlocking; \textit{quid agatur} rendered as the deniable
passive ``what is being done''; the historic date and the
chiastic structure registered in the headnote per the launch-
prompt's explicit requirement. \textbf{One of the most
historically remarkable single sentences in the corpus.}
\item \textit{Fam.} 6.16 from A.\ Pompeius Bithynicus
(\textbf{INCOMING --- the only incoming letter in this cluster},
late March 44 BC, in Sicily): no Greek; the salutation
\texttt{BITHYNICVS CICERONI S.} preserved as the marker that
this is the unusual incoming direction; \textit{intermoriturum}
in the closing clause rendered to keep the perfective-future
sense ``be allowed to die out''; the headnote registers
explicitly that the letter is Bithynicus to Cicero from Sicily.
\item \textit{Fam.} 6.17 to Bithynicus (mid-April 44 BC, in
Latio, Cicero's reply to 6.16): no Greek; the hinge antithesis
\textit{beneficiorum magnitudine} vs.\ \textit{necessitudine}
(``size of obligation'' vs.\ ``family tie'') preserved; the
Perseus transcription quirks ``a.\ 720 (44)'' = OCR typo for
``a.\ 710 (44)'' = 44 BC, and the apparent want of a final
\textit{vale}, both noted in the sidecar.
\end{itemize}

\textbf{Date corrections and precision changes committed to
\texttt{meta/works.yaml} during session 19 (one entry):}
\begin{itemize}
\item \textit{Fam.} 6.9: \mbox{-0046-10-22} year-precision
$\rightarrow$ \mbox{-0046-12-01} month-precision per Perseus
\textit{circa initium Decembris 708 (46)} (OCR garble ``ica.\
in.\ Dee.'' resolved). \texttt{location\_written} also trimmed
from ``Romae ica.\ in.\ Dee'' to ``Romae.'' The \texttt{046bc-}
file-prefix is correct under either reading; no rename needed.
\end{itemize}

\textbf{Other date observations (flagged but not corrected
this session):}
\begin{itemize}
\item \textit{Att.} 13.28: Perseus dateline \textit{Vii.\ K.\
Iun.\ a.\ 709 (45)} reads literally as 26 May; works.yaml's
day-precision \mbox{-0045-06-01} preserved per the editorial
tradition. Defer to a Shackleton Bailey consultation.
\item \textit{Att.} 13.30 and 13.31 share the dateline \textit{v
K.\ Iun.} = 28 May; works.yaml carries both as \mbox{-0045-05-28},
correct.
\item \textit{Fam.} 6.19: month-precision \mbox{-0045-08-15}
could be tightened to \mbox{-0045-08-25} per Perseus
\textit{ex.\ m.\ Sext.}; left as month-precision for now.
\item \textit{Fam.} 6.16 / 6.17: works.yaml month-precision
\mbox{-0044-03-15} and \mbox{-0044-04-15} are conventional
placeholders within the months Perseus gives; left as-is.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{Att.} 13.28 ``letter to Caesar''
withdrawal as a structural pivot in the cluster.} The Greek
\textit{probl\=ema Archid\=emou} (Stoic-dialectical ``Archidemus's
puzzle'') frames the dilemma; the bitter \textit{hunc de pompa
Quirini contubernalem} (Caesar as ``messmate of Quirinus's
procession,'' i.e.\ his statue carried with the gods at the
\textit{ludi}) is the cluster's sharpest single line of political
register. Worth a corpus-level note as the moment Cicero finally
abandons the project of writing an advice-letter to Caesar.
\item \textbf{The \textit{Cato}/\textit{Anticato} sop-register
(\textit{Att.} 13.27).} The \textit{Catonis
\textgreek{μείλιγμα}} ``a sop to balance my Cato'' is the
cluster's clearest single window onto how Cicero received
Caesar's \textit{Anticato} as a polemic exchange. The
\textit{epiteugma}/\textit{apoteugma} pair (success/failure) is
also worth a glossary note as the Stoic-rhetorical technical
vocabulary the letter deploys.
\item \textbf{The Dicaearchus revival cluster (\textit{Att.}
13.30, 13.31, 13.32, 13.33).} Dicaearchus's \textit{Descent}
(\textit{katabase\=os}), \textit{On the Soul} (\textit{peri
psych\=es}), and the \textit{Tripolitikon} surface across four
consecutive letters as the framing models for Cicero's own
projected dialogue \textit{\textgreek{πολιτικὸν σύλλογον}}
(``political assembly''). The cluster is the densest single
deployment of Dicaearchus in the corpus and is worth a sustained
allusion-pass entry.
\item \textbf{The \textit{Fam.} 6.15 chiasm as a single-sentence
masterpiece.} The Ides-of-March note to Basilus is six clauses
of perfect I/you-interlocking parallelism, and the deniable
passive \textit{quid agatur} (``what is being done'') is itself
an act of literary self-protection. Worth a corpus-level note
both for the rhetorical construction and for the date.
\item \textbf{The Bithynicus exchange (\textit{Fam.} 6.16--6.17)
as the cluster's unusual two-way pair.} 6.16 is the only
incoming letter in book 6's post-Pharsalus cluster; 6.17 is
Cicero's direct reply. Worth registering as a structural
exception to the cluster's one-direction-only norm. The
\textit{beneficiorum magnitudine} vs.\ \textit{necessitudine}
antithesis is the doctrinal hinge of 6.17.
\end{itemize}

\textbf{Suggested next translation batch} (when session 19 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 19:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T finish: \textit{Att.} 13.36 onward
through 13.52 + \textit{Att.} 14.1 onward.} 13.36 has dating
issues (year-precision, no Perseus URL in works.yaml --- only
the Latin Library fallback); skip 13.36 (and re-investigate at a
later metadata pass) and pick up at 13.37. The Att.\ 14 sequence
opens in April 44 BC at Astura/Lanuvium just after the Ides ---
parallel-dispatchable as 3--4 short letters per worker.
\item \textbf{Slice S (the chronological-gap sweep, 108 pending
letters earlier than the new -0044-04-15 marker):} the largest
single concentration is in \textit{Ad Familiares} 5
(\textit{Fam.} 5.9--5.18, 9 letters, all 45 BC) and the
remaining \textit{Att.} 12 / 13 holes (e.g.\ 13.15 and 13.18,
both still on placeholder stubs awaiting manual Latin from
Shackleton Bailey). Dispatch \textit{Fam.} 5.9--5.14 (6 letters)
as a single worker's batch; small and clustered chronologically
in 45 BC.
\item \textbf{Slice V continuation: the Paetus 45 BC tail.}
Only \textit{Fam.} 9.24 (February 43 BC) and \textit{Fam.} 9.25
(placeholder, no usable Latin) remain in book 9 pending --- 9.24
moves the marker further forward into 43 BC if picked up early.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}. None advanced
this session.
\item \textbf{Slice P (post-session metadata follow-up):} supply
manual Latin for \textit{Att.} 13.15 and 13.18 (placeholder
stubs from session 18) and resolve \textit{Att.} 13.28's
date-tradition discrepancy (Perseus literal 26 May vs.\ works.yaml
1 June) against Shackleton Bailey vol.\ 5. Also: investigate
\textit{Att.} 13.36's missing Perseus URL (works.yaml currently
points only to the Latin Library fallback, which 403s in the
sandbox).
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has $\sim$472 stub entries needing real summaries
--- ripe for an aggressive parallel pass once the Att.\ 14
sequence is opened.
\end{itemize}


\textbf{Translation state (post-Cowork-session-18):} 619 / 958
works drafted (\~64.6\%). Latest drafted by deep chronology
unchanged: \textit{Ad Familiares} 9.12 (Cumanum, late November 45
BC). \textbf{Session 18 drafted 20 letters --- the
Arpinum-to-Tusculanum daily-letter sequence of late-June/early-July
45 BC (\textit{Att.} 13.10--13.14, 13.16, 13.17, 13.19, 13.20,
13.22--13.25; 13 letters), plus the Paetus 45 BC / late-46 BC
continuation (\textit{Fam.} 9.22, 9.23, 9.26; 3 letters), plus the
Pompeian-exile cluster gap-fill (\textit{Fam.} 6.10, 6.11, 6.12,
6.13; 4 letters) --- in two parallel waves (five workers total),
plus three date corrections and one date-precision tightening.}
The chronological-gap warning is now \textbf{106 pending works
dated earlier than the latest-drafted} (down from 126 at the end of
session 17). The pointer for ``latest drafted by date'' did not
advance --- session 18 continued the gap-fill sweep, this time
nearly closing out the Arpinum daily-letter run of late June 45 BC
and continuing the Paetus / Pompeian-exile threads.

\textbf{Cowork session 18 --- 20 letters drafted across two
parallel waves (five workers):}

\textbf{Wave 1 (3 workers, 12 letters --- \textit{Att.} 13.10--13.24,
the late-June Arpinum-Tusculanum daily-letter run):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 13.10--13.13):} 13.10 (the
\textit{politikoteros}/\textit{koinoteros} register run, range-
dateline xiiii--xi K. Quint. = 18--21 June 45 BC; one daggered crux
\dag\ \textit{aut erat} \dag\ in \S3); 13.11 (one Greek phrase
\textit{ou tauton eidos}); 13.12 (the \textit{Academica}
dedication-shuffle locus: seven Greek transliterations including
\textit{Kallippides}, \textit{auto to metro kai}, and the Hesiod
\textit{Works and Days} 350 quotation \textit{ai ke dunai}; the
\textit{prosphonesis} register reactivated; \textbf{date correction}
from invalid placeholder \mbox{-0045-06-31} to \mbox{-0045-06-24}
per Perseus OCR-garbled dateline \textit{vh i K. Quint.}, restored
as viii K. Quint., supported by the surrounding sequence
13.11 = ix K. = 23 June, 13.13 = vi K. = 26 June; \textbf{also
trimmed} \texttt{location\_written} from ``in Arpinati vh'' to
``in Arpinati''); 13.13 (five Greek transliterations, including
the Hector tag \textit{aideomai Troas} from \textit{Iliad} VI.442;
bibliographically important note on the \textit{Academica}
expansion from 2 to 4 books).

\item \textbf{Worker B (\textit{Att.} 13.14, 13.16, 13.17, 13.19):}
13.14 (very brief, no Greek); 13.16 (\textbf{four Greek phrases}
\textit{Akademiken syntaxin}, \textit{para to prepon},
\textit{apaideusia}, \textit{atripsia}, the last pair a candidate
translator-note for the rare second term); 13.17 (three Greek
phrases, daggered crux \dag\ \textit{non imperassem. igitur aliquid
tuis} \dag\ in \S1 preserved); 13.19 (the long letter at $\sim$620
words, \textbf{nine Greek transliterations} including
\textit{akindyna}, \textit{philendoxos}, \textit{akatalepsian},
\textit{kophon prosopon}, \textit{Aristoteleion}, \textit{logikotera},
\textit{hermaion}; daggered crux \dag\ \textit{easque} \dag\ in
\S4; the \textit{De Finibus} reference \textit{quinque libros peri}
restored to ``On Ends'' without note per editorial consensus).
\textbf{Att. 13.15 and 13.18 were SKIPPED} --- the Latin Library
edition combines 13.14--13.15 and 13.17--13.18, and Perseus's TEI
book 13 lacks discrete \texttt{n=15} and \texttt{n=18} positions
matching the works.yaml entries; placeholder stubs left in the
Latin files explaining the situation. Manual Latin from Shackleton
Bailey or another standard edition is needed before these two can
be translated.

\item \textbf{Worker C (\textit{Att.} 13.20, 13.22--13.24):} 13.20
(four Greek phrases \textit{philaitios}, \textit{philosophos},
\textit{dedechthai}, \textit{me gar autois}; daggered crux \dag\
\textit{in toto} \dag\ in \S4; dateline ``vi aut v Non. Quint.''
ambiguous between 2 and 3 July, works.yaml's 07-03 reading
preserved); 13.22 (three Greek phrases including
\textit{asmenaitata} and \textit{eulogian} --- the \textit{eulogon}
register continues from 13.05/13.07; daggered crux \dag\ \textit{a
quis sine te opprimi militia est} \dag\ at end of \S4); 13.23
(two Greek phrases including \textit{symbiosis} ``shared life,''
the cluster's most resonant Greek term for the Atticus friendship;
daggered crux \dag\ \textit{deffecti} \dag\ in \S2; the veiled
grievance against Brutus motivating the \textit{symbiosis} remark
kept opaque in translation per the Latin); 13.24 (very brief, two
Greek phrases \textit{diphtherai} and \textit{aideomai}; the
``Cicero'' in \S1 disambiguated in JSON notes as the son, not the
orator).
\end{itemize}

\textbf{Wave 2 (2 workers, 8 letters --- \textit{Att.} 13.25 +
\textit{Fam.} 9.22, 9.23, 9.26 + \textit{Fam.} 6.10--6.13, the
late-Tusculanum closure and the Paetus / Pompeian-exile gap-fill):}
\begin{itemize}
\item \textbf{Worker D (\textit{Att.} 13.25 + \textit{Fam.} 9.22,
9.23, 9.26):} 13.25 (four Greek phrases including the Homer
\textit{Iliad} 11.654 allusion \textit{tacha ken kai anaition
aitiooto} ``even a guiltless man might be blamed,'' and the closing
\textit{o Academiam volaticam et sui similem!}); 9.22 (the long
bawdy Stoic-parrhesia letter at $\sim$860 words: one Greek phrase
\textit{ho sophos euthyrrhemonesei} ``the wise man will speak
openly''; Cicero's elaborate defence of plain Latin terms for
genital matters [\textit{mentula}, \textit{coleos}, etc.] preserved
literally where the joke turns on the Latin word --- a major Paetus-
register set-piece; \textit{suppedit} read as ``pisses underneath
himself'' against Shackleton Bailey's emendation, candidate
translator-note); 9.23 (very brief at $\sim$115 words; no Greek;
the Perseus transcript's known glitch ``Here veni'' restored to
``Heri veni'' = ``Yesterday I came''; the gout joke and chiastic
close \textit{minime edacem} / \textit{inimicum cenis sumptuosis}
preserved; \textbf{date-precision update} from year to month, date
moved from -0046-12-28 placeholder to -0046-12-15 per Perseus
\textit{m. interc. post a. 708 (46)} = second [later] intercalary
month of 46 BC, $\sim$mid-to-late December Julian); 9.26 (one Greek
phrase \textit{zetema} ``a question'' put to Dion the philosopher;
pseudo-Ennian mock-epic verse \textit{cuius ob os Graii ora
obvertebant sua} preserved; Aristippus's \textit{habeo, non habeor
a Laide} ``I have, I am not had by, Lais'' with the parenthetical
``in Greek the saying is better''; \textbf{major date correction}
from wildly-wrong placeholder \mbox{-0046-03-03} year-precision to
\mbox{-0046-11-15} month-precision per Perseus dateline
\textit{Romae ex. m. interc. pr. aut in. post a. 708 (46)} =
seam between earlier and later intercalary months of 46 BC,
$\sim$mid-November Julian).

\item \textbf{Worker E (\textit{Fam.} 6.10--6.13 Pompeian-exile
cluster):} 6.10 to Trebianus ($\sim$830 words; no Greek; the
doctrinal pivot at \S4 \textit{conscientia factorum et consiliorum}
``the consciousness of one's deeds and counsels'' established as
the binding Stoic-consolatio formula of the cluster, mirrored
verbatim at the close of 6.13; the ``tilts of the times''
\textit{temporum inclinationibus} as the Book 6 keynote); 6.11 to
Trebianus (no Greek; daggered crux \dag\ \textit{opus esse} \dag\
in \S1; the quiet parenthetical greeting to Siro the Epicurean as
the cluster's Stoic-vs-Epicurean seam); 6.12 to Ampius Balbus (no
Greek; the live coinage \textit{tuba belli civilis} ``the trumpet
of the civil war'' preserved as direct quotation; the late-46
regime roll-call --- Pansa, Hirtius, Balbus, Oppius, Matius,
Postumius, \textit{Tillius Cimber}, who in three years will stand
among the Liberators --- left to register the irony without
commentary; the doctrinal pivot at \S5 sharpened to
\textit{doctrina ac litterae} as the single refuge ``now even of
preservation [\textit{nunc vero etiam salutem}],'' a tighter
formulation than 6.10's; ring-form \textit{ut ad initium revertar});
6.13 to Ligarius (no Greek; the same self-deprecating formula
\textit{si tantum possem quantum in ea re p., de qua ita sum
meritus} as Fam 6.10.2 --- same hand, same month; closes at \S5
with the identical \textit{conscientia et factorum et consiliorum
tuorum} pivot; the addressee is the Ligarius of the speech
\textit{Pro Ligario} the following year).
\end{itemize}

\textbf{Date corrections and precision changes committed to
\texttt{meta/works.yaml} during session 18 (three entries):}
\begin{itemize}
\item \textit{Att.} 13.12: invalid placeholder \mbox{-0045-06-31}
$\rightarrow$ \mbox{-0045-06-24} day-precision per Perseus OCR-
garbled dateline \textit{vh i K. Quint.}, restored as viii K. Quint.
(= 24 June 45 BC; vii K. = 25 June also defensible). The
\texttt{location\_written} field was also trimmed from ``in
Arpinati vh'' (carrying the dateline-garble fragment) to ``in
Arpinati''.
\item \textit{Fam.} 9.23: \mbox{-0046-12-28} year-precision
$\rightarrow$ \mbox{-0046-12-15} month-precision per Perseus
\textit{Scr. in Cumano m. interc. post a. 708 (46)} (= second
[later] intercalary month of 46 BC, $\sim$mid-to-late December
Julian).
\item \textit{Fam.} 9.26: wildly-wrong placeholder
\mbox{-0046-03-03} year-precision $\rightarrow$ \mbox{-0046-11-15}
month-precision per Perseus \textit{Romae ex. m. interc. pr. aut
in. post a. 708 (46)} (= seam between earlier and later intercalary
months of 46 BC, $\sim$mid-November Julian). The \texttt{046bc-}
file-prefix is correct under either reading; no rename needed.
\end{itemize}

\textbf{Other date observations (no correction needed):}
\begin{itemize}
\item \textit{Att.} 13.10 dateline range \textit{xiiii et xi K.
Quint.} = 18--21 June 45 BC; works.yaml's day-precision -0045-06-21
(the final day of the range, xi K.) preserved as the conventional
landing point.
\item \textit{Att.} 13.20 dateline \textit{vi aut v Non. Quint.}
ambiguous between 2 July (vi Non.) and 3 July (v Non.);
works.yaml's day-precision 07-03 (v Non.) preserved.
\item \textit{Fam.} 9.22 dateline \textit{m. Iun. aut Quint.}
month-precision uncertain between June and July of 45 BC;
works.yaml's month-precision 06-15 covers the earlier of the two
options.
\item \textit{Fam.} 6.11 dateline \textit{in. m. Iun. a. 709 (45)}
could be tightened from month-precision 06-15 to $\sim$06-01;
month-precision left in place as sufficient.
\item \textit{Fam.} 6.12 dateline \textit{ex. m. Nov. a. 708 (46)}
could be tightened from month-precision 11-15 to $\sim$11-28;
month-precision left in place.
\item \textit{Fam.} 6.13 dateline \textit{in. m. Sext. a. 708 (46)}
could be tightened from month-precision 08-15 to $\sim$08-01;
month-precision left in place.
\end{itemize}

\textbf{Two letters skipped this session (Latin not usable):}
\begin{itemize}
\item \textit{Att.} 13.15 --- placeholder stub written to the
Latin file. The works.yaml entry lacks a Perseus URL; the Latin
Library edition combines 13.14--13.15 (TOC line ``13--14 14--15
16''). Modern editors (Shackleton Bailey) variously assign the
text. Manual Latin from a standard edition needed before this can
be translated.
\item \textit{Att.} 13.18 --- placeholder stub written to the
Latin file. Same situation: works.yaml lacks a Perseus URL; Latin
Library combines 13.17--13.18. Manual Latin needed.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The Arpinum daily-letter \textit{Academica}-shuffle
cluster (\textit{Att.} 13.10--13.25).} The cluster's binding
preoccupation is the rapid-cycle revision of the
\textit{Academica}: dedication shifted from Catulus/Lucullus to
Varro (13.12, 13.13, 13.16, 13.19, 13.25), book-count expanded
from two to four (13.13), and the prefatory \textit{prosphonesis}
to Varro composed and revised across multiple letters. The Greek
\textit{Akademiken syntaxin} ``the Academic arrangement'' (13.16,
13.19) becomes a fixed cluster keyword. Worth a corpus-level note
as the first sustained look at a Ciceronian philosophical
publication in active revision.
\item \textbf{The \textit{symbiosis} register in \textit{Att.}
13.23.} \textit{symbiosis} ``shared life'' is the cluster's most
resonant Greek term for the Atticus friendship under strain ---
the veiled grievance against Brutus (whose recent behaviour
provokes the remark) is left unspoken in the Latin. Worth flagging
as a binding emotional keyword of the Atticus correspondence in
this stretch.
\item \textbf{The Paetus parrhesia letter (\textit{Fam.} 9.22)
and its place in the Paetus cluster.} The bawdy Stoic-parrhesia
set-piece (the elaborate defence of plain Latin terms for genital
matters: \textit{mentula}, \textit{coleos}, \textit{cauda},
\textit{penis}, the corrupt stage-quotations and the false
etymologies) is the cluster's most distinctive single performance.
The Greek \textit{ho sophos euthyrrhemonesei} ``the wise man will
speak openly'' frames the whole as Stoic doctrine; the joke turns
on Cicero adopting the philosophical pretext for what is in fact
sustained low-diction comedy. The \textit{suppedit} reading
``pisses underneath himself'' vs.\ Shackleton Bailey's emendation
is the translator-note candidate.
\item \textbf{The Pompeian-exile doctrinal pivot
(\textit{conscientia factorum et consiliorum}).} The same
Stoic-consolatio formula recurs verbatim in \textit{Fam.} 6.10.4
and 6.13.5 --- a deliberate binding refrain across the Book 6
cluster. Worth flagging as the cluster's stable doctrinal pivot;
the 6.12.5 sharpening to ``now even of preservation
[\textit{nunc vero etiam salutem}]'' is the cluster's most acute
formulation.
\item \textbf{Homer and Hesiod allusions in Atticus 13.x.}
\textit{Iliad} VI.442 (Hector's \textit{aideomai Troas}) at
13.13; \textit{Iliad} 11.654 (\textit{tacha ken kai anaition
aitiooto}) at 13.25; Hesiod \textit{Works and Days} 350
(\textit{ai ke dunai}) at 13.12. Worth corpus-level allusion
entries and glossary notes at the apparatus pass.
\end{itemize}

\textbf{Suggested next translation batch} (when session 18 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 18:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T continuation: \textit{Att.} 13.21 + remaining
\textit{Att.} 13 mid-book (13.26 onward as they fall by date).}
13.21 (29 July 45 BC, Asturae) is the next surviving Atticus
letter after the daily-run cluster. 13.26 onward continues the
sequence (note 13.26 is dated -0045-05-14, well before 13.10, so
it's an earlier letter shelved in book 13 by manuscript order ---
treat similarly to the 13.06 mid-March-out-of-sequence case from
session 17).
\item \textbf{Slice V finish (the Paetus 45 BC sequence):} only
\textit{Fam.} 9.24 (Feb 43 BC, much later in chronology) and
\textit{Fam.} 9.25 (placeholder, no usable Latin) remain in book
9 pending; effectively the Paetus 45 BC cluster is closed with
session 18's 9.22, 9.23, 9.26.
\item \textbf{Slice W continuation (the Pompeian-exile cluster):}
\textit{Fam.} 6.8, 6.9 (to Caecina, mid-late 46 BC, both short),
6.15--6.17 (to Basilus / Mescinius / Fadius Gallus and others,
44--45 BC if pending). Confirm pending status against works.yaml
before dispatching.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}. None advanced
this session.
\item \textbf{Slice P (post-session metadata follow-up): supply
manual Latin for \textit{Att.} 13.15 and 13.18}, both skipped
this session due to no usable upstream source. Source: Shackleton
Bailey, \textit{Cicero's Letters to Atticus} vol.\ 5 (Cambridge),
or any modern critical edition. Until supplied, these two entries
remain pending and the \textit{Att.} 13 run has two visible holes.
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has $\sim$472 stub entries needing real summaries.
\end{itemize}


\textbf{Translation state (post-Cowork-session-17):} 599 / 958
works drafted (\~62.5\%). Latest drafted by deep chronology
unchanged: \textit{Ad Familiares} 9.12 (Cumanum, late November 45
BC). \textbf{Session 17 drafted 24 letters --- the Tusculanum
late-May/early-June 45 BC run (\textit{Att.} 12.51--12.53 +
\textit{Att.} 13.1--13.9, 12 letters, 20 May--17 June/1 July 45 BC,
incorporating one out-of-sequence Astura mid-March letter 13.6),
plus the Paetus mid-46 BC to late-46 BC sequence (\textit{Fam.}
9.15--9.21, 7 letters), plus the Torquatus consolation cluster
(\textit{Fam.} 6.2--6.4, 3 letters, early 45 BC), plus the Lepta
practical note (\textit{Fam.} 6.18, end January 45 BC) and the
Toranius condolence (\textit{Fam.} 6.21, c.\ April 45 BC) --- in
three parallel waves (eight workers total) and applied five date
corrections.} The chronological-gap warning is now \textbf{126
pending works dated earlier than the latest-drafted} (down from
150 at the end of session 16). The pointer for ``latest drafted by
date'' did not advance --- session 17 continued the gap-fill sweep,
this time advancing the Astura-to-Tusculanum daily letter sequence
beyond mid-May, opening \textit{Att.} 13, and resuming the Paetus
witty-dining cluster after a long gap.

\textbf{Cowork session 17 --- 24 letters drafted across three
parallel waves (eight workers):}

\textbf{Wave 1 (3 workers, 8 letters --- the
Tusculanum-late-May/Astura-cluster closure and \textit{Att.} 13
opening, 20--30 May plus 1--2 June 45 BC, in Tusculano):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 12.51--12.53):} 12.51 (the
\textit{politikoi} / \textit{touto de m\=el\=os\=ei} pair --- two
Greek phrases, the surgical-probe metaphor preserved; the
\textit{hoc metuere, alterum in metu non ponere} antithesis kept
balanced; \textbf{date correction} from year-precision placeholder
\mbox{-0045-04-20} to day-precision \mbox{-0045-05-20} per Perseus
dateline \textit{xiii K. Iun.} = 20 May 45 BC, with the explicit
note that Perseus prints \textit{K. luit.} as an OCR garble for
\textit{K. Iun.} per the surrounding sequence
[12.52 = xii K. Iun. = 21 May, 12.53 = xi K. Iun. = 22 May];
\textit{perscriptio} rendered ``assignment'' on the banker's-
transfer reading; possible senarius accentuation
\textit{hoc m\'etuere, \'in metu non p\'onere} noted but rendered
as plain antithetic prose); 12.52 (one Greek phrase
\textit{apographa} ``transcripts'' --- the closing tease about
Cicero's Latin philosophical works as transcripts of Greek
originals, the cluster's first explicit metareflection on the
\textit{syntagmata} now occupying him; HS \overline{XX} rendered
``20{,}000 sesterces''; the throwaway \textit{de lingua Latina
securi es animi} confirmed as referring to the in-progress
\textit{Academica}); 12.53 (very brief, no Greek; the cluster's
characteristic ``write daily even with nothing to write'' moment
foregrounded; one-paragraph headnote per the brief).

\item \textbf{Worker B (\textit{Att.} 13.01--13.03):} 13.01 (one
Greek phrase \textit{katabi\=osin} ``a running-down of life'' /
``passing of remaining years''; one daggered crux \dag\
\textit{totum in hunc} \dag\ in \S3 preserved); 13.02 (very brief,
60 words, the manuscript breaks off mid-sentence at
\textit{verum tamen---} preserved with the em-dash; the
\textit{humanitatem exuimus} ``we have stripped off all
humanity'' echo of the grief-cluster register); 13.03 (one
daggered crux \dag\ \textit{espraes} \dag\ in \S1 preserved,
with the headnote suggesting \textit{ex praesenti} as a possible
restoration per flag-not-resolve).

\item \textbf{Worker C (\textit{Att.} 13.04--13.05):} 13.04
(no Greek; the saepius/saepius parallelism preserved as ``keep
asking \ldots\ keep answering''; \textit{nomina} in the financial
sense rendered ``debts''; the Terentia-dowry context flagged in
the headnote); 13.05 (one Greek phrase \textit{eulogon}
``stands to reason'' --- Stoic dialectical term in parenthesis;
the \textit{misi tibi Torquatum} rendered ``I have sent you the
\textit{Torquatus}'', the standard reading as the presentation
copy of what becomes \textit{De Finibus} Book 1; the Mummius
ambiguity --- L.\ Mummius Achaicus vs.\ his brother Spurius ---
resolved in headnote).
\end{itemize}

\textbf{Wave 2 (2 workers, 7 letters --- \textit{Att.} 13.6--13.9
\& \textit{Fam.} 9.15--9.17, mid-March 45 BC + mid-46 BC):}
\begin{itemize}
\item \textbf{Worker D (\textit{Att.} 13.06--13.09):} 13.06
(Astura, mid-March 45 BC, out-of-sequence within \textit{Att.} 13
--- the editorial decision to leave it under 13 rather than
re-shelving into the Astura cluster preserved; no Greek;
\textit{columnarium} rendered ``column-tax'' [the Caesarian
assessment]; \textit{solitudinem Catonis} translated literally as
``Cato's lonely position'' with the resonance carried by the
headnote); 13.07 (one Greek phrase \textit{eulogon}
``reasonable''; the sly self-distancing
\textit{nisi placet hanc ipsam sententiam nos persequi}
``unless one cares to take up that very line of thought oneself''
preserved); 13.08 (one Greek phrase
\textit{Panaitiou peri Pronoias} ``Panaetius \textit{On
Providence}''; \textit{triplicis} rendered ``triple-tablets'' for
the three-leaf wax tablets; \textit{Caelianorum} taken with
\textit{epitomen Bruti} as Brutus's epitome of the annals of
L.\ Coelius Antipater); 13.09 (\textbf{five Greek phrases}
\textit{ektenesteron} ``more attentive,''
\textit{philostorgoteron} ``more affectionate,'' \textit{aphata}
``unspeakable,'' \textit{adi\=eg\=eta} ``not to be recounted,''
\textit{eukair\=os} ``at just the right moment'' --- the dense
Greek-deployment cluster of the spring; the dateline
\textit{xttv K. Quint.} is an OCR garble [restorations: xiv K.
Quint.\ = 18 June OR K.\ Quint.\ = 1 July] for which the
translation does not depend on disambiguation; \texttt{works.yaml}
date preserved at \mbox{-0045-07-01} per current entry, with the
headnote naming both readings).

\item \textbf{Worker E (\textit{Fam.} 9.15--9.17):} 9.15
(no Greek; \textit{clavum tenebamus \ldots\ vix est in sentina
locus} rendered ``we sat on the stern and held the helm \ldots\
now there is barely room in the bilge'' preserving the
helmsman/bilge contrast; \textit{noster hic praefectus moribus}
``our prefect of morals'' [of Caesar]; \textbf{date correction}
from year-precision placeholder \mbox{-0046-04-20} to
month-precision \mbox{-0046-11-15} per Perseus dateline
\textit{Romae in.\ interc.\ priore} = beginning of the earlier
intercalary month of 46 BC = ca.\ mid-November of Caesar's
calendar-reform year); 9.16 (one Greek phrase
\textit{apophthegmaton} ``sayings''; two daggered cruxes \dag\
\textit{popillium} \dag\ and \dag\ \textit{denarium} \dag\
preserved with explicit dagger markers; the magnificent
\textit{salis enim satis est, sannionum parum} ``Salt there is
enough; clowns, too few'' epigram preserved as Cicero's perfectly-
balanced chiasm; \textit{tyrotarichi patinam} rendered ``dish of
cheese-and-salt-fish'' in the diaspora-of-poor-man's-food
register; \textit{polypum miniati Iovis similem} rendered ``an
octopus to match a red-leaded Jupiter'' on the red-Capitoline-
Jupiter reading); 9.17 (no Greek; the
\textit{de lucro prope iam quadriennium vivimus} idiom rendered
``for nearly four years we have been living on bonus time'';
closing tricolon \textit{optare optima, cogitare difficillima,
ferre quaecumque erunt} rendered ``hope for the best, brace for
the worst, and bear whatever comes,'' with \textit{cogitare} taken
in its Stoic-\textit{proso{\=c}h\=e} sense; \textbf{date
correction} from day-precision \mbox{-0046-08-13} to
month-precision \mbox{-0046-08-20} per Perseus
\textit{post Id.\ Sext.} = ``after the Ides of Sextilis''
= 14--31 August 46 BC).
\end{itemize}

\textbf{Wave 3 (3 workers, 9 letters --- \textit{Fam.} 9.18--9.21
+ \textit{Fam.} 6.2--6.4 + \textit{Fam.} 6.18, 6.21, the Paetus
late-46/Torquatus-early-45/Lepta-Toranius cluster):}
\begin{itemize}
\item \textbf{Worker F (\textit{Fam.} 9.18--9.21):} 9.18
(one Greek phrase \textit{prolegomenas} ``rhetorical preludes'';
the schoolmaster conceit \textit{quasi habere coeperim} preserved;
proverb \textit{sus Minervam} rendered ``a pig giving lessons to
Minerva''; the Pompey/Lentulus/Scipio/Afranius vs.\ ``Cato
gloriously'' death-catalogue kept terse; the Haterianum/Hirtianum
sauce chiasm balance preserved); 9.19 (no Greek; the Balbus
wordplay \textit{balbos / disertos} ``stutterers / well-spoken''
glossed inline as the joke's whole point;
\textit{ad suam} rendered tactfully but visibly as ``to his
lady's house''); 9.20 (one Greek phrase \textit{opsimatheis}
``late-learners''; \textit{scurram velitem malis oneratum}
rendered ``skirmisher of a comic buffoon \ldots\ pelted with
apples'' [the \textit{mala} = apples flung at comic actors];
\textit{in Epicuri castra coniecimus} kept military as ``flung
myself into the camp of Epicurus''; the closing threat
\textit{te iacente bona tua comedim} kept blunt as ``I shall
devour your property with you lying flat'';
\dag\ \textit{ex artis tantum habemus} \dag\ preserved as crux);
9.21 (one Greek phrase \textit{apoteugma} ``misfire'';
\textit{Papisii dicebamini} preserved as direct address
``you used to be called the Papisii''; \textit{a Trabea} flagged
as a comic-poet tag of unknown content; \textit{cantharidas
sumpsisse} and \textit{sutorio atramento absolutus} kept literal
with notes on the cantharides/shoemaker's-blacking suicide-or-ink
ambiguity; \textbf{date correction} from year-precision
\mbox{-0046-10-26} to month-precision \mbox{-0046-11-15} per
Perseus \textit{ut videtur, circ.\ m.\ intercal.\ pr.} = around
the earlier intercalary month of 46 BC).

\item \textbf{Worker G (\textit{Fam.} 6.2--6.4 Torquatus
consolation cluster):} 6.2 (no Greek; \S2's Stoic trichotomy
[arms prevail / peace restored / total ruin] rendered as a
numbered ``one of three things'' to make the rhetorical
scaffolding visible; the M.\ Antonius the orator [Torquatus's
grandfather-in-law] disambiguated from the triumvir in headnote);
6.3 (one Greek phrase \textbf{\textit{glauk' eis Ath\=enas}}
``owls to Athens'' --- particularly pointed since Torquatus is
literally in Athens; one daggered crux \dag\
\textit{quemvis aut} \dag\ in \S4 preserved); 6.4 (the longest
of the three at 838 words; no Greek; the doctrinal pivot
\textit{conscientiam rectae voluntatis maximam consolationem esse
rerum incommodarum nec esse ullum magnum malum praeter culpam}
rendered to preserve the parallel ``X is the greatest consolation
\ldots\ there is no great evil except guilt''; \S4's turn from
consoler to consoled flagged in the headnote as the
characteristic move of the cluster; one daggered crux \dag\
\textit{non quo, sed quod difficilis erat coniectura} \dag\
preserved).

\item \textbf{Worker H (\textit{Fam.} 6.18 Lepta + 6.21
Toranius):} 6.18 (one Greek phrase \textbf{Hesiod \textit{Works
and Days} 289 \textit{t\=es d' aret\=es hidr\=ota}} ``but in
front of excellence [the gods set sweat]'' --- the cluster's only
Hesiod quotation; the Caesarian municipal-law distinction
between \textit{qui faciunt} [currently practising auctioneers,
barred] and \textit{qui fecissent} [former auctioneers, not
barred] preserved literally to keep the legal-technical force;
\textit{me hercule} rendered ``by Hercules'' per STYLE.md; the
diminutive ``our young Lepta'' for the son distinguished from
the father throughout); 6.21 (no Greek; the dramatic antithesis
\textit{aut interitum \ldots\ aut \ldots\ servitutem} rendered
as a colon-split parallel ``destruction it would bring, if you
were defeated; if you conquered, slavery'' to preserve Cicero's
chiastic shape; \textit{salutem retinere} rendered ``preserve
survival'' rather than ``preserve safety'' for the sharp post-
Pharsalus sense against \textit{dignitati \ldots\ consuluisse}).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 17 (five entries):}
\begin{itemize}
\item \textit{Att.} 12.51: \mbox{-0045-04-20} year-precision
$\rightarrow$ \mbox{-0045-05-20} day-precision per Perseus
\textit{xiii K. Iun.} (= 20 May 45 BC; ``K. luit.'' in Perseus is
an OCR garble for ``K. Iun.'' per surrounding sequence).
\item \textit{Fam.} 9.15: \mbox{-0046-04-20} year-precision
$\rightarrow$ \mbox{-0046-11-15} month-precision per Perseus
\textit{Romae in.\ interc.\ priore} (= beginning of earlier
intercalary month of 46 BC, ca.\ mid-November).
\item \textit{Fam.} 9.17: \mbox{-0046-08-13} day-precision
$\rightarrow$ \mbox{-0046-08-20} month-precision per Perseus
\textit{Romae post Id.\ Sext.} (= 14--31 August 46 BC; original
day-precision Aug 13 was inconsistent with ``post Id.'').
\item \textit{Fam.} 9.19: \mbox{-0046-08-13} day-precision
$\rightarrow$ \mbox{-0046-08-20} month-precision (same as 9.17).
\item \textit{Fam.} 9.21: \mbox{-0046-10-26} year-precision
$\rightarrow$ \mbox{-0046-11-15} month-precision per Perseus
\textit{circ.\ m.\ intercal.\ pr.} (= around earlier intercalary
month of 46 BC).
\end{itemize}

\textbf{Other date observations (no correction needed or
deferred):}
\begin{itemize}
\item \textit{Att.} 13.09 dateline OCR garble: Perseus prints
\textit{xttv K. Quint.} which is not a valid Roman numeral. The
two standard restorations are (a) \textit{xiv K. Quint.}
= 18 June 45 BC (Shackleton Bailey, Tyrrell--Purser), or
(b) \textit{K. Quint.} alone = 1 July 45 BC. \texttt{works.yaml}
has \mbox{-0045-07-01} day-precision matching restoration (b);
preserved pending review against Shackleton Bailey.
\item \textit{Fam.} 6.2: Perseus \textit{ante xii K. Mai.}
(= before 20 April). \texttt{works.yaml} has \mbox{-0045-04-20}
day-precision; technically ``ante'' suggests slightly earlier,
but the precision is close enough not to demand a correction.
\item \textit{Fam.} 6.18: Perseus \textit{ex.\ m.\ Ian.}
(= end of January). \texttt{works.yaml} has \mbox{-0045-01-15}
month-precision; could be tightened to \mbox{-0045-01-28} but
month-precision covers the range.
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The Paetus voice register reactivated (\textit{Fam.}
9.15--9.21).} After the long gap since 9.10--9.13 was drafted in
earlier sessions, the Paetus cluster's distinctive register
returns in force: food language as Cicero's medium of
self-mockery (\textit{tyrotarichum}, \textit{lucanicae},
\textit{polypus miniati Iovis}, the appetizer-to-roast-veal
\textit{promulside ad assum vitulinum}), chiastic epigrams
(\textit{dicendi discipulos, cenandi magistros}; \textit{salis
satis est, sannionum parum}), deliberate slumming into low
diction (the \textit{Popillius/denarius} cruxes in 9.16, the
threat-as-affection close \textit{bona tua comedim} in 9.20),
mock-formal verbs (\textit{censeo}), and the wordplay that drives
each joke's whole point (Balbi/balbos in 9.19; the philosophical
defection-to-Epicurus military metaphor in 9.20). Worth a
corpus-level note as the cluster's binding voice across the 18
months it spans.
\item \textbf{The Torquatus consolation register vs.\ the
Toranius condolence register (\textit{Fam.} 6.2--6.4 vs.\ 6.21).}
Two Pompeian-exile registers in proximity: Torquatus letters are
grave, philosophically pitched, with full Stoic-consolatio
machinery deployed (\textit{conscientiam rectae voluntatis
maximam consolationem esse rerum incommodarum} as the doctrinal
pivot); Toranius letter is more distant, more measured, with the
philosophical resources surfacing only briefly. The two registers
should sound audibly different even though the subject (Pompeian
defeat, Caesarian clemency, Athens-as-refuge) is the same.
\item \textbf{The Hesiod quotation in \textit{Fam.} 6.18.}
The Hesiod \textit{Works and Days} 289 quotation
\textit{t\=es d' aret\=es hidr\=ota} ``but in front of excellence
[the gods set sweat]'' is a canonical line, frequently quoted by
Cicero across his philosophical and rhetorical works. Worth a
corpus-level allusion entry and a glossary note when the
apparatus pass reaches \textit{Fam.} 6.
\item \textbf{The Caesarian municipal-law technical distinction
in \textit{Fam.} 6.18.1.} The \textit{qui faciunt} /
\textit{qui fecissent} contrast (currently practising auctioneers
barred from public office vs.\ former ones not barred) is a
small but precise window onto the legal-technical drafting style
of Caesar's \textit{lex municipalis}. Worth preserving literally
in translation; modernizing into ``current'' / ``former'' loses
the explicit verbal-aspect contrast that the Latin foregrounds.
\item \textbf{The \textit{cantharidas} / \textit{sutorio
atramento} suicide-or-ink ambiguity in \textit{Fam.} 9.21.4.}
\textit{cantharidas sumpsisse} (``took cantharides,'' a poisonous
beetle) and \textit{sutorio atramento absolutus} (``acquitted by
shoemaker's blacking'') are two interlocked obscurities in
Cicero's antiquarian Papisius/Carbo joke. The standard reading
is that both are suicide-by-poison idioms (with the ``ink'' of
shoemaker's atramentum standing for the poison). The translation
preserves the literal images with the obscurity intact rather
than disambiguating in body; a translator-notes entry should
record the choice.
\item \textbf{The \textit{eulogon} doubling across \textit{Att.}
13.05 and 13.07.} \textit{eulogon} ``reasonable'' / ``stands to
reason'' appears in two consecutive letters of the Tusculanum
philosophical-writing cluster, both times as a Stoic dialectical
term in parenthesis. Worth flagging as the cluster's stable
philosophical-technical vocabulary item.
\end{itemize}

\textbf{Suggested next translation batch} (when session 17 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 17:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T continuation: \textit{Att.} 13.10--13.20 +
\textit{Att.} 13.22 onward as they fall by Perseus dating.} The
Tusculanum daily-letter sequence of June 45 BC continues; the
\textit{Att.} 13 mid-book run is the natural continuation.
Plan 12--15 letters across 3 workers, watching for the
\textit{Att.} 13 manuscript-order/date-order disagreements that
have already shown up in 12.49/12.50 and 13.07/13.08.
\item \textbf{Slice V continuation (the Paetus 45 BC sequence):}
\textit{Fam.} 9.22, 9.23 (the two remaining year-precision
pending Paetus letters, both 45 BC), plus 9.24--9.26 if they
fall pending in the chronological sweep. The Paetus voice is now
firmly re-established; running the remaining Paetus letters as a
single sub-batch capitalises on the worker's voice continuity.
\item \textbf{Slice W continuation (the Pompeian-exile
condolence cluster):} \textit{Fam.} 6.5, 6.6 (early 45 BC, to
Caecina, both substantial), 6.7 (Caecina to Cicero, a rare
non-Cicero voice in book 6), 6.10--6.14 (Trebianus and Plancius
consolations of 46 BC, gap-fill).
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}. None advanced
this session.
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has $\sim$472 stub entries needing real summaries.
\end{itemize}


\textbf{Translation state (post-Cowork-session-16):} 575 / 958
works drafted (\~60.0\%). Latest drafted by deep chronology
unchanged: \textit{Ad Familiares} 9.12 (Cumanum, late November 45
BC). \textbf{Session 16 drafted 17 letters --- the conclusion of
the Astura grief sequence (\textit{Att.} 12.38--12.50, 13 letters,
6--19 May 45 BC) plus the Cassius / Stoic-Epicurean diptych
(\textit{Fam.} 15.16--15.19, 4 letters, mid-Dec 46 BC--end Jan 45
BC) --- in two parallel waves (four workers) and applied one date
correction.} The chronological-gap warning is now \textbf{150
pending works dated earlier than the latest-drafted} (down from
166 at the end of session 15). The pointer for ``latest drafted by
date'' did not advance --- session 16 continued the gap-fill sweep
of pre-Fam.\ 9.12 letters.

\textbf{Cowork session 16 --- 17 letters drafted across two
parallel waves (four workers):}

\textbf{Wave 1 (3 workers, 13 letters --- the Astura grief
sequence concludes, 6--19 May 45 BC):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 12.38--12.41, 6--11 May 45
BC, Astura):} 12.38 (the brief opening on writing as a partial
release, \textit{aberro} ``I get out of myself a little'' added to
the cluster's \textit{levari}/\textit{adlevor} register);
12.39 (the lift-up vocabulary \textit{adlevor} ``I am lifted up a
little''); 12.40 (the \textit{Anticato}/\textit{laudatio Catonis}
question, with \textbf{four Greek phrases}
\textit{sumbouleutikon} ``a piece of political counsel,''
\textit{Aristotelous} ``Aristotle's,'' \textit{Theopompou}
``Theopompus's,'' \textit{pros Alexandron} ``addressed to
Alexander'' --- the \textit{Anticato}-rebuttal genre placed by
ancient analogy; one daggered crux \dag\ \textit{est in eo} \dag\
in \S4 [of Lentulus, sense uncertain] preserved literally;
\textit{frequentia} ``crowd of visitors'' kept distinct from
\textit{celebritas} ``frequented spot,'' the \textit{fanum}-cluster
keyword); 12.41 (\textbf{two Greek phrases}
\textit{philaition sumphora} ``how prone misfortune is to find
fault,'' a proverb-like opener, and \textit{proplasma} ``a kind of
preliminary sketch'' --- the \textit{Laudatio Tulliae} as a
sculptor's clay model; Perseus transmits \S\S1, 2, 4 only --- no
\S3 --- preserved as in source). Six Greek phrases; one daggered
crux; gaps preserved.

\item \textbf{Worker B (\textit{Att.} 12.42--12.45, 10--17 May 45
BC, Astura then Tusculanum):} 12.42 (the brief logistical note
with manuscript-break mid-sentence \textit{placet mihi res sic ut
secundum / Othonem nihil magis} preserved across the section
boundary); 12.43 (one daggered passage \dag\ \textit{quod scies
recte illam rem fore levamento, bene facis cumidesse} \dag\
preserved as in 12.32 convention); 12.44 (\textbf{four Greek
phrases}: \textit{sympath\=os} ``sympathetically,''
\textit{eng\=erama} ``a place to grow old in'' [the cluster's
turning point from \textit{fanum} narrowly to retirement-residence
broadly, recurring from 12.29.2], \textit{oikodespotika}
``befitting a master of the household,'' \textit{syntagmata}
``treatises'' --- the first explicit reference to the philosophical
writing as deliberate self-medication, \textit{nec aliter possum
errare quam a miseria mea}; the visceral \textit{contundo animum}
``I have beaten down my spirit''); 12.45 (\textbf{four Greek
phrases}: \textit{ak\=edia} ``listlessness/indifference''
[reserved as Atticus's state, distinct from Cicero's
\textit{dolor}/\textit{maeror}], \textit{anektotera}
``more bearable'' --- the cluster's first retrospective on
\textit{solitudo} as a lower threshold of distress,
\textit{synnaon} ``temple-mate'' [in the dark political joke
\textit{synnaon Quirini malo quam Salutis}, deified Romulus over
Safety personified --- a coded line preserved literally with the
headnote unpacking it], \textit{hypothesis} ``theme''; the
chronological pivot from Astura to Tusculanum). Eight Greek
phrases; one daggered crux.

\item \textbf{Worker C (\textit{Att.} 12.46--12.50, 15--19 May 45
BC, Astura $\rightarrow$ Lanuvium $\rightarrow$ Tusculanum):}
12.46 (\textbf{date correction} from placeholder year-precision
\mbox{-0045-11-15} to day-precision \mbox{-0045-05-15} per Perseus
dateline \textit{Id. Mai. a. 709 (45)} = Ides of May; the
\textit{location\_written: Asturae ld. Mai} entry had silently
encoded the date into the location field --- corrected to plain
\textit{Asturae}; the philosophical-discipline note \textit{vincam
animum} ``I shall master my mind'' continuing 12.44's
\textit{contundo animum} register; the near-Terentian
\textit{exculto enim animo nihil agreste, nihil inhumanum est}
``to a cultivated mind nothing is uncouth, nothing inhuman''
rendered freshly without echoing the famous \textit{Heauton
Timorumenos} line --- worth a corpus-level allusion flag);
12.47 (Lanuvium, 16 May, the \textit{Faberianum nomen}
``Faberian bond'' --- a debt instrument used as currency for the
shrine-property purchase, the cluster's first sustained financial-
instrument language; tricolon \textit{cupido, locuples, heres}
``covetous, wealthy, an heir'' preserved); 12.48 (Lanuvium, 17
May, brief morning note --- Perseus marks the time of writing
\textit{mane} ``in the morning,'' preserved in the headnote;
\textit{divulga} of Hirtius's book rendered ``distribute'' rather
than ``publish,'' on the ongoing-circulation reading); 12.49
(Tusculanum, 19 May, the famous Curtius-consulship paragraph
\textit{o tempora! fore cum dubitet Curtius consulatum petere!}
``what times! that there should be one when Curtius hesitates to
stand for the consulship!'' rendered freshly as ``What times!''
to avoid the Catilinarian shadow --- worth a translator-notes
entry on rendering \textit{o tempora} afresh outside the famous
speech-context; \textit{viri optimi et hominis liberalissimi} of
Caesar rendered straight, leaving the irony for the reader);
12.50 (Tusculanum, 18 May --- chronologically precedes 12.49 by
one day despite the manuscript numbering; clean antithesis
\textit{ut me levarat tuus adventus sic discessus adfiixit} ``as
your coming had relieved me, so your departure has cast me down,''
the \textit{adventus}/\textit{discessus} and
\textit{levare}/\textit{adfligere} pairs added to the cluster's
register). One date + location\_written correction; one daggered
crux carried over from 12.49 phrasing; the closure of the Astura
sweep.
\end{itemize}

\textbf{Wave 2 (1 worker, 4 letters --- Slice U, the Cassius /
Stoic-Epicurean diptych, mid-Dec 46 BC--end Jan 45 BC):}
\begin{itemize}
\item \textbf{Worker D (\textit{Fam.} 15.16--15.19):}
\textit{Fam.} 15.16 (Cicero $\rightarrow$ Cassius, Rome, m.\ Ian.\
45 BC --- the famous \textit{eid\=ola} ``images'' /
\textit{phantasias} ``impressions'' /
\textit{dianoetikas phantasias} ``impressions of thought''
philosophical-tease letter on Cassius's recent Epicurean conversion;
the mock-juridical \textit{interdict} ``\textsc{vi hominibus
armatis}'' ``by men under arms'' [Gaius 4.155] preserved in
small-caps Latin; \textit{hairesei} ``school/sect'' used twice in
mock-praetorian register; Catius the Insubrian Epicurean named as
the inventor of \textit{spectra} as Latin for \textit{eid\=ola});
\textit{Fam.} 15.17 (Cicero $\rightarrow$ Cassius, Rome, 30 Dec.\
46 BC --- the fast-moving political snapshot with \textbf{five
Greek phrases}: \textit{panta peri pant\=on} ``everything about
everything,'' \textit{pros\=opon pole\=os} ``the public face of
the city,'' \textit{adespotoi} ``unattributed'' [of rumours],
\textit{to kalon di' hauto haireton} ``the noble [is] to be
chosen for its own sake'' [the Stoic slogan in its first cluster
appearance, returned on by Cassius in 15.19], \textit{akenospoudos}
``free from idle eagerness''; Brutus's Cisalpine governorship and
Sittius in the post-Munda months; \textit{praeposteros tabellarios}
``back-to-front couriers'' as the rendering choice;
\textit{hasta refrixisset} ``the auction-spear cooled off''
preserving the confiscation-market metaphor); \textit{Fam.} 15.18
(Cicero $\rightarrow$ Cassius, Rome, c.\ mid-Dec 46 BC --- short,
with \textit{phluaron} ``nonsense'' and \textit{spoudazein} ``to
be in earnest''; the brief \textit{convicium Platonis} ``Plato's
rebuke'' rendered calmly rather than as ``a railing''); \textit{Fam.}
15.19 (Cassius $\rightarrow$ Cicero, Brundisium, ex.\ m.\ Ian.\
45 BC --- the only Cassius-voice letter in the cluster: shorter
clauses, fewer suspensions, colloquial oaths preserved at full
force \textit{peream nisi sollicitus sum} ``I will be damned if I
am not [fretting]'' as a register-loosening choice for Cassius
specifically; \textit{antimukt\=erisai} ``to sneer back''
preserved as a rare and pungent Greek verb; canonical Epicurus
quotation \textit{ouk estin h\=ede\=os aneu tou kal\=os kai
dikai\=os z\=en} ``there is no living pleasantly without living
finely and justly'' [the doctrinal centre of the cluster, and
Cassius's reply to 15.17's \textit{to kalon} slogan]; the
philhedonic/philokaloi/philodikaioi tricolon
\textit{phil\=edonoi}, \textit{philokaloi}, \textit{philodikaioi}
``pleasure-lovers, lovers of the noble, lovers of the just'' ---
Cassius's own coinage and the closest the cluster comes to a
synoptic Epicurean reply to Stoic ethics; the closing one-liner
\textit{si vicerit Caesar, celeriter ad te veniam} ``if Caesar has
won, expect me soon'' left bare, the brevity carrying the
political content). Eighteen Greek phrases across the four
letters; no daggered cruxes; the Cassius-voice register shift
worth carrying forward whenever a non-Cicero correspondent voice
appears.
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 16 (one entry):}
\textit{Att.} 12.46 corrected from placeholder year-precision
\mbox{-0045-11-15} to day-precision \mbox{-0045-05-15} per Perseus
dateline \textit{Id. Mai. a. 709 (45)} = Ides of May = 15 May
45 BC. Precision upgraded \texttt{year} $\rightarrow$ \texttt{day}.
The corrupted \texttt{location\_written: Asturae ld. Mai} (the
``ld. Mai'' had leaked in from the date abbreviation in a prior
edit, exactly the same failure mode as the 12.31 ``Asturae iv''
silently corrected in session 15) was silently restored to
\texttt{location\_written: Asturae} in the same edit.

\textbf{Other date observations (no correction needed):}
- \textit{Att.} 12.49 (xiv K. Iun. = 19 May) and 12.50 (xv K. Iun.
= 18 May) form a manuscript-order/date-order disagreement: 12.50
chronologically precedes 12.49 by one day despite the manuscript
numbering. Both \texttt{works.yaml} dates are correct per Perseus;
the chronology builder should be aware that manuscript ordering
within a single book is not always strict chronological order in
this stretch of \textit{Ad Atticum} 12.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{frequentia} / \textit{celebritas}
distinction in \textit{Att.} 12.40.3.} The two words look like
synonyms but are kept deliberately distinct across the cluster:
\textit{celebritas} ``frequented spot'' is the \textit{fanum}-
cluster keyword (the positive value Cicero now wants for the
shrine site, the reversal of 12.13--12.16's
\textit{solitudo}-love); \textit{frequentia} ``crowd of
visitors'' is the negative thing he flees on his estates. Worth a
corpus-level note as the cluster's most precise lexical choice.
\item \textbf{The \textit{eng\=erama} broadening in \textit{Att.}
12.44.2.} The Greek term first appeared in 12.29.2 (Atticus
suggests Cicero buy a property as ``something to grow old in'')
and was paired there with \textit{entaphion} ``something to be
buried in.'' Here in 12.44 the term broadens from a specific
property-purchase to the conceptual goal of the whole project:
not just a shrine but a \textit{place to grow old in}. Worth
flagging as the moment the project takes on its later, broader
character.
\item \textbf{The \textit{contundo} / \textit{vincam} / \textit{exculto}
philosophical-discipline register, \textit{Att.}
12.44.3--12.46.1.} The brutal physical metaphor
\textit{contundo animum} ``I have beaten down my spirit''
(12.44.3) is picked up and softened to \textit{vincam animum}
``I shall master my mind'' (12.46.1), and then sublimated into
the cultivated-mind formula \textit{exculto enim animo nihil
agreste, nihil inhumanum est} (12.46.1, near-Terentian).
The three-step progression --- pound, master, cultivate --- is the
cluster's clearest philosophical-discipline arc. Worth a corpus-
level note.
\item \textbf{The \textit{o tempora!} rendering at \textit{Att.}
12.49.2.} Rendered ``What times!'' deliberately fresh rather than
``O the times!'' to avoid echoing the famous Catilinarian
\textit{o tempora, o mores}. The principle of fresh-rendering of
canonical lines (STYLE.md ``Things to avoid'' \S3) applies even
to Cicero quoting himself --- arguably especially. Worth a
translator-notes entry as a methodological example.
\item \textbf{The Cassius voice register in \textit{Fam.} 15.19.}
Shorter clauses, fewer suspensions, colloquial oaths preserved at
full force (\textit{peream nisi sollicitus sum} ``I will be
damned if I am not''), denser per-word Greek deployment with
technical coinages (the \textit{philhedonic/philokaloi/philodikaioi}
tricolon), military tricolon \textit{scis ... scis ... scis}.
Worth a corpus-level note on non-Cicero correspondent voices: the
project's working assumption that they should sound audibly
different from Cicero's own voice while remaining clean modern
English.
\item \textbf{The canonical Epicurus quotation in \textit{Fam.}
15.19.} \textit{ouk estin h\=ede\=os aneu tou kal\=os kai
dikai\=os z\=en} ``there is no living pleasantly without living
finely and justly'' --- a verbatim Epicurus citation by Cassius.
Worth a corpus-level allusion entry and a glossary note when the
apparatus pass reaches \textit{Fam.} 15.
\item \textbf{The mock-juridical \textsc{vi hominibus armatis} in
\textit{Fam.} 15.16.3.} The all-caps quotation of the praetor's
interdict (Gaius 4.155) preserved in small-caps Latin rather than
rendered in mock-archaic English (``by armed men with violence''
or the like). Worth a translator-notes entry on the choice not to
archaize legal formulae when their Latin form is the joke.
\end{itemize}

\textbf{Suggested next translation batch} (when session 16 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 16:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T continuation: \textit{Att.} 12.51--12.53 +
the \textit{Att.} 13 opening run (13.1, 13.6, 13.7a, 13.9 ff.\ as
they fall by Perseus dating).} The Astura sequence's mid-May
closure (12.50) sets up the Tusculanum-from-Tusculanum letters of
late May and into June 45 BC; the \textit{Att.} 12 tail and
\textit{Att.} 13 opening are the natural continuation. Plan
12--15 letters across 3 workers.
\item \textbf{Slice V (the Paetus winter-46/spring-45 sequence)}:
\textit{Fam.} 9.15--9.23 still pending, filling forward from the
9.5--9.13 cluster drafted earlier. Nine short, witty letters;
parallelisable across 2 workers.
\item \textbf{Slice W (the Torquatus / Lepta / Toranius condolence
continuations of early 45 BC):} \textit{Fam.} 6.2, 6.3, 6.4
(Cicero $\rightarrow$ Torquatus, all year-precision Jan.\ 45 BC),
6.18 (Lepta), 6.21 (Toranius). All short.
\item \textbf{Slice C (substantial speeches blocking the
chronological-gap sweep, dispatch one per session not in
parallel):} \texttt{pro-milone} (52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}. None advanced
this session.
\item \textbf{Slice M (entity-stub enrichment):} the entity
registry still has $\sim$472 stub entries needing real summaries.
\end{itemize}


\textbf{Translation state (post-Cowork-session-15):} 558 / 958
works drafted (\~58.2\%). Latest drafted by deep chronology
unchanged: \textit{Ad Familiares} 9.12 (Cumanum, late November 45
BC). \textbf{Session 15 drafted 25 letters of the Astura grief
sequence in two parallel waves (six workers) and applied one
date correction.} The chronological-gap warning is now
\textbf{166 pending works dated earlier than the latest-drafted}
(down from 191 at the end of session 14). The pointer for ``latest
drafted by date'' did not advance --- session 15 was a
gap-fill sweep through the post-Tullia letters of March--early May
45 BC, all earlier than \textit{Fam.} 9.12.

\textbf{Cowork session 15 --- 25 letters drafted across two
parallel waves of \textit{Ad Atticum} 12 (the Astura grief
sequence, post-Tullia):}

\textbf{Wave 1 (4 workers, 17 letters, 7--25 March 45 BC):}
\begin{itemize}
\item \textbf{Worker A (\textit{Att.} 12.13--12.17, 7--12 March 45
BC):} the opening of the Astura retreat. 12.13 (the \textit{ardor
ille idem urget et manet} grief-burning, the avoidance of
Appuleius's banquets via the \textit{morbi causa} excuse, the
search for a \textit{latibulum et perfugium doloris mei}
``hiding-place and refuge for my grief''); 12.14 (the
\textit{Consolatio} self-reference \textit{feci quod profecto ante
me nemo, ut ipse me per litteras consolarer} ``I have done what
surely no man has done before me, console myself by writing'' as
the moment in the corpus where the \textit{Consolatio} is named as
already begun; the \textit{non ad animum sed ad vultum ipsum}
distinction); 12.15 (the famous \textit{secundum te nihil est mihi
amicius solitudine} ``after you, nothing is more friendly to me
than solitude,'' the day-long retreats into the
\textit{silvam densam et asperam} ``thick and rough woods''); 12.16
(unsectioned in Perseus TEI, wrapped as \texttt{\textbackslash
ciceroSection\{1\}} for parallel-JSON consistency; the
counter-statement \textit{me scriptio et litterae non leniunt sed
obturbant} ``writing and books do not soothe me, but unsettle me''
as the dark twin to 12.14.3); 12.17 (the only pure-business letter
in the opening, with the lone grief mark \textit{quamquam quid ad
me?} ``but what is it to me?''; one-day gap from 12.16 noted in
the headnote). \textbf{Stable cluster register established:}
\textit{solitudo}\,$\rightarrow$\,``solitude''; \textit{ardor}\,$\rightarrow$\,``burning''; \textit{dolor}\,$\rightarrow$\,``grief'' or
``pain''; \textit{maeror}\,$\rightarrow$\,``mourning''/``sorrow'';
\textit{fletus}\,$\rightarrow$\,``weeping''. No Greek; no daggered cruxes.

\item \textbf{Worker B (\textit{Att.} 12.18--12.21, 11--17 March
45 BC):} 12.18 (the quiet Epicurean turn \textit{longum illud
tempus cum non ero} ``that long stretch of time when I shall not
be''); 12.19 (the \textit{sanctius et antiquius} ``more sacred
and older'' formula on the obligation of building the
\textit{fanum} preserved as a Roman-feeling pledge rather than
flattened); 12.20 (the closing \textit{de luctu minuendo} ``on
the lessening of grief'' as the cluster's nearest reference to
the \textit{Consolatio} being now nearly complete); 12.21 (the
longest letter in the sub-batch, with one daggered crux
\dag\ \textit{aut quatenus} \dag\ in \S5 preserved literally;
the \textit{optimum consulem} ``the best of consuls'' sarcasm
rendered with bite via the surrounding \textit{ieiunius}). No
Greek; one daggered crux preserved.

\item \textbf{Worker C (\textit{Att.} 12.22--12.25, 18--22 March
45 BC):} 12.22 (one daggered crux \textit{iis\dag\ usuris}
preserved literally); 12.23 (the dictum \textit{occidimus,
occidimus, Attice} rendered ``we are finished, finished, Atticus''
deliberately fresh, not Shackleton-Bailey's ``I am done for'';
\textbf{one Greek phrase} \textit{politikoi} ``statesmen'' in \S2
on the men of letters not engaging in public life under Caesar);
12.24 (the antiquarian death-of-children \textit{exempla}
gathered for the consolation work, \textit{meas ineptias}
rendered ``my own trifles''); 12.25 (\textbf{two Greek phrases},
both load-bearing: \textit{tetyph\=osthai} ``infatuated/puffed up
by vanity'' as Stoic-Cynic technical term, and the famous
\textit{engēērama} ``something to grow old with'' --- Atticus's
tactful counsel that Cicero choose a property as a retirement
seat; Cicero's reply \textit{actum de illa re} ``that matter is
done with'' the cluster's bleakest two-word rejection of further
life). One crux preserved; three Greek phrases handled.

\item \textbf{Worker D (\textit{Att.} 12.26--12.29, 22--25 March
45 BC):} 12.26 (the elliptical refusal \textit{unam rem ad me
scripsisti; de qua decrevi nihil tibi rescribere} ``you have
written to me about one matter; on which I have determined to
write nothing back to you'' --- almost certainly the
Publilia/remarriage question, recurring across the cluster);
12.27 (the conceptual hinge \textit{sequor celebritatem} ``what I
am after is a frequented spot'' --- Cicero, who had earlier sought
\textit{solitudo}, now wants \textit{celebritas} for the shrine's
site; the central pivot of the \textit{fanum} project); 12.28
(the famous Stoic-precision distinction \textit{maerorem minui,
dolorem nec potui nec, si possem, vellem} ``my mourning I have
lessened; my grief I could not lessen, nor would I, if I could''
--- the canonical \textit{maeror}/\textit{dolor} split between
public mourning and inward pain; one daggered crux \dag\
``to him''\dag\ in \S3 in the Castricius slave-transaction
passage preserved literally); 12.29 (\textbf{two Greek phrases,
the most-quoted of the four:} \textit{engēērama} ``thing to grow
old in'' and \textit{entaphion} ``thing to be buried in,''
deliberately rendered as plain English glosses rather than
something more literary). One crux preserved; two Greek phrases
handled.
\end{itemize}

\textbf{Wave 2 (2 workers, 8 letters, 26 March--4 May 45 BC):}
\begin{itemize}
\item \textbf{Worker E (\textit{Att.} 12.30--12.33):} 12.30 (8
April 45 BC, Astura --- short three-sentence note on the Otho
gardens negotiation; no grief mark); 12.31 (\textbf{date
corrected from \mbox{-0045-04-01} to \mbox{-0045-03-29}} per
Perseus dateline \textit{iv. K. Apr. a. 709 (45)} = 29 March 45
BC; \textbf{location\_written corrupted ``Asturae iv'' silently
corrected to ``Asturae''} --- the ``iv'' had leaked in from the
date abbreviation in a prior edit; the closing \textit{servio
cupiditati et dolori meo ut a te regi velim} ``I am the slave
of my own longing and grief, and so I want to be steered by
you'' as the cluster's most personal admission of dependence on
Atticus); 12.32 (the famous Publilia letter, with one
daggered crux \dag\ \textit{cum Publilio loqueretur} \dag\
preserved literally in \S2 [the textual question is whether the
mother was speaking with Publilius or Publilia herself was
writing after speaking with him]; the autograph mark \textit{haec
ad te mea manu} ``this part to you in my own hand'' as Cicero
shifts to autograph for the Publilia paragraph); 12.33 (one
three-sentence inventory of unmemorable estate lots,
\textit{nescio quotenorum iugerum} ``of so-many iugera apiece
(size unknown)''). One date correction; one location-string
correction; one daggered crux preserved.

\item \textbf{Worker F (\textit{Att.} 12.34--12.37, 30 March--4
May 45 BC):} 12.34 (the brief Sicca-suburbanum announcement of
the planned overnight trip out of Astura toward Rome); 12.35
(\textbf{location\_written = ``fort.\ in suburbano Siccae''}
already correct in works.yaml; Perseus dateline \textit{K.\ vesp.\
aut mane vi Non.\ Mai.\ a.\ 709 (45)} = evening of 1 May or
morning of 2 May 45 BC; works.yaml date \mbox{-0045-05-02}
maintained, worker JSON uses \mbox{-0045-05-01} per the
\textit{vesp.}\ reading --- both within the same overnight
window; \textbf{one Greek phrase} \textit{alog\=os}
``unreasonably'' as Cicero's self-deprecating Stoic/Academic
technical aside admitting his attachment to the word
\textit{fanum} is non-rational; the lex-funeral provision noted
in passing as the discovery that triggered the \textit{fanum}
shift); 12.36 (\textbf{one Greek phrase} \textit{apotheōsin}
``apotheosis'' as the conceptual goal of the shrine project,
deliberately Greek --- Latin had no word for the private-person
cult-deification at this date); 12.37 (the conceptual completion
of the \textit{celebritas} hinge, \textit{celebritatem requiro}
``I am after a frequented spot''; \textit{nescio quo pacto}
``somehow'' preserves the self-puzzled quality of the
\textit{solitudo}-to-\textit{celebritas} reversal). Two Greek
phrases handled.
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 15 (one entry):}
(a) \textit{Att.} 12.31 corrected from day-precision
\mbox{-0045-04-01} to day-precision \mbox{-0045-03-29} per Perseus
dateline \textit{iv. K. Apr. a. 709 (45)} = ante diem IV Kalendas
Apriles = 29 March 45 BC. The 1 April placeholder was off by
three days; precision unchanged (\texttt{day}). The same entry
carried a corrupted \texttt{location\_written: Asturae iv}
(the ``iv'' had leaked in from the date abbreviation in a prior
edit); silently corrected to \texttt{location\_written: Asturae}
in the same edit.

\textbf{Other date observations (no correction needed):}
- The launch prompt assigned to Worker E/F by the PM agent listed
several letters with March/April placeholder dates that turned
out to be wrong; the actual \texttt{meta/works.yaml} entries for
12.35, 12.36, and 12.37 already carried the correct May 45 BC
dates per Perseus. The workers' \texttt{data/parallel/} JSON
files use the Perseus dates throughout, matching works.yaml.
- 12.35 has a half-day ambiguity in the Perseus dateline
(\textit{K. vesp. aut mane vi Non. Mai.}) between 1 May evening
and 2 May morning; works.yaml takes the conservative 2 May
reading, while the worker's JSON took 1 May. Both readings are
valid for the same letter; left as is.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention;
deferred to a future enrichment pass):
\begin{itemize}
\item \textbf{The \textit{maeror}/\textit{dolor} distinction in
\textit{Att.} 12.28.2.} \textit{maerorem minui, dolorem nec
potui nec, si possem, vellem} is the canonical Ciceronian split
between \textit{maeror} (public mourning, the kind one performs
and can modulate) and \textit{dolor} (inward grief, which one
cannot reduce by an act of will and would not, even if one
could). The rendering choice between ``mourning''/``grief'' vs
the more uniform ``grief''/``pain'' shapes the whole Astura
cluster. Worth a corpus-level note.
\item \textbf{The \textit{engēērama}/\textit{entaphion} pair in
\textit{Att.} 12.29.2.} Atticus suggests Cicero purchase a
property as something to grow old in (\textit{engēērama}); Cicero
replies that what he wants is something to be buried in
(\textit{entaphion}). The two Greek words are the most-quoted
moment of the four-letter sub-batch; rendered as plain English
glosses (``thing to grow old in'' / ``thing to be buried in'')
rather than something more literary, on the principle that the
diminutive force of the Greek terms lands in their literal
ordinariness.
\item \textbf{The \textit{solitudo}-to-\textit{celebritas}
reversal across \textit{Att.} 12.13--12.37.} Cicero's opening
position is the famous \textit{secundum te nihil est mihi amicius
solitudine} (12.15.1); by 12.27.1 the position has reversed
into \textit{sequor celebritatem} ``what I am after is a
frequented spot,'' and by 12.37.2 \textit{celebritatem requiro}
``I am after a frequented spot'' has become the engine of the
\textit{fanum} project. The reversal is the cluster's central
arc and worth a corpus-level note on how the shrine project
re-orients the grief.
\item \textbf{The \textit{Consolatio} self-reference in
\textit{Att.} 12.14.3.} \textit{feci quod profecto ante me nemo,
ut ipse me per litteras consolarer} is the cluster's clearest
naming of the now-lost \textit{Consolatio} as a self-addressed
literary act. With 12.20.3 (\textit{de luctu minuendo}), the two
references bracket the composition of the treatise within the
March 45 BC retreat. Worth a corpus-level note when the lost
\textit{Consolatio} is reconstructed for the apparatus pass.
\item \textbf{The Publilia question's elliptical refusals in
\textit{Att.} 12.26.2 and the daggered crux of 12.32.2.} The
\textit{unam rem ad me scripsisti; de qua decrevi nihil tibi
rescribere} of 12.26.2 and the \dag\ \textit{cum Publilio
loqueretur} \dag\ crux of 12.32.2 (autograph paragraph) are the
cluster's two Publilia moments; both are deliberately elliptical
in the Latin and rendered without expansion in the English.
Worth a translator-notes entry on the cluster's discretion
around the marriage's dissolution.
\item \textbf{The \textit{cupiditas}/\textit{dolor} pairing in
\textit{Att.} 12.31.2.} \textit{servio cupiditati et dolori meo
ut a te regi velim} (``I am the slave of my own longing and
grief, and so I want to be steered by you'') is the cluster's
most personal admission of dependence on Atticus; the
\textit{cupiditas} here is the longing for the shrine, not for
remarriage. Worth a corpus-level note on \textit{cupiditas}
under grief, distinct from \textit{cupiditas} under desire.
\end{itemize}

\textbf{Suggested next translation batch} (when session 15 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 15:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item \textbf{Slice T continuation: \textit{Att.} 12.38--12.50}
(the rest of the Astura grief sequence into mid-May 45 BC; the
\textit{fanum} project's culmination and Cicero's brief journey
out of Astura). All short; a worker batch of 10--13 letters
across 2--3 workers is realistic. The cluster's lexicon is now
stable (see session-15 register notes above), making this an
efficient continuation.
\item Slice U (the \textit{Cassius Longinus} / Stoic-Epicurean
diptych of January 45 BC): \textit{Fam.} 15.16, 15.17, 15.18,
15.19. A four-letter cluster on Cassius's philosophical
conversion to Epicureanism; load-bearing for the
political-philosophical network 45--44 BC.
\item Slice V (the Paetus winter-46/spring-45 sequence,
Cicero $\rightarrow$ L.\ Papirius Paetus, the dinner-and-wit
correspondence): \textit{Fam.} 9.15--9.23 (filling forward from
9.5--9.13 drafted earlier).
\item Slice W (the Torquatus / Lepta / Toranius condolence
continuations of early 45 BC): \textit{Fam.} 6.2, 6.3, 6.4
(Cicero $\rightarrow$ Torquatus, all year-precision Jan.\ 45
BC), 6.18 (Lepta), 6.21 (Toranius). All short.
\item Slice C (substantial speeches blocking the chronological-
gap sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item Slice M (entity-stub enrichment): the entity registry
still has $\sim$472 stub entries needing real summaries.
\end{itemize}


\textbf{Translation state (post-Cowork-session-14):} 533 / 958
works drafted (\~55.6\%). Latest drafted by deep chronology:
\textit{Ad Familiares} 9.12 (Cumanum, late November 45 BC ---
date corrected this session per the internal \textit{oratiuncula
pro Deiotaro} reference, which is unambiguous since the
\textit{Pro Deiotaro} was delivered in November 45 BC; works.yaml
formerly carried the year-precision placeholder
\mbox{-0045-01-17}). \textbf{Session 14 drafted 29 letters across
two parallel waves (seven workers) and applied four date
corrections to meta/works.yaml.} The chronology pointer leapt
forward from \textit{Fam.} 9.13 (Dec 46 / early Jan 45 BC) to
\textit{Fam.} 9.12 (late Nov 45 BC) because of the 9.12
re-dating; consequently the chronological-gap warning is now
\textbf{191 pending works dated earlier than the latest-drafted}.
The gap reshapes rather than shrinks --- the leap pulls in
several months of 45 BC pending letters (chiefly the
\textit{Ad Atticum} 12--13 sequence of March--August 45 BC, the
post-Tullia grief correspondence in volume).

\textbf{Cowork session 14 --- 29 letters drafted across two
parallel waves (seven workers):}

\textbf{Wave 1 (4 workers, 15 letters):}
\begin{itemize}
\item \textbf{Worker A (Slice L Dolabella cluster --- 4 letters,
spanning June 48 BC to late 45 BC):} \textit{Fam.} 9.9 (Dolabella
$\rightarrow$ Cicero, June 48 BC, in Caesar's camp at
Dyrrhachium; Dolabella urges Cicero from Caesar's side to
withdraw from the Pompeian cause and rely on Caesarian mercy
--- the only Dolabella-voice letter in book 9; voice rendered
deliberately less periodic, more direct than Cicero's),
\textit{Fam.} 9.10 (Cicero $\rightarrow$ Dolabella, Rome, 30
Dec.\ 46 BC --- the Alexandrian-critic conceit on a money
dispute, with three Greek phrases \textit{obelizei} ``marks with
an obelus,'' \textit{tou poi\=etou \=e parembebl\=emenoi}
``the poet's own or interpolated,'' \textit{sumbi\=ot\=en}
``housemate''; daggered crux \textit{ingentium $\dagger$cularum$\dagger$}
preserved with daggers; the closing \textit{hasta Caesaris
refrixerit} ``the auction-spear has cooled off'' load-bearing as
an indicator of the Caesarian confiscation market going slack),
\textit{Fam.} 9.11 (Cicero $\rightarrow$ Dolabella, at Atticus's
Ficuleanum, 20 April 45 BC --- the gracious 265-word thanks for
Dolabella's condolence on Tullia's death; the load-bearing
hyperbole \textit{vel meo ipsius interitu mallem litteras meas
desiderares} ``I should rather you had missed my letters by
reason of my own death''; the closing \textit{nondum satis sum
confirmatus ad scribendum} ``not yet sufficiently strengthened
for writing''), \textit{Fam.} 9.12 (Cicero $\rightarrow$
Dolabella, Cumanum, \textbf{date corrected from year-precision
\mbox{-0045-01-17} to month-precision \mbox{-0045-11-15}} per
the internal \textit{oratiuncula pro Deiotaro} reference; the
famous self-deprecatory \textit{levidense crasso filo} ``of
light-woven cloth of coarse thread'' weaving metaphor preserved
literally; the closing \textit{aliorum infamet iniuriam} kept
deliberately ambiguous on the \textit{iniuria} suffered).

\item \textbf{Worker B (Slice P Plancus / Acilius / Allienus
continuations --- 4 letters):} \textit{Fam.} 13.29 (Cicero
$\rightarrow$ L.\ Munatius Plancus, governor of one of the
Gauls, Rome, late 47 BC --- the substantive 870-word
recommendation; the warmest-tier formula \textit{rogo et a te
ita peto, ut maiore cura, maiore studio nullam possim}; the rare
Pharsalus self-defence \textit{quod fuerim moderatior
temperatiorque quam in ea parte quisquam}; HS X$\_$X$\_$X$\_$
numeric notation preserved), \textit{Fam.} 13.30, 13.31
(M$'$.\ Acilius Glabrio, Sicily, 46 BC --- short recommendation
pair continuing the cluster of session 13's worker B; 13.31
carries the explicit \textit{neque id ambitione adductus facio}
disavowal echoing 13.32, worth a translator-notes entry on the
cluster-internal \textit{ambitio} callback), \textit{Fam.} 13.78
(Cicero $\rightarrow$ A.\ Allienus, late 46 BC --- short letter
opening the Allienus succession to Acilius; the tricolon closer
\textit{complectare, diligas, in tuis habeas} ``embrace him,
hold him dear, count him among your own'' the warmest tier in
the cluster; the remark \textit{quod non multis contigit,
Graecis praesertim} ``what has fallen to the lot of not many,
and especially few Greeks'' a noteworthy Ciceronian observation
on the rarity of his Greek intimates).

\item \textbf{Worker C (Slice R Servilius / Sulpicius
continuations --- 4 letters):} \textit{Fam.} 13.66 (Cicero
$\rightarrow$ P.\ Servilius Isauricus, Asia, ca.\ early Feb.\
45 BC --- recommendation for A.\ Caecina, with the
\textit{clementia conlegae tui} ``the clemency of your
colleague'' [scil.\ Caesar] preserved; the day-precision dating
sits right at the moment of Tullia's death noted in the
headnote without sentimentalising the routine recommendation
tone), \textit{Fam.} 13.67 (Cicero $\rightarrow$ Servilius now
\textbf{propraetor}, Rome, ca.\ Dec.\ 46 BC --- title shift in
the salutation; one Greek phrase \textit{treis dioik\=eseis}
``three Asiatic districts'' for the three administrative
divisions of Asia; the bitter epigram \textit{non te fugit
$\ldots$ quam multi grati reperiantur} ``how few are found to be
grateful''), \textit{Fam.} 13.72 (Cicero $\rightarrow$
Servilius \textit{conlegae}, Asia, ca.\ May 46 BC ---
recommendation for the heirs of C.\ Vennonius citing a
\textit{senatus consultum} preserved as ``decree of the Senate
concerning the heirs of C.\ Vennonius''; Caerellia introduced
as ``my close friend''), \textit{Fam.} 13.77 (Cicero
$\rightarrow$ Ser.\ Sulpicius Rufus, \textit{imperator},
Achaia, \textbf{date corrected from \mbox{-0046-10-06} year-
precision to month-precision \mbox{-0046-11-15}} per Perseus
dateline \textit{mense intere. pr. a. 708} = first intercalary
month of 46 BC ($\approx$ mid-November on the unreformed
calendar). Upstream salutation corruption \texttt{n SVLPICIO
IMfl} silently restored to \texttt{CICERO SULPICIO IMP. S.} in
the English file per cluster convention; the load-bearing
personal sentence \textit{res ipsa parva, sed animi mei dolor
magnus est} ``the matter in itself is small, but the pain to my
mind is great'' on the librarian-slave Dionysius and Cicero's
treasured \textit{bibliotheca}, worth a translator-notes entry
on the cluster's only sentence of domestic distress).

\item \textbf{Worker D (Slice S post-Pharsalus consolation
cluster --- 3 load-bearing letters):} \textit{Fam.} 6.1
(Cicero $\rightarrow$ A.\ Manlius Torquatus, Rome, ex.\ m.\
intercal.\ post.\ a.\ 708 [late second-intercalary month of 46
BC, $\approx$ mid-Feb.\ on the unreformed calendar] ---
substantive 1,156-word consolatory letter to a Pompeian in
continued exile; the \textit{togati potius potentiam quam
armati victoriam} ``the power of the man in the toga rather
than the victory of the man in arms'' antithesis preserved; the
Stoic-indifferents formulation \textit{omnia humana placate et
moderate feramus} anticipating \textit{De Officiis} flagged in
the headnote), \textit{Fam.} 4.5 (\textbf{Ser.\ Sulpicius Rufus
$\rightarrow$ Cicero}, Athens, mid-March 45 BC --- the famous
consolation letter on Tullia's death; 1,174 words; voice held
to Stoic-jurist register, not Cicero's; the load-bearing
\textit{homunculi} diminutive rendered ``we, us little men'' to
preserve the deflationary force; the ruined-cities passage
``so many corpses of towns lie cast down together''
\textit{oppidum cadavera} kept literal; the
\textit{unius mulierculae animula} double diminutive
``the little life-breath of one little woman'' preserved
deliberately uncomfortable; the diatribe shape
\textit{malum est liberos amittere. malum;} kept in the
self-quoting-objection-and-answer pattern; renderings stress-
tested to avoid Melmoth / Shuckburgh / Williams echoes per
STYLE.md \S Things to avoid), \textit{Fam.} 4.6 (Cicero
$\rightarrow$ Servius, at Atticus's Ficuleanum, mid-April 45
BC --- 698-word reply to 4.5; the \textit{ea me solacia
deficiunt} ``those consolations fail me'' admission of the
philosophical apparatus failing him in the moment; the
\textit{hoc tam gravi vulnere $\ldots$ recrudescunt} ``even
those griefs which had seemed to have healed are breaking
open again'' medical metaphor preserved; the chiastic
\textit{domus iam consolari potest nec domesticum res publica}
``home can no longer console the grief I take from the
commonwealth, and the commonwealth cannot console the grief
I take from home'' preserved as chiasm; the deliberately
periphrastic naming of Caesar in \S3 as ``the will of one
man --- a man of prudence, of generous bearing, $\ldots$ not
unfriendly to me, and a particularly warm friend to you''
preserved without ever saying his name; the political register
of \textit{quiescere} under autocracy rendered ``keeping
quietly,'' not ``rest'' or ``leisure'').
\end{itemize}

\textbf{Wave 2 (3 workers, 14 letters):}
\begin{itemize}
\item \textbf{Worker E (Marcellus exile cluster --- 5 letters,
Aug.--Nov.\ 46 BC, bracketing the \textit{Pro Marcello}):}
\textit{Fam.} 4.7 (Cicero $\rightarrow$ M.\ Marcellus at
Mytilene, 13 Aug.\ 46 BC --- the cluster opener; the
\textit{victi sumus $\ldots$ fracti certe et abiecti} ``we were
beaten, then; or, if standing cannot be beaten, we were broken
at any rate'' antithesis on \textit{dignitas / vinci}; the
\textit{ita late pateat eius potestas $\ldots$ ut terrarum
orbem complexa sit} ``extends so widely as to embrace the
whole globe'' as the cluster's central political claim;
\textit{medium quoddam tuum consilium fuit} ``yours has been a
middle course'' as structural pivot), \textit{Fam.} 4.8 (Cicero
$\rightarrow$ Marcellus, mid-Aug.\ 46 --- short follow-up; a
daggered crux at end of \S1 \textit{omnia debere $\dagger$tua
causa, sed causa quoque, etiam quae non possim} preserved with
daggers; conditional pairing \textit{si sit aliqua res publica
$\ldots$ sin autem nulla sit}), \textit{Fam.} 4.9 (Cicero
$\rightarrow$ Marcellus, 13 Aug.\ 46 --- same-day pair to 4.7;
the load-bearing Stoic commonplace \textit{tempori cedere, id
est necessitati parere, semper sapientis est habitum} ``to give
way to the times --- that is, to obey necessity --- has always
been held the wise man's part'' flagged as the engine of the
\textit{Pro Marcello}; the parallelism \textit{dicere fortasse
quae sentias non licet, tacere plane licet}; the climax
\textit{omnia sunt misera in bellis civilibus $\ldots$ sed
miserius nihil quam ipsa victoria}; the four-part contrastive
\textit{si fuit magni animi $\ldots$ stultum est nolle
privata}), \textbf{\textit{Fam.} 4.10} (\textbf{salutation
corrected from the brief's assumption}: the Latin
\texttt{CICERO MARCELLO S.} is unambiguous --- this is
\textbf{Cicero $\rightarrow$ Marcellus}, not Marcellus $\rightarrow$
Cicero per the launch brief's mistake. Rendered accordingly;
short letter set after the recall has taken effect; the wry
\textit{ne te delectet tarda decessio} ``that this slow
departure of yours is taking on a charm of its own''
suspecting Marcellus is dragging his feet even after the
recall), \textit{Fam.} 4.11 (\textbf{M.\ Marcellus $\rightarrow$
Cicero}, Mytilene, mid-Oct.\ 46 BC --- the only Marcellus-voice
piece in the cluster; voice rendered drier, shorter-clausal,
Ciceronian periodicity flattened; \textit{facile et aequo animo
carebam} ``I could do without them easily and without
complaint'' as the heart of \S2's Stoic understatement;
\textit{re tibi praestabo} ``I will prove it to you in the
fact'' as characteristically clipped).

\item \textbf{Worker F (Sulpicius / Servius / Allienus / Rex
recommendation continuations --- 5 letters):} \textit{Fam.}
13.17 (Cicero $\rightarrow$ Servius, ca.\ early Oct.\ 46 BC ---
M$'$.\ Curius of Patrae; the three-tier conditional escalation
capped by the formal pledge formula \textit{spondebo enim tibi
vel potius spondeo in meque recipio} ``I will pledge to you ---
or rather, I do pledge, and I take it upon myself'' with the
tense-flip preserved), \textit{Fam.} 13.18 (Cicero $\rightarrow$
Servius, ca.\ early Nov.\ 46 BC --- thank-you for a volunteered
favour to Atticus on Epirus; the small-scale \textit{praeteritio}
``I shall not ask $\ldots$ I shall not thank $\ldots$ and now I
shall do both'' preserved; upstream salutation \texttt{SERVIO. S}
[stray period] silently rationalised to \texttt{CICERO SERVIO S.}
per cluster convention), \textit{Fam.} 13.19 (Cicero $\rightarrow$
Servius, ca.\ early Dec.\ 46 BC --- Lyso of Patrae, Pompeian
pardoned through Cicero's intercession with Caesar with Caesar
himself sending Servius a covering letter [a rare detail in the
\textit{commendaticia} genre]; the unusual closing inversion
of obligation [Cicero's standing with Lyso, not Servius's with
Cicero, at stake] worth a translator-notes entry),
\textit{Fam.} 13.79 (Cicero $\rightarrow$ D.\ Allienus, ca.\
early Dec.\ 46 BC --- substantive occasion is Allienus's
succession to Acilius in Sicily; \textbf{works.yaml date
\mbox{-0046-11-07} maintained but Perseus dateline
\textit{in.\ a.\ 708} flagged as substantive-date discrepancy
in the JSON}; the closing reduplication \textit{te rogo $\ldots$
te vehementer etiam atque etiam rogo} preserved),
\textit{Fam.} 13.52 (Cicero $\rightarrow$ \textbf{Rex}
[\textit{identity uncertain}; conventionally Q.\ Marcius Rex
propraetor in Asia/Cilicia but editors hedge], Rome, mid-Sept.\
46 BC --- A.\ Licinius Aristoteles of Malta, another pardoned
Pompeian paralleling Lyso in 13.19; \textit{antiquissimus
hospes} ``host of the oldest standing'' tier-marker preserved;
the bare-cognomen vocative \textit{fac igitur, mi Rex} as the
easy-intimacy register confirming Rex is no stranger).

\item \textbf{Worker G (Caecina exile cluster --- 4 letters,
Oct.--Dec.\ 46 BC, the policy-substantive companion to the
Marcellus and Ligarius clusters):} \textit{Fam.} 6.6 (Cicero
$\rightarrow$ A.\ Caecina, ca.\ 1 Oct.\ 46 BC --- the cluster's
substantive 1,580-word policy letter, 13 sections; the
Amphiaraus tag \textit{prudens et sciens ad pestem ante oculos
positam} ``knowing and aware, to the destruction set before my
eyes'' preserved with tragic register; augural technical terms
preserved Roman --- \textit{cantu sinistro oscinis} ``sinister
note of the singing-bird,'' \textit{tripudiis solistimis aut
soniviis} ``the most full-footed beat or sound of the sacred
chickens''; the diplomatic recasting of Caecina's
anti-Caesarian pamphlet \textit{praeclaro illo libro
`querelarum' tuarum} as a portrait of Caesar's clemency ---
the central political maneuver of the letter --- kept dry in
the English; the imagined hostile interlocutor rendered as
quoted objection for rhythm), \textit{Fam.} 6.5 (Cicero
$\rightarrow$ Caecina, \textbf{date corrected from
\mbox{-0046-12-15} to \mbox{-0046-12-25}} per Perseus
\textit{ex.\ m.\ Dec.}; a daggered crux $\dagger$ at start of
\S3 \textit{qua re ad eam spem} preserved with translator-note
on the editorial reading), \textit{Fam.} 6.7 (\textbf{Caecina
$\rightarrow$ Cicero}, Sicily, mid-Dec.\ 46 BC --- 890-word
reply, the cluster's one inward-facing voice; voice held to
learned-equal-under-unequal-fortune, not subservient; the
antiquarian tricolon of ``corrections'' \textit{mendum
scripturae litura tollatur, stultitia fama multetur, meus
error exsilio corrigitur} preserved as ``where a fault in the
writing is taken away by the eraser, where folly is fined by
reputation, my own error is corrected by exile'' with
\textit{exsilio corrigitur} as the climactic third term;
\textit{armatus adversario male dixi} ``with arms in my hand,
I spoke ill of an adversary'' as Caecina's precise legal-style
self-summary of his crime; the staircase-as-failed-text image
preserved literally as the most ``literary'' moment of the
letter; the wry observation that Cicero ``takes cover behind
Brutus'' even in the dialogue-frame of the \textit{Orator}),
\textit{Fam.} 6.8 (Cicero $\rightarrow$ Caecina,
\textbf{date corrected from \mbox{-0046-12-15} to
\mbox{-0046-12-05}} per Perseus \textit{in.\ m.\ Dec.}; the
Balbus / Oppius pair kept unexpanded with the headnote glossing
them as ``Caesar's regular men of business in his absence''; a
referenced appendix-letter-of-recommendation noted as not
preserved in the manuscript text).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 14 (four entries):}
(a) \textit{Fam.} 9.12 corrected from year-precision
\mbox{-0045-01-17} (precision \texttt{year}) to month-precision
\mbox{-0045-11-15} (precision \texttt{month}) per the internal
\textit{oratiuncula pro Deiotaro} reference, which is
unambiguous: the \textit{Pro Deiotaro} was delivered in November
45 BC, so 9.12 must postdate it. The January placeholder was
off by ten months.
(b) \textit{Fam.} 13.77 corrected from year-precision
\mbox{-0046-10-06} (precision \texttt{year}) to month-precision
\mbox{-0046-11-15} (precision \texttt{month}) per Perseus
dateline \textit{mense intere.\ pr.\ a.\ 708} = first
intercalary month of 46 BC, which on the unreformed Roman
calendar of 46 BC falls roughly in mid-November. The October
placeholder was within the first intercalary month period but
the dateline pins it more precisely; precision upgraded from
\texttt{year} to \texttt{month}.
(c) \textit{Fam.} 6.5 refined from month-precision
\mbox{-0046-12-15} (mid-month) to month-precision
\mbox{-0046-12-25} (end of month) per Perseus dateline
\textit{ex.\ m.\ Dec.\ a.\ 708 (46)}. Precision unchanged
(\texttt{month}); date-within-month shifted to reflect Perseus's
end-of-month indicator.
(d) \textit{Fam.} 6.8 refined from month-precision
\mbox{-0046-12-15} (mid-month) to month-precision
\mbox{-0046-12-05} (early month) per Perseus dateline
\textit{in.\ m.\ Dec.\ a.\ 708 (46)}. Precision unchanged
(\texttt{month}); date-within-month shifted to reflect Perseus's
beginning-of-month indicator.

\textbf{Latin-file opener corruption flagged this session (not
corrected; deferred to future fetch-script enhancement):}
\textit{Fam.} 13.77 carries the upstream salutation
\texttt{M.\ CICERO S.\ D.\ n SVLPICIO IMfl} where the
conventional form is \texttt{CICERO SULPICIO IMP.\ S.} (or
\texttt{Ser.\ SULPICIO IMP.\ S.\ D.}). The ``n'' is most
plausibly an OCR/scribal artefact for the praenomen
abbreviation \texttt{Ser.} (Servius); ``IMfl'' is \texttt{IMP.}
The English file silently restores per cluster convention;
the Latin file preserves the upstream form per general
discipline. \textit{Fam.} 13.18 carries the upstream
salutation tail \texttt{SERVIO.\ S} (stray period) silently
rationalised to \texttt{CICERO SERVIO S.} in the English file.
Both are upstream Perseus TEI artefacts.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention; the
PM or a future enrichment pass should consolidate):
\begin{itemize}
\item \textbf{The Servius / Cicero consolation pair (\textit{Fam.}
4.5 + 4.6) as load-bearing pair.} These two letters are among
the most-read pieces of Latin prose Cicero wrote, and the pair
is one of the great consolation-correspondences of Latin
literature. The headnotes cross-link them explicitly. The
\textit{homunculi} / \textit{oppidum cadavera} /
\textit{mulierculae animula} renderings in 4.5 and the
\textit{ea me solacia deficiunt} / \textit{recrudescunt} /
periphrastic-Caesar renderings in 4.6 should be preserved
across any future revision. Worth a corpus-level note on the
voice-distinction between Servius's Stoic-jurist register and
Cicero's grieving-philosopher register in the pair.
\item \textbf{The Marcellus exile cluster as the \textit{Pro
Marcello}'s epistolary companion.} \textit{Fam.} 4.7--4.11
bracket the September 46 BC speech; the headnotes position
them explicitly. The Stoic commonplace \textit{tempori cedere}
in 4.9 is the engine of the speech and worth a cross-reference
in any future apparatus pass.
\item \textbf{The Caecina exile cluster as the substantive
policy-letter cluster.} \textit{Fam.} 6.6 is Cicero's most
candid public-private overlap on Caesar's likely course in
late 46 BC, and the cluster (6.5 / 6.6 / 6.7 / 6.8) sits
between the Marcellus and Ligarius letters in the bound-volume
narrative of mercy correspondence. Caecina's reply in 6.7 ---
the cluster's one inward-facing voice --- preserves a
deliberately learned-equal-under-unequal-fortune register.
\item \textbf{The salutation correction for \textit{Fam.} 4.10}
(Cicero $\rightarrow$ Marcellus, not Marcellus $\rightarrow$
Cicero). The launch brief misidentified the sender; the Latin
salutation \texttt{CICERO MARCELLO S.} is unambiguous. The
post-recall content (Theophilus setting out, anticipating
Marcellus's return, the wry \textit{tarda decessio}) confirms.
Worth a translator-notes entry as a guide for any future
re-pass of the cluster.
\item \textbf{The \textit{Pro Deiotaro} dating peg for
\textit{Fam.} 9.12.} The letter's internal
\textit{oratiuncula pro Deiotaro} reference is the
chronological anchor; the speech itself dates to November 45
BC, so 9.12 must postdate. Worth a methodological note on
preferring internal references to placeholder month/year
metadata.
\item \textbf{The Caesarian intercalary calendar continues to
shape late-46 BC datelines (\textit{Fam.} 13.77, 6.1).} 13.77
sits in the first intercalary month ($\approx$ mid-November);
6.1 sits at the end of the second intercalary month
($\approx$ mid-February of the unreformed calendar). The
session-13 note on the calendar should be extended.
\item \textbf{The \textit{quiescere} register under autocracy
in \textit{Fam.} 4.6.} Cicero's \textit{non agendi aliquid,
sed illius concessu et beneficio quiescendi} ``not for any
action of our own, but for keeping quietly, by his concession
and favour'' is the cleanest statement in the corpus of the
political register of \textit{quiescere} under Caesarian
clemency. The verb will recur; worth a corpus-level note.
\item \textbf{The Alexandrian-critic conceit in \textit{Fam.}
9.10.} Cicero applies obelizing-and-interpolation language to
a money dispute as a sustained metaphor; the three Greek
phrases \textit{obelizei}, \textit{tou poi\=etou \=e
parembebl\=emenoi}, and \textit{sumbi\=ot\=en} all belong to
the same conceit. Worth a translator-notes entry on the
metaphor's coherence across the letter.
\item \textbf{Single-section Latin source files this session.}
\textit{Fam.} 13.30, 13.31, 13.52, 13.67, 13.70 [drafted last
session], 13.79 are all single-section in Perseus's TEI. The
English supplies \texttt{\textbackslash ciceroSection\{1\}}
markers for parallel-JSON consistency where appropriate.
\end{itemize}

\textbf{Suggested next translation batch} (when session 14 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 14:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item Slice T (the \textit{Ad Atticum} 12 grief sequence,
March--early May 45 BC --- the post-Tullia withdrawal at
Astura): \textit{Att.} 12.13--12.50 (in chronological order).
These are short, dense day-by-day letters from Astura and the
Ficuleanum; many are single-paragraph notes. A worker batch of
8--10 letters is realistic given their length. Together they
form the textual record of Cicero's grief and the project of
the \textit{Consolatio} (now lost).
\item Slice U (the \textit{Cassius Longinus} / Stoic-Epicurean
diptych of January 45 BC): \textit{Fam.} 15.16 (Cicero
$\rightarrow$ Cassius), 15.17 (Cicero $\rightarrow$ Cassius),
15.18 (Cicero $\rightarrow$ Cassius, end of 46 BC), 15.19
(Cassius $\rightarrow$ Cicero, Brundisium, late January 45 BC).
A four-letter cluster on Cassius's philosophical conversion to
Epicureanism; load-bearing for the political-philosophical
network 45--44 BC.
\item Slice V (the Paetus winter-46/spring-45 sequence, Cicero
$\rightarrow$ L.\ Papirius Paetus, the dinner-and-wit
correspondence): \textit{Fam.} 9.15--9.23 (filling forward
from 9.5--9.7 drafted in session 13 and 9.10--9.13 drafted
this session and last). Mostly short, all in the established
Paetus register.
\item Slice W (the Torquatus / Lepta / Toranius condolence
continuations of early 45 BC): \textit{Fam.} 6.2, 6.3, 6.4
(Cicero $\rightarrow$ Torquatus, all year-precision Jan.\ 45
BC), 6.18 (Lepta), 6.21 (Toranius). All short. Together they
fill out the consolatio register established by 6.1 / 4.5 /
4.6 of this session.
\item Slice C (substantial speeches blocking the chronological-
gap sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. None advanced this session.
\item Slice M (entity-stub enrichment): the entity registry
still has $\sim$472 stub entries needing real summaries; can
be batched aggressively in parallel ($\sim$50/worker, no
inter-batch contention).
\end{itemize}


\textbf{Translation state (post-Cowork-session-13):} 504 / 958
works drafted (\~52.6\%). Latest drafted by deep chronology:
\textit{Ad Familiares} 9.13 (end of 46 BC or beginning of 45 BC,
Rome). \textbf{Session 13 pushed the chronology pointer forward from
\textit{Fam.} 9.5 (early June 46 BC) to \textit{Fam.} 9.13 (Dec.\ 46
BC / early Jan.\ 45 BC) by drafting 26 letters across two parallel
waves of recommendation-letter clusters plus two substantive Varro
literary-otium continuations and a high-interest early-46 BC trio
(Dolabella, Brutus, Ligarius). The chronological-gap warning is
now \textbf{78 pending works dated earlier than the latest-drafted}:
the pointer moved seven months forward, so the gap reshapes (some
late-46 BC pending cleared, more 45 BC pending now in scope). Three
\texttt{meta/works.yaml} date corrections committed (see below).}

\textbf{Cowork session 13 --- 26 letters drafted across two
parallel waves (seven workers):}

\textbf{Wave 1 (4 workers, 15 letters --- chronological-gap fill
in early/mid 46 BC):}
\begin{itemize}
\item Worker A (4 letters of the Servius cluster to Ser.\ Sulpicius
Rufus, proconsul of Achaia 46 BC; standard \textit{commendaticiae}
register): \textit{Fam.} 13.20 (Rome, year-precision 46 BC ---
the very short note recommending L.\ Manlius Sosis with no
\texttt{\textbackslash ciceroSection} division; preserved as
single-section per the Latin's lack of subdivision), \textit{Fam.}
13.21 (Rome, 46 BC --- the M.\ Aemilius Avianius / Hammonius pair,
deploying the load-bearing \textit{ut si a me manumissus esset}
formula ``as if he had been freed by my own hand''; corrupt
\textit{molestissimis temporibus} preserved as ``in my most
distressing season''), \textit{Fam.} 13.22 (Rome, 46 BC --- the
co-recommendation of T.\ Manlius at Thespiae alongside Varro Murena;
the doubled \textit{tribuere} construction \textit{quantum cui
tribuisti plurimum} unpacked carefully), \textit{Fam.} 13.23 (Rome,
46 BC --- L.\ Cossinius and his freedman Anchialus, with the
\textit{tribuli tuo} ``your tribesman'' technical voting-tribe
sense glossed in the headnote).

\item Worker B (4 letters of the Acilius cluster to M$'$.\ Acilius
Glabrio, proconsul of Sicily 46 BC; standard \textit{commendaticiae}
register harmonised with Worker A): \textit{Fam.} 13.32 (Rome,
46 BC --- the \textit{ambitio quadam commendationes meas exaequare}
canvassing metaphor preserved as ``levelling out my recommendations
by some sort of canvasser's habit''), \textit{Fam.} 13.33 (Rome,
46 BC --- with a stray Perseus punctuation artefact
\textit{Hilarus, .\ Antigonus, Demostratus} flagged in the JSON;
\textit{illius ordinis} rendered ``any man of his rank''),
\textit{Fam.} 13.34 (Rome, 46 BC --- \textit{avitum hospitium}
``inherited tie of hospitality''; the \textit{et adiumento et
ornamento} doublet preserved), \textit{Fam.} 13.35 (Rome, 46 BC
--- Philoxenus's enrolment in the Transpadane colony Novum Comum
under Caesar; \textit{non vulgaris} tier-marker preserved with
explicit headnote gloss as a recognised genre tier).

\item Worker C (4 letters of the Servilius cluster to P.\ Servilius
Isauricus, proconsul of Asia 46 BC, with the \textit{conlegae}
formula marking both as ex-consuls): \textit{Fam.} 13.68 (Rome,
\textbf{date corrected from year-precision -0046-01-25 to
month-precision -0046-09-05} per Perseus dateline \textit{circ.\
med.\ in.\ Sept.\ a.\ 708 (46)} = mid-early September 46 BC ---
the longest letter of the Servilius cluster, with the
\textit{magni referebat te interesse} pivot on Caesar's planning
versus the senate's deliberations), \textit{Fam.} 13.69 (Rome,
46 BC --- daggered crux \textit{non $\dagger$vulgare nec
ambitiose} rendered with the editorial conjecture \textit{vulgariter} 
in adverbial sense), \textit{Fam.} 13.70 (Rome, 46 BC --- salutation
trailing \textit{S.\ R} silently emended to \textit{S.\ P.} per the
cluster convention; single-section Latin), \textit{Fam.} 13.71
(Rome, 46 BC --- the \textit{illo miserrimo tempore} exile reference
of 58--57 BC handled in the headnote rather than the body).

\item Worker D (3 substantive letters of high interest, early 46
BC --- the Dolabella / Brutus / Ligarius cluster): \textit{Fam.}
9.13 (Rome, \textbf{date corrected from year-precision -0046-02-18
to month-precision -0046-12-15} per Perseus dateline \textit{ex.\
a.\ 708 (46) aut in.\ a.\ 709 (45)} = end of 46 BC or beginning
of 45 BC; the Scapula-Pompeius Spanish-war references in the body
confirm late 46 BC, and place this letter not in February 46 but
on the eve of the Munda campaign; the \textit{vix equestris}
``barely of equestrian rank'' technical census-marker noted),
\textit{Fam.} 13.10 (Rome, beginning of 46 BC --- the recommendation
to M.\ Junius Brutus of M.\ Terentius (Varro Gibba), Brutus's
quaestor in Cisalpine Gaul; the institutional \textit{quaesturae
coniunctionem liberorum necessitudini proximam} formula ``the
quaestor-praetor bond is next to that of one's own children''
preserved literally; \textit{versatus in utrisque subselliis}
``appeared on both sides of the bench''; \textit{societates
publicorum} rendered ``partnerships of the public revenues''
rather than the technical ``tax-farming companies''),
\textit{Fam.} 6.14 (Rome, ``a.\ d.\ v K.\ intercal.\ priores a.\
708 (46)'' per Perseus dateline = 5 days before the kalends of
the first Caesarian intercalary month of 46 BC, $\approx$ 26
November 46 BC in the unreformed Roman calendar; the famous moving
letter to Q.\ Ligarius after Cicero's audience with Caesar on his
behalf, anticipating the \textit{Pro Ligario}; the closing antithesis
\textit{si turbidissima sapienter ferebas, tranquilliora laete
feras} preserved as ``if you bore the wildest waters wisely,
that you bear the calmer ones with gladness''; \textit{ex oratione
Caesaris ... ex oculis et vultu} pivot from verbal reply to face
preserved as a parallel construction).
\end{itemize}

\textbf{Wave 2 (3 workers, 11 letters --- chronological forward
push from June 46 BC, plus mid-46 BC recommendation continuations):}
\begin{itemize}
\item Worker E (2 substantive Varro literary-otium continuations,
late May / late June 46 BC --- the post-Pharsalus correspondence
extending the voice established in \textit{Fam.} 9.1--9.5):
\textit{Fam.} 9.7 (Rome, \textbf{date corrected from year-precision
-0046-08-12 to month-precision -0046-05-30} per Perseus dateline
\textit{ex.\ m.\ Maio a.\ 708 (46)} = end of May 46 BC; the letter
belongs BEFORE \textit{Fam.} 9.5 and 9.6 in chronology even though
Perseus's canonical numbering places it after --- Perseus orders
book 9 by manuscript sequence, not by date; three Greek phrases
\textit{sun te du' erch\=omen\=o} (Iliad 10.224 Diomedes-to-Nestor
``when two go together''), \textit{apoproēgmena} (the Stoic
``dispreferred'' technical antonym of \textit{proēgmena}),
\textit{polloi math\=etai kreissones didaskal\=on} (``many pupils
outdo their teachers''); the half-line \textit{quid hic mihi
faciet patri?} read as an iambic senarius drawn from the comic
stage about the Caesarian killings in Africa; \textit{tempori
serviendum est} ``one must serve the time'' as the load-bearing
programmatic line for the whole Varro-otium sequence),
\textit{Fam.} 9.6 (Rome, between 20 and 25 June 46 BC per Perseus
dateline \textit{inter xii et vii K.\ Quint.\ a.\ 708 (46)} ---
the substantive 670-word June letter; two daggered cruxes in §6
preserved with the editorial conjectures; \textit{cum opera nostra
patria sive non possit uti sive nolit} ``since our country either
cannot or will not use our service'' preserving the precise
disjunction Cicero is aware of in the Caesarian regime).

\item Worker F (5 letters of the Servius mid-46 cluster --- the
Worker A continuation): \textit{Fam.} 13.24 (Lyso of Patrae,
renewed-after-misunderstanding, 340 words), \textit{Fam.} 13.25
(Hagesaretus of Larisa, single-paragraph 95-word letter; single-
section Latin), \textit{Fam.} 13.26 (Mescinius inheritance from
Mindius at Elis; \textit{quasi commendaticias} ``so to say, in the
manner of letters of recommendation'' meta-commendatio formula
preserved), \textit{Fam.} 13.27 (Hammonius/Avianius thanks pair to
13.21, plus Servius's son grace note as cluster-closing seal;
\textit{`DE EADEM RE ALIO MODO'} known lacuna in §1 with supplied
verb flagged), \textit{Fam.} 13.28 (Mescinius thanks plus Oppia
plus \textit{cautio amplius} pair to 13.26; Latin legal formula
\textit{amplius eo nomine non peti} ``no further claim shall be
made under that head'' preserved verbatim in italic Latin with
parenthetical gloss; \textit{studia illa nostra ... nunc etiam
vivimus} ``those studies of ours, in which we formerly took delight
and by which we now actually live'' as the post-Pharsalus retreat-
into-philosophy programmatic line).

\item Worker G (4 letters of the Acilius mid-46 cluster --- the
Worker B continuation): \textit{Fam.} 13.36 (Demetrius Megas;
\textit{non vulgaris}-tier marker \textit{maiore studio neminem
commendarim}; opener corruption \textit{CICERO ACILIO PROCONSVLI
$\$$} silently restored to \textit{S.}\ per the cluster convention
--- the Latin source itself is uncorrected),
\textit{Fam.} 13.37 (Hippias of Calacte; \textit{publice
possidentur alieno nomine} ``held in public ownership under
another man's name'' preserved with the ambiguity between
confiscation by the town treasury and irregular registration;
\textit{quoquo modo autem se res habet} ``but in any event,
however the matter stands'' as a recurring formula across the
cluster), \textit{Fam.} 13.38 (Lucius Bruttius; dateline reads
\textit{iit videtur} where Perseus has an OCR-induced corruption
of \textit{ut videtur}, date itself unambiguous 46 BC),
\textit{Fam.} 13.39 (M.\ Titurnius Rufus; \textit{est igitur in
tua potestate ut ille in me satis sibi praesidi putet esse} ``It
lies in your hands, then, to see that he reckons he has in me a
sufficient protection'' as the most candid sentence in the
cluster on the dependency of a recommendation on the recipient's
willingness).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 13 (three entries):}
(a) \textit{Fam.} 9.7 corrected from year-precision
\mbox{-0046-08-12} (precision \texttt{year}) to month-precision
\mbox{-0046-05-30} (precision \texttt{month}) per Perseus dateline
\textit{ex.\ m.\ Maio a.\ 708 (46)}. The August placeholder was a
canonical-numbering artifact; the letter belongs to end of May 46
BC and \textit{precedes} 9.5 (early June) and 9.6 (last week of
June) in chronology even though Perseus's book 9 manuscript sequence
places it later.
(b) \textit{Fam.} 9.13 corrected from year-precision
\mbox{-0046-02-18} (precision \texttt{year}) to month-precision
\mbox{-0046-12-15} (precision \texttt{month}) per Perseus dateline
\textit{ex.\ a.\ 708 (46) aut in.\ a.\ 709 (45)}. The Scapula-
Pompeius Spanish-war references in the body confirm late 46 BC, on
the eve of the Munda campaign; the February placeholder was off by
ten months.
(c) \textit{Fam.} 13.68 corrected from year-precision
\mbox{-0046-01-25} (precision \texttt{year}) to month-precision
\mbox{-0046-09-05} (precision \texttt{month}) per Perseus dateline
\textit{circ.\ med.\ in.\ Sept.\ a.\ 708 (46)} = mid-early September
46 BC. The January placeholder was off by eight months.

\textbf{Latin-file opener corruptions observed (not corrected
this session, deferred to future fetch-script enhancement):}
\textit{Fam.} 13.36, 13.37 carry the salutation tail rendered
\texttt{CICERO ACILIO PROCONSVLI \$} in the fetched Latin where
the conventional \texttt{S.} is expected (OCR/transcription
artefact in the upstream Perseus TEI of book 13). \textit{Fam.}
13.38's Perseus dateline reads \texttt{iit videtur} where
\texttt{ut videtur} is meant. \textit{Fam.} 13.70's salutation
trail \texttt{S.\ R} silently rationalised to \texttt{S.} in the
English opener. These are all upstream Perseus artefacts; the
English files emend silently per cluster convention while the
Latin files preserve the upstream form. A future
\texttt{fetch\_latin.py} sanitisation pass could clean these.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (deferred to enrichment pass
to avoid concurrent-write contention; the PM did not write the
shared jsonl directly):
\begin{itemize}
\item \textbf{The \textit{non vulgaris} tier-marker as recognised
genre signal across the recommendation books.} \textit{Fam.} 13.35
(Philoxenus / Novum Comum), 13.36 (Demetrius Megas), and 13.26
(Lepidus / Mescinius / Mindius) all carry the formula in some
variant (\textit{non vulgaris esse commendationem hanc meam},
\textit{maiore studio neminem commendarim}, \textit{quasi
commendaticias}). The formula explicitly out-ranks the routine
\textit{commendaticia} tier and signals to the recipient that the
present letter is to be read with extra weight. The trio of
session-13 occurrences plus prior session attestations would
support a backmatter glossary stub on the \textit{non vulgaris}
formula as a recognised letter-of-recommendation tier-marker.
\item \textbf{The Caesarian intercalary calendar in \textit{Fam.}
6.14.} The dateline \textit{a.\ d.\ v K.\ intercal.\ priores a.\
708 (46)} refers to the first of the two intercalary months
Caesar inserted in 46 BC before the Julian reform took effect on
1 January 45 BC; the date corresponds roughly to 26 November 46
BC in the unreformed Roman calendar. This is the calendar that
ends with Caesar's reform; \textit{Fam.} 6.14 sits inside that
transitional intercalary period. Worth a glossary entry on the
46 BC intercalary calendar for the scholar profile.
\item \textbf{The \textit{ut si a me manumissus esset} formula in
the Servius cluster.} \textit{Fam.} 13.21 (Hammonius) and 13.23
(Anchialus) both deploy the ``as if he had been freed by my own
hand'' fiction --- a recurring Ciceronian commendation move that
casts the freedman as Cicero's own client through transitive
patronage of the actual patron. Worth a corpus-level note on this
patronage formula.
\item \textbf{Perseus canonical numbering versus chronological
order in \textit{Ad Familiares} book 9.} The Varro/Paetus/Dolabella
sequence of book 9 is arranged in Perseus's TEI by manuscript
order rather than by date; the actual chronological order is
9.7 (May 46), 9.1 (Dec.\ 47 / Jan.\ 46), 9.2 (April 46), 9.3
(April 46), 9.4 (June 46), 9.5 (June 46), 9.6 (June 46), then
9.13 (Dec.\ 46 / Jan.\ 45). This is a recurring pattern in the
\textit{Ad Familiares} books and worth a corpus-level
methodological note: the file-prefix \texttt{NNNbc-} sort, the
\texttt{date} field, and Perseus's numerical order are three
distinct orderings that all need to be kept straight.
\item \textbf{Iambic senarius embedded in \textit{Fam.} 9.7.}
Cicero's \textit{quid hic mihi faciet patri?} scans as a comic
trimeter quotation (or compositional fragment) about the
Caesarian killings in Africa. Whether quoted from a contemporary
comedy or coined for the moment, the metrical shape is intentional.
Worth a translator-notes entry as a candidate prosodic detail for
the scholar profile.
\item \textbf{The post-Pharsalus \textit{studia / litterae /
libri} hardening continues through \textit{Fam.} 9.7 and 9.6.}
The note recorded in session 12 on the rhetorical economy of
Cicero's literary-otium turn extends: \textit{Fam.} 9.7's
\textit{polloi math\=etai kreissones didaskal\=on} (``many pupils
outdo their teachers'') and 9.6's \textit{cum opera nostra patria
sive non possit uti sive nolit} ``since our country either cannot
or will not use our service'' belong to the same rhetorical
economy. The voice across \textit{Fam.} 9.1--9.7 plus 9.13 is
extraordinarily coherent.
\item \textbf{Single-section Latin source files.} \textit{Fam.}
13.20, 13.25, 13.33, 13.34, 13.37, 13.39, 13.70, 13.71 are all
single-section letters in Perseus's TEI. Where appropriate, the
English added \texttt{\textbackslash ciceroSection\{1\}} markers
for parallel-JSON consistency; where the Latin's lack of
subdivision was load-bearing (very short notes), it was preserved.
Structural-divergence checks should expect a mix of patterns
across book 13.
\end{itemize}

\textbf{Suggested next translation batch} (when session 13 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 13:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item Slice L Dolabella continuation (Cicero $\rightarrow$
Dolabella, late 46 -- 45 BC): \textit{Fam.} 9.10 (Dec.\ 30, 46),
9.11 (April 20, 45), 9.12 (Jan.\ 17, 45), plus the special-case
9.9 (June 48, Dolabella in Caesar's camp $\rightarrow$ Cicero ---
this letter belongs chronologically to a much earlier moment but
sits in the book 9 manuscript sequence; treat as a deliberate
chronological backfill).
\item Slice P continuation (\textit{Ad Familiares} 13 recommendation
cluster): \textit{Fam.} 13.29 -- 13.31 (Plancus, Acilius
continuations Sept-Dec 46), 13.40 -- 13.44 (further recommendations
spread across 46--45 BC); the Servius cluster continues with 13.66
(Feb 45) and the Acilius cluster with 13.30, 13.31.
\item Slice R (the \textit{P.\ Servilius Isauricus} continuation):
13.67 (Dec 46), 13.72 (May 46 if year-precision pending), 13.77
(Oct 46 to Sulpicius Imperator $\rightarrow$ likely Sulpicius
Rufus). These complete the Servilius/Sulpicius cluster.
\item Slice C (substantial speeches blocking the chronological-
gap sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\item Slice S (the post-Munda 45 BC condolence/consolation cluster
that follows from the Ligarius register): \textit{Fam.} 6.01
(A.\ Torquatus, Feb 46 \textit{year}), 4.05 (Servius's famous
consolation on Tullia's death, March 45), 4.06 (Cicero's
\textit{Consolatio} reply to Servius, April 45). These three are
load-bearing for the bound-volume reader and should be sequenced
deliberately rather than scattered across recommendation-cluster
batches.
\item Slice M (entity-stub enrichment): the entity registry still
has $\sim$472 stub entries needing real summaries; can be batched
aggressively in parallel ($\sim$50/worker, no inter-batch contention).
\end{itemize}


\textbf{Session 12 pushed the chronology pointer forward from
\textit{Fam.} 13.49 (Oct. 47 BC) to \textit{Fam.} 9.5 (June 46 BC)
while also filling four year-range-placeholder letters in the
50--47 BC band that were blocking the chronological-gap sweep.}
Thirteen letters drafted across one parallel wave (three workers):
the four-letter Slice N \textit{Ad Familiares} 15.11/15.12/15.13
+ 16.20 metadata-fix-and-translate cluster, the four-letter
Slice O Caelius-to-Cicero gap-fill 8.2/8.6/8.7/8.17, and the
five-letter Slice L opening of the post-Pharsalus Varro
correspondence 9.1--9.5 (the literary-otium turn under Caesar's
dictatorship). The chronological-gap warning is now \textbf{47
pending works dated earlier than the latest-drafted}: the
pointer moved forward eight months, so the gap reshapes rather
than shrinks --- some earlier-pending warnings cleared by the
Slice N + Slice O fills, but the pointer's advance into mid-46
BC pulled an additional band of pending 47--46 BC letters
(\textit{Fam.} 13.10, 13.20, etc.) into "earlier-pending"
territory.

\textbf{Cowork session 12 --- 13 letters drafted across one
parallel wave (three workers):}
\begin{itemize}
\item Worker A (4 letters of Slice N: \textit{Ad Familiares}
15.11/15.12/15.13/16.20, the year-range-placeholder cluster
that needed Perseus metadata before fetching): \textit{Fam.}
15.11 (Tarsus, August 50 BC, to C.\ Marcellus cos.\ 50 ---
the short formal thanks to the consul who carried the
supplicatio decree; corrupt §1 close \textit{†cum studiose ac
libenter} rendered loosely with daggers flagged), \textit{Fam.}
15.12 (on the march through Lycaonia, ~21 Sept. 51 BC, to
L.\ Paullus consul-designate --- congratulation on his
imminent consulship, the closing request that no extension be
added to Cicero's Cilician year), \textit{Fam.} 15.13
(Tarsus, January 50 BC, to L.\ Paullus now consul ---
the longer follow-up petition for the senate decree on
Cicero's res gestae; salutation \textit{L. PAVLLO COS.}
without \textit{desig.} forces a date on or after 1 January
50, when Paullus took office, ruling out the late-51
date Perseus's back-reference would otherwise imply),
\textit{Fam.} 16.20 (Rome, ~mid-May 47 BC, to Tiro
convalescing under the doctor Metrodorus --- the tender 90-word
note: ``organize the books; bring an index with Metrodorus,
since you must live by his rule; you can watch the gladiators
on the Kalends, return the next day; if you love me, take care
of yourself.'' Single-section letter; Perseus has no
\texttt{\textbackslash ciceroSection\{1\}} division --- I
supplied one).

\item Worker B (4 letters of Slice O: Caelius-to-Cicero
gap-fill spanning 51--48 BC, the brilliant young political
gossip's reports to Cicero in Cilicia and after):
\textit{Fam.} 8.2 (Rome, June 51 BC --- the Messalla acquittal
under the Lex Licinia de sodaliciis with Hortensius as
defending counsel, Hortensius hissed at the games shortly
after; \textbf{date corrected from year-precision placeholder
-0051-11-19 to -0051-06-15 month-precision} per Perseus
dateline \textit{m. Iun. a. 703 (51)} --- November is plainly
wrong, June is right; corrupt phrase \textit{†repraesentante
pronuntiatum} rendered ``announced in my presence [corrupt]''),
\textit{Fam.} 8.6 (Rome, before end of February 50 BC ---
Appius indicted by Dolabella for \textit{maiestas}, Curio's
defection still being staged, Bibulus's cohorts, the famous
\textit{consaepta omnia foeda et inhonesta} wickerwork-of-the-
juries figure, the freezing/hot/superheated chain on Curio's
prospects, and the gentle warning about the Dolabella-Tullia
match dressed as a domestic update on Fabia's divorce),
\textit{Fam.} 8.7 (Rome, end of April or beginning of May
50 BC --- hurried courier letter on Cornificius's betrothal,
Paula Valeria's divorce, Servius Ocella caught \textit{in
flagranti}; \textbf{date corrected from day-precision
placeholder -0050-05-15 to -0050-05-01 month-precision} per
Perseus dateline \textit{ex. m. Apr. aut in. Mai.}; corrupt
\textit{†nondum rettuleras} flagged), \textit{Fam.} 8.17
(Rome, January--February 48 BC, the last surviving Caelius
letter --- Caelius now on the Caesarian side and writing in
recriminations against Cicero and against his own dead
collaborator Curio: \textit{bonam mentem iracundia et amore
ablatam}, \textit{hanc perditam causam}; \textbf{date adjusted
from -0048-01-15 to -0048-02-01 month-precision} per Perseus
dateline \textit{vel ex. m. Ian. vel m. Febr. a. 706 (48)};
three corruptions flagged: \textit{quod utinam taut Appius
Claudius}, \textit{†Arruntanum me Catonem}, and
\textit{quod firmissimum †haec?}).

\item Worker C (5 letters of Slice L: opening of the
post-Pharsalus Varro correspondence, 47--46 BC, Cicero's
literary-otium turn under Caesar's dictatorship):
\textit{Fam.} 9.1 (Rome, end of 47 BC or beginning of 46 BC
--- the staged-reconciliation-with-the-books letter,
\textit{ignoscunt mihi, revocant in consuetudinem pristinam};
\textbf{date corrected from year-precision -0047-02-06 to
month-precision -0047-12-15} per Perseus dateline \textit{ex.\
a.\ 707 (47) aut in.\ a.\ 708 (46)}), \textit{Fam.} 9.2 (Rome,
a little after 20 April 46 BC, the substantial 746-word letter
--- three Greek phrases \textit{heolos, lelethotos, politeias},
the \textit{architectos / fabros} rebuilding metaphor, the
load-bearing \textit{stetit illud, una vivere in studiis
nostris} ``let this stand between us: that we live together
with our studies''; the lynx-eyed Lynceus reference; the
politeia-register that anticipates the \textit{Brutus}),
\textit{Fam.} 9.3 (Rome, 19 April 46 BC, \textit{paulo ante}
9.2 by Perseus's own back-reference --- the proverbial
\textit{glauk' eis Athenas} ``owls to Athens'' (carrying coals
to Newcastle), the medical-metaphor on the gravity of the
disease; \textbf{date corrected from year-range placeholder
-0046-07-01 to -0046-04-19 day-precision}; single-section in
Perseus, English supplies \texttt{\textbackslash
ciceroSection\{1\}}), \textit{Fam.} 9.4 (Tusculum, 6--10 June
46 BC, the one-paragraph philosophical joke on Diodorus
Cronus's Master Argument vs. Chrysippus on modal possibility
--- five Greek phrases \textit{peri dynaton, kata Diodoron,
adynaton, krisis, kata Chrysippon dynaton}, anticipating
\textit{De Fato}; the proverbial close \textit{si hortum in
bybliotheca habes, deerit nihil} ``if you have a garden along
with your library, nothing will be wanting''), \textit{Fam.}
9.5 (Rome, beginning of June 46 BC --- the load-bearing
antitheses \textit{non spem sed officium / non officium sed
desperationem} ``not hope but duty / not duty but a lost
cause,'' and the hard \textit{severitas otiosorum} ``severity
of the disengaged''; Perseus text of §3 ends mid-clause
without a closing full stop, flagged in JSON).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 12 (twelve entries):}
(a) \textit{Fam.} 15.11 corrected from year-range placeholder
\mbox{-0054-07-01} (precision \texttt{year\_range}) to
\mbox{-0050-08-01} month-precision; location and recipient
populated; \texttt{speech\_index: book:15,letter:11} added;
Perseus URL substituted for the Latin Library fallback.
(b) \textit{Fam.} 15.12 corrected from \mbox{-0054-07-01} to
\mbox{-0051-09-21} month-precision; location ``in itinere per
Lycaoniam'' and recipient \texttt{L. PAVLLO COS. DESIG.}
populated; \texttt{speech\_index: book:15,letter:12} added.
(c) \textit{Fam.} 15.13 corrected from \mbox{-0054-07-01} to
\mbox{-0050-01-01} month-precision (the \texttt{L. PAVLLO COS.}
salutation forces a date on or after 1 Jan 50 BC, ruling out
the late-51 BC date Perseus's back-reference suggested);
\texttt{speech\_index: book:15,letter:13} added.
(d) \textit{Fam.} 16.20 corrected from \mbox{-0054-07-01} to
\mbox{-0047-05-15} month-precision; location \texttt{Romae},
recipient \texttt{TIRONI} populated;
\texttt{speech\_index: book:16,letter:20} added.
(e) \textit{Fam.} 8.2 corrected from year-precision placeholder
\mbox{-0051-11-19} to \mbox{-0051-06-15} month-precision per
Perseus dateline \textit{m. Iun. a. 703 (51)}.
(f) \textit{Fam.} 8.7 corrected from day-precision placeholder
\mbox{-0050-05-15} to \mbox{-0050-05-01} month-precision per
Perseus dateline \textit{ex. m. Apr. aut in. Mai.}; precision
downgraded from \texttt{day} to \texttt{month}.
(g) \textit{Fam.} 8.17 corrected from \mbox{-0048-01-15} to
\mbox{-0048-02-01} month-precision per Perseus dateline
\textit{vel ex. m. Ian. vel m. Febr. a. 706 (48)}.
(h) \textit{Fam.} 9.1 corrected from year-precision placeholder
\mbox{-0047-02-06} to \mbox{-0047-12-15} month-precision per
Perseus dateline \textit{ex.\ a.\ 707 (47) aut in.\ a.\ 708
(46)}.
(i) \textit{Fam.} 9.3 corrected from year-range placeholder
\mbox{-0046-07-01} to \mbox{-0046-04-19} day-precision per
Perseus back-reference \textit{paulo ante ep. 2} (= one day
before 9.2 of 20 April 46 BC); location and recipient
populated; \texttt{speech\_index: book:9,letter:3} added; Perseus
URL substituted for the Latin Library fallback.
(j) \textit{Fam.} 8.6: dateline confirmed at \mbox{-0050-02-15}
month-precision per Perseus \textit{ante ex. m. Febr.\ a.\ 704
(50)}; no change.
(k) \textit{Fam.} 9.2: dateline confirmed at \mbox{-0046-04-20}
day-precision; no change.
(l) \textit{Fam.} 9.4: dateline confirmed at \mbox{-0046-06-10}
day-precision per Perseus \textit{inter viii et iv Id. Iun.}
range; no change.

\textbf{Stale-filename cleanup deferred:} four Slice N letters
(15.11, 15.12, 15.13, 16.20) still carry the \texttt{054bc-}
filename prefix from the year-range placeholder. Their real
dates are now -0050-08, -0051-09, -0050-01, -0047-05
respectively. Renaming was deferred this session because the
Cowork sandbox cannot delete files (sandbox limitation per
CLAUDE.md), and orphaning the original \texttt{054bc-} stems as
placeholder stubs that the handoff script does not auto-clean
would create noise that outlives the session. \textbf{A future
metadata-cleanup pass (run from Alexander's machine, which
\textit{can} delete) should:} (1) \texttt{git mv
latin/letters/054bc-ad-familiares-15-11.tex
latin/letters/050bc-ad-familiares-15-11.tex} (and likewise for
the english/, headnotes/, data/parallel/ stems), (2) repeat for
15.12 (→ 051bc), 15.13 (→ 050bc), 16.20 (→ 047bc), (3) update
the \texttt{latin\_file:}/\texttt{english\_file:}/
\texttt{headnote\_file:} paths in \texttt{meta/works.yaml}
accordingly, (4) regenerate manifests. None of this affects
the build (sorting is by \texttt{date} not filename).

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention; the
PM or a future enrichment pass should consolidate):
\begin{itemize}
\item \textbf{The Caelius voice across \textit{Fam.} 8.2/8.6/
8.7/8.17.} Caelius's letters to Cicero are written in a
register utterly distinct from Cicero's own --- gossipy,
slangy, hurried, friend-to-friend Roman political insider
talk, a generation younger and more excitable. The English
should keep that voice consistently colloquial-modern across
the whole book 8 sequence, not elevate it to Cicero's higher
register. The session preserved the \textit{consaepta} jury-
wattle figure in 8.6 without explanation, kept the
freezing/hot/superheated Curio chain literal, and resisted
glossing the Dolabella-Tullia warning. Cross-book voice
consistency worth a corpus-level note.
\item \textbf{The Diodorus / Chrysippus material in
\textit{Fam.} 9.4.} One of the clearest small windows onto
Hellenistic modal logic in surviving classical Latin. The
Master Argument of Diodorus Cronus (only past possibilities
are possibilities, only what will happen is possible)
contested by Chrysippus's broader definition of \textit{kata
Chrysippon dynaton}. May merit a backmatter glossary stub
linking to the contemporaneous \textit{De Fato}.
\item \textbf{The \textit{architectos / fabros} figure in
\textit{Fam.} 9.2 §5} anticipates the rhetorical-political
imagery of the \textit{Brutus} (early 46 BC) and could be
cross-linked once that work is drafted.
\item \textbf{The \textit{studia / litterae / libri}
hardening across \textit{Fam.} 9.1, 9.2, 9.3.} These nouns
shift in pressure across the three letters from ``leisure
pursuits'' to something nearer ``the only ground left to
live on.'' The English in 9.1 (\textit{ignoscunt mihi,
revocant in consuetudinem pristinam}), 9.2 (\textit{una
vivere in studiis nostris}), and 9.3 (the medical metaphor)
lets the pressure build without spelling it out. Worth a
corpus-level note on the rhetorical economy of Cicero's
literary-otium turn under the dictatorship.
\item \textbf{\textit{Fam.} 16.20 single-section structure.}
Perseus presents the Tiro convalescence letter as a single
undivided paragraph; the English supplies a
\texttt{\textbackslash ciceroSection\{1\}} marker for parallel-
JSON consistency. Two other letters this session
(\textit{Fam.} 9.3, 9.4) have the same single-section
structure in Perseus and received the same treatment.
Structural-divergence checks should expect these.
\item \textbf{The Bursa hatred / Caelius-Curio reproach
pairing.} Cicero's \textit{Fam.} 7.2 of February 51 BC (the
Bursa-conviction letter, already drafted) says he hated
Bursa worse than Clodius himself ``because the latter at
least had a great public motive.'' The Caelius letter
\textit{Fam.} 8.17 of February 48 BC enacts a similar
private-grief / private-reproach register in the opposite
direction (Caelius now reproaching Cicero and Curio).
Across the book-7-to-book-8 sequence the two voices form a
diptych on private bitterness toward political collaborators.
Worth flagging as a cross-reference for the scholar profile.
\item \textbf{\textit{Fam.} 15.13 salutation-vs.-back-reference
puzzle.} Perseus dates 15.13 to the same time as 15.4 and
15.10 (both late 51 BC at Tarsus), but the salutation
\textit{L. PAVLLO COS.} (without \textit{desig.}) requires a
date on or after 1 January 50 BC when Paullus took office.
The companion 15.12 to \textit{L. PAVLLO COS. DESIG.}
correctly belongs to autumn 51 (Paullus had just been elected).
The two letters are thus three or four months apart, not
contemporaneous; Perseus's geographic ``same place''
back-reference is right (both from the Cilician winter
quarters) but the temporal one is loose. Session chose to
trust the salutation. Worth a footnote in any future
chronological-table apparatus.
\item \textbf{Worker reports noted that \textit{Fam.} 8.2's
opening \textit{repraesentante} is daggered in Perseus, and
that \textit{Fam.} 8.17 carries three further corruptions.}
The post-Pharsalus textual transmission of book 8 is rougher
than book 9; the parallel JSON segments for 8.2, 8.7, and
8.17 carry the daggered passages in their \texttt{notes}
field.
\item \textbf{The orphan Latin file
\texttt{latin/letters/054bc-ad-familiares-13-49.tex}}
(flagged by \texttt{validate.py}) remains in the tree as a
known artifact of the Phase-0 session 1 fetch debugging. The
handoff script has a one-off rule to remove this specific
file; the warning is harmless.
\end{itemize}

\textbf{Suggested next translation batch} (when session 12 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session
12: \ldots"} and the next Cowork session opens):
\begin{itemize}
\item Slice L continuation (\textit{Ad Familiares} book 9
through 9.13, the rest of the Varro/Paetus 46 BC cluster):
9.6, 9.7, 9.9, 9.10, 9.11, 9.12, 9.13 (plus 9.8 which is
already drafted). Letters of the second half of 46 BC,
substantial intellectual register; batch 2--3 per worker.
\item Slice P (the \textit{Ad Familiares} 13 book of
recommendation letters, year-range-placeholdered cluster):
13.10, 13.20, 13.21, 13.22, 13.23, etc. through the book.
These are mostly short patronage letters; metadata-fix-and-
translate cluster; can be batched aggressively (5--6 per
worker).
\item Slice C (substantial speeches blocking the year-
precision sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\item Slice Q (Tier 2 stale-filename rename pass): execute
the four Slice N \texttt{054bc-} → \texttt{NNNbc-} renames
described above, then sweep \texttt{meta/works.yaml} for
other entries whose filename prefix disagrees with the
corrected date (a recurring pattern from year-range-
placeholder cleanups). Pure metadata pass, no translation.
\item Slice M (entity-stub enrichment): the entity registry
still has $\sim$472 stub entries needing real summaries; can
be batched aggressively in parallel ($\sim$50/worker, no
inter-batch contention since each worker writes a disjoint
slice of \texttt{data/entities.json}).
\end{itemize}

 \textbf{Session 11 attacked the chronological-gap
backlog from below}, drafting 16 letters spread across 54--50 BC
plus the \textit{Q. fr.} 3.5/3.6 doublet — the entire pending
\textit{Q. fr.} book 3 sequence of autumn 54 BC, two Cilician
recommendation/advice letters of 51--50 BC to Thermus
propraetor of Asia, the Volumnius wit letter, the Cilician
quaestor handover pair, the long 13 February 50 BC Atticus
letter on the Brutus-Salaminian moneylending case, and the
entire pending Appius Pulcher cluster of April--August 50 BC
including the long April 50 BC \textit{Fam.} 3.10 (incorrectly
year-precision dated to November 50 in works.yaml before this
session). The chronological-gap warning is now \textbf{29 pending
works dated earlier than the latest-drafted} (down from 46 at
end of session 10, a clean drop of 17 = exactly this session's
17 status flips).

\textbf{Cowork session 11 --- 16 letters drafted across one
parallel wave (four workers):}
\begin{itemize}
\item Worker A (5 letters of autumn 54 BC, the entire pending
\textit{Q. fr.} book 3 sequence): \textit{Q. fr.} 3.7
(Tusculum, late Oct./early Nov.\ 54 --- the very short note on
the Tiber flood damaging the Appian Way by the temple of Mars,
with two Homeric Iliad-16 quotations on Zeus's autumn rains;
the lampstand Quintus had made on Samos, the warm domestic
close; \textbf{corrupt §1 †et Appia ad Martis mira luvies†}
restored to sense), \textit{Q. fr.} 3.4 (Rome, 24 Oct.\ 54 ---
Drusus and Vatinius both acquitted, Cicero's own defence of
Vatinius producing the famous "you can imagine how cheerful I
was," news of P.\ Crassus dead in Parthia), \textit{Q. fr.} 3.3
(Rome, 1 Nov.\ 54 --- the four-candidate ambitus hurricane and
the looming interregnum, Caesar's two affectionate letters from
Britain), \textit{Q. fr.} 3.5 + 3.6 \textbf{combined as single
SB letter 3.5b} (Tusculum, late Oct./early Nov.\ 54 --- THE
famous letter on the composition of \textit{De Republica},
with Sallustius's reading-aloud intervention triggering the
rewrite from Africanus-Laelius dialogue to first-person treatise;
Homer Il.\ 6.208 \textit{Πολλὸν ἀριστεύειν καὶ ὑπείροχον ἔμμεναι
ἄλλων} the project's heroic motto, the \textit{γνῶθι σεαυτόν}
of §7 doubled in sense; three daggered cruxes in §§4, 6 flagged
in the JSON; \textbf{Perseus has no separate 3.6, and 3.6 is
flipped to drafted with stub pointers to 3.5 in this commit};
date-precision corrected from day -0054-11-13 to month
-0054-11-01 per the Perseus dateline \textit{ex.\ m.\ Oct.\
aut in.\ Nov.}), \textit{Q. fr.} 3.8 (Rome, mid-late Nov.\ 54 ---
Caesar's friendly letters from Britain, Pompey's Sardinia trip
and commendation of Cicero to Caesar, the body §5 fixing
composition after 24 Nov.\ 54).

\item Worker B (5 letters of 51--50 BC, the short
recommendation/wit cluster): \textit{Fam.} 13.53 (in Cilicia,
late 51 or early 50 BC year-precision --- recommendation to
Q.\ Minucius Thermus, propraetor of Asia, on behalf of L.\
Genucilius Curvus on his Hellespontine \textit{dioikēsis}
business), \textit{Fam.} 7.32 (Laodicea, after 11 Feb.\ 50,
\textbf{date corrected -0050-02-11 day → -0050-02-12 day} per
the Perseus dateline \textit{post iii Id.\ Febr.} = after 11
February --- to P.\ Volumnius Eutrapelus the wit, the wonderful
playful letter on the title to Cicero's \textit{salinae} ---
"saltworks/saltness" of wit; **seven Greek wit-category tags**:
\textit{eutrapelia, akythēron, amphibolia, hyperbolē, paragramma,
para prosdokian, entechna} --- the densest Greek concentration
of any letter in the session), \textit{Fam.} 2.18 (Laodicea,
beginning of May 50, \textbf{date corrected from year-precision
-0050-03-23 to month-precision -0050-05-01} per Perseus dateline
\textit{in.\ m.\ Maio}; to Thermus once more, on the choice of
interim governor of Asia --- prefer your quaestor, three of whose
brothers will be tribunes, to your veteran legates; \textbf{the
works.yaml description of this letter as "M. Anneius leave" is
wrong --- M. Anneius is the subject of 13-57 not 02-18}),
\textit{Fam.} 13.57 (Laodicea, beginning of April 50 --- to
Thermus again, on behalf of M.\ Anneius the legate, who is being
recalled to Cicero's Cilician staff because of the Parthian-war
news, and on Anneius's case with the Sardians; \textbf{the
works.yaml description of this letter as "Curius at Patrae"
is wrong}), \textit{Fam.} 2.19 (in camp in Cilicia, x K.\ Quint.\
= 22 June 50, to C.\ Coelius Caldus the quaestor on his coming
out from Rome; the formal first-contact letter with full
patronymic salutation \textit{M.\ TVLLIVS M.\ F.\ M.\ N.\ IMP.\
C.\ COELIO L.\ F.\ C.\ N.\ CALDO Q.}, dagger in §2 \textit{ad te
proficiscentur} for missing apodosis flagged).

\item Worker C (4 letters of April--August 50 BC, the entire
pending Appius Pulcher cluster of the Cilician proconsulship):
\textit{Fam.} 3.10 (Laodicea, April 50 BC, \textbf{date
corrected from year-precision -0050-11-03 to month-precision
-0050-04-01} per Perseus dateline \textit{m.\ April a.\ 704
(50)}; the long 1,720-word stem letter, written before
Appius's \textit{maiestas} trial; the famous \textit{triumphum
iustissimum ex inimicorum dolore} promise; the four-role
self-description \textit{rogando deprecatoris, laborando
propinqui, auctoritate cari hominis, gravitate imperatoris};
Pompey \textit{quem unum ex omnibus facio, ut debeo, plurimi};
the unnamed Dolabella as \textit{ille adulescens} of §5),
\textit{Fam.} 3.11 (in camp by the river Pyramus, mid-late
June 50 BC --- after Appius's acquittal on the \textit{maiestas}
charge brought by Dolabella; the antithesis \textit{alterum
non attigisti, alteram auxisti} ``ambitus you have not touched,
maiestas you have positively magnified''; the Aristarchus/Homer
joke), \textit{Fam.} 3.12 (Side, 4 August 50 BC, prid.\ Non.\
Sext.\ = 4 August --- on Appius's \textit{ambitus} prosecution,
the Tullia-Dolabella engagement obliquely apostrophised through
\textit{suscipe paulisper meas partis} ``take up my role for
a moment''; \textit{vides sudare me iam dudum laborantem} ``you
see me sweating''), \textit{Fam.} 3.13 (Rhodes, c.\ 10 August
50 BC, iv Id.\ Sext.\ --- short follow-up, the \textit{fructum
amicitiae nostrae ipsam amicitiam} figure preserved, the
self-deprecating closing apology to a hoped-for \textit{magister
morum}).

\item Worker D (2 substantial letters of February--July 50 BC):
\textit{Ad Atticum} 5.21 (Laodicea, Id.\ Febr.\ a.\ 704 = 13
February 50, the substantial 2,150-word letter on the
proconsular accounting and \textbf{the Brutus-Salaminian
moneylending case}: Scaptius and Matinius lent the Salaminians
at 48\% compound interest (4\% per month) under a 56 BC
senatusconsultum specifically exempting the loan from the
\textit{lex Gabinia} cap; the Salaminians arrived with the
money; Cicero froze them at his own 12\% and refused Scaptius
the cavalry to enforce the higher rate. Eight Greek phrases:
\textit{εὐημερήματι, ἀκροτελεύτιον, γλυκύπικρον,
ὑπερβολικῶς, τέθριππα, κέρας, ὁδοῦ πάρεργον, ἐνδομύχῳ}.
\textbf{Load-bearing letter for the later Brutus correspondence
in \textit{Ad Brutum} 43 BC.}), \textit{Fam.} 2.17 (Tarsus,
xvi K.\ Sext.\ = 17 July 50 --- the six-topic methodical letter
to a proquaestor with Bibulus in Syria, on successor
expectations, the Julian law on accounts, the Apamea garrison,
the 333,000 drachmas quaestorial account, the legions decreed
for Syria, and the long remonstrance about Bibulus; the
salutation is \textbf{corrupt} \textit{†CANINI SALVSTIO PROQ.}
in Perseus, with Shackleton Bailey identifying the addressee as
C.\ Caelius Caldus the proquaestor of Syria; \textbf{the
works.yaml description of this letter as "handover-to-quaestor"
is misaligned --- the actual handover-to-quaestor narrative is
in Fam 2.15 §4 already drafted}; rendered with the corrupt
salutation preserved verbatim).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 11 (five entries):}
(a) \textit{Fam.} 3.10 corrected from year-precision
\mbox{-0050-11-03} (precision \texttt{year}) to month-precision
\mbox{-0050-04-01} (precision \texttt{month}) per Perseus
dateline \textit{m.\ April a.\ 704 (50)} at Laodicea. The
November year-precision placeholder put this April 50 BC letter
out of chronological order with its companions 3.11--3.13 of
June--August.
(b) \textit{Fam.} 2.18 corrected from year-precision
\mbox{-0050-03-23} (precision \texttt{year}) to month-precision
\mbox{-0050-05-01} (precision \texttt{month}) per Perseus
dateline \textit{in.\ m.\ Maio} at Laodicea.
(c) \textit{Fam.} 7.32 corrected from \mbox{-0050-02-11} (day)
to \mbox{-0050-02-12} (day) per Perseus dateline \textit{post
iii Id.\ Febr.}\ = ``after 11 February'' (the 11th itself is
not the date; ``after'' is the dateline word). Also corrected
the \texttt{recipient:} field typo \texttt{VOLVMINO} → 
\texttt{VOLVMNIO}, and the \texttt{location\_written:} field
from the truncated \texttt{Laudiceae post} to plain
\texttt{Laudiceae}.
(d) \textit{Q. fr.} 3.5 corrected from \mbox{-0054-11-13}
(precision \texttt{day}) to \mbox{-0054-11-01} (precision
\texttt{month}) per Perseus dateline \textit{ex.\ m.\ Oct.\ aut
in.\ Nov.}\ = ``end of October or beginning of November'';
day-precision 13 November is not supported by the dateline.
Title updated to flag the Shackleton-Bailey combined-letter
designation \textit{3.5b = 3.5 + 3.6}.
(e) \textit{Q. fr.} 3.6 corrected from \mbox{-0054-07-01}
(precision \texttt{year}, the manifest-seed placeholder) to
\mbox{-0054-11-01} (precision \texttt{month}) per the dating of
3.5 with which 3.6 is bundled; \texttt{location\_written:} and
\texttt{recipient:} fields populated from the 3.5 dating;
\texttt{no\_perseus\_reason:} field rewritten to remove the
``alternative: source manually'' clause now that the entry is
drafted with the 3.5 stub pointer convention.

\textbf{Q.fr. 3.6 stub-pointer convention adopted:} since the
Perseus TEI has no separate letter 6 (sequence 1,2,3,4,5,7,8,9)
and modern editions combine 3.6's material with 3.5's second
half as the single letter SB 3.5b, the
\texttt{latin/}, \texttt{english/}, \texttt{headnotes/}, and
\texttt{data/parallel/} files for 3.6 are stub pointers to
their 3.5 counterparts (with a \texttt{stub: true} marker
in the parallel JSON). This keeps the manifest internally
consistent (both 3.6 and 3.5 numberings present) without
duplicating content. **If a future enrichment pass wants to
elide the doublet entirely, the cleanest path is to add a
\texttt{merged\_into:} field to works.yaml and have validate.py
exempt entries with that field from the file-existence check.**

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write
the shared jsonl directly to avoid concurrent-write
contention; the PM or a future enrichment pass should
consolidate):
\begin{itemize}
\item \textbf{\textit{Fam.} 7.32 sustained legal-metaphor.}
The mock-property-law conceit \textit{possessio salinarum
mearum} (``title to my saltworks'') is sustained through the
\textit{interdicta} (praetorian injunctions on property) deployed
as the imagined apparatus for defending Cicero's copyright on
his own jokes, with seven Greek wit-category tags supplying
the metalanguage of jest theory. Worth a corpus-level note as
one of the densest legal-jest passages outside the speeches.
\item \textbf{\textit{Q. fr.} 3.5 corrupt §4 † ΑΜΠΩΕΙΣ †.}
The Greek manuscript reading is meaningless and editorial
conjectures (e.g.\ Manutius's \textit{ἀτὰρ ποιήσεις} ``but yet
you will write'') are speculative. Rendered ``[corrupt]'' in
the body; flagged in the JSON.
\item \textbf{\textit{Q. fr.} 3.5 §6 † crebrius † and
†adiurat, debere tibi valde renuntiant†.} Two further
corruptions in the closing accounts passage; sense reconstructed
loosely; both rendered ``[corrupt]'' in the body.
\item \textbf{Sallustius the literary advisor across
\textit{Q. fr.} 3.4 §1 and 3.5 §1.} The same future-historian
young man (Cicero's literary interlocutor at Tusculum in late
54) urges Cicero to prosecute Gabinius (3.4) and prompts the
rewrite of \textit{De Republica} (3.5). Worth an entities
registry entry on the next enrichment pass.
\item \textbf{The Dolabella-suppression discipline across
\textit{Fam.} 3.10--3.13.} Through the four Appius letters
Dolabella is never named: \textit{ille adulescens} of 3.10 §5,
the unnamed prosecutor of 3.11, the unnamed husband-of-Tullia
of 3.12. The translator should resist any urge to gloss in the
body; the suppression is the rhetorical event.
\item \textbf{The \textit{censor, ut spero} running gag across
\textit{Fam.} 3.10--3.13.} Cicero opens, closes, and salutes
Appius as ``censor, I hope''; preserved across the four
letters as a structural grace note.
\item \textbf{\textit{Att.} 5.21 Brutus-Salaminian case is
load-bearing for the later \textit{Ad Brutum}.} The 48\%
compound interest, the two 56 BC senatusconsulta under
Lentulus and Philippus, the \textit{lex Gabinia}, Cicero's
12\% edict with annual compounding, the withdrawal of the
cavalry, the refusal to give Scaptius a prefecture, and the
Salaminians arriving with the money --- this episode will be
referenced obliquely in the run-up to the assassination and
in \textit{Ad Brutum} of 43 BC. When those letters come up,
the headnotes should cross-reference \textit{Att.} 5.21
\textsection\textsection\ 10--13.
\item \textbf{\textit{Att.} 5.21 §7 Cyprus 200 talents.} Cicero
refused the 200 Attic talents the Cyprians had customarily paid
to keep troops out of winter quarters --- the same community
(Salaminians) and suggestively close to the 200-talent
settlement Scaptius later demanded; worth a possible cross-
reference flag.
\item \textbf{Cicero's Cilician moral self-portrait.} The
recurring boast in this batch --- 12\% edict, no statues, no
shrines, no chariots, the famine handled by exhortation --- is
the moral self-portrait Cicero is consciously building for
posterity. Headnotes for the Cilician period should be
consistent in flagging this as performance-for-Atticus, not
naive self-praise.
\item \textbf{\textit{Fam.} 2.18 and 13-57 works.yaml
description swap.} The two Thermus letters' \texttt{notes:}
or description fields appear to have been swapped: 2.18's
description in works.yaml refers to ``M.\ Anneius leave'' but
the actual content is on Thermus's choice of interim governor;
13-57's description refers to ``Curius at Patrae'' but the
actual content is on Thermus releasing M.\ Anneius back to
Cicero. The PM or a future metadata-cleanup pass should
sanity-check works.yaml \texttt{title\_english} and
\texttt{notes} fields for these two entries against the Latin.
\item \textbf{\textit{Fam.} 2.17 misaligned description.} The
works.yaml entry's general description (``handover of imperium
to Caelius Caldus the inexperienced Cilician quaestor heir'')
matches what \textit{Fam.} 2.15 §4 actually is, not what 2.17
is. 2.17 is to a proquaestor (Caelius Caldus serving with
Bibulus in Syria) on six topics including the 333,000-drachma
quaestorial account. PM should review the works.yaml
description for 2.17 against the Latin.
\item \textbf{Recurring Homeric register in the autumn 54 BC
\textit{Q. fr.} letters.} 3.5 has Iliad 6.208 (Glaucus's
father's command, ``always to be best''), 3.7 has Iliad
16.385--388 (Zeus's autumn rains and the crooked-judging
elders). Worth flagging for the eventual greek-phrases.json
enrichment pass as the heightened private-mood self-quotation
register of the Tusculum days.
\end{itemize}

\textbf{Suggested next translation batch} (when session 11 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session
11: \ldots"} and the next Cowork session opens):
\begin{itemize}
\item Slice N (\textit{Ad Familiares} book 15 + 16-20 metadata-
fix-and-translate). \textbf{Four entries
(\texttt{ad-familiares-15-11, 15-12, 15-13, 16-20}) are missing
the \texttt{speech\_index:} and \texttt{latin\_source\_url:}
fields and currently carry only the Latin Library URL.} Add
\texttt{speech\_index: book:15,letter:11} (and analogously
12, 13) and the Perseus URL
\texttt{https://raw.githubusercontent.com/PerseusDL/canonical-latinLit/master/data/phi0474/phi056/phi0474.phi056.perseus-lat1.xml};
for 16-20, \texttt{speech\_index: book:16,letter:20} and the
same phi056 URL. Then fetch and translate as a small parallel
batch.
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}. \texttt{de-legibus} (52 BC) is no-Perseus
and needs manual Latin sourcing (Latin Library 403s); defer.
\item Slice O (the gap-fill 50 BC Caelius-incoming
\textit{Ad Familiares} 8.02, 8.06, 8.07, 8.17 --- the Caelius
letters TO Cicero in the Cilician period; these are short and
batchable 4 per worker).
\item Slice L (\textit{Ad Familiares} book 9, the Varro / Paetus
letters of 46 BC --- substantial intellectually-charged
post-Pharsalus letters; batch 2--3 per worker).
\item Slice M (entity-stub enrichment): the entity registry
still has $\sim$472 stub entries needing real summaries; can
be batched aggressively in parallel ($\sim$50/worker, no
inter-batch contention since each worker writes a disjoint
slice of \texttt{data/entities.json}).
\end{itemize}

\textbf{Session-10 resume notes below remain accurate} for the
\textit{Ad Familiares} 14 Terentia sequence; session 11
filled in the chronological-gap backlog from below (54--50 BC
proconsular-Cilicia letters), advancing the gap-warning count
from 46 to 29 pending earlier-than-drafted works.

\textbf{Cowork session 10 --- 16 letters drafted across one
parallel wave (four workers, four letters each):}
\begin{itemize}
\item Worker A (4 letters of 48 BC, the Dyrrhachium camp and
the early Brundisium homecoming arc):
\textit{Fam.} 14.6 (Dyrrhachium, \textit{i Id. Quint.\ a.\ 706}
= 14 July 48, the last letter from Pompey's camp before
Pharsalus, to the whole household \textit{SVIS}; date
correction \textbf{-0048-07-15 → -0048-07-14} per Perseus
dateline; no Greek; \textit{Pollicem ... extrudas} ``send Pollex
packing as soon as you can''),
\textit{Fam.} 14.12 (Brundisium, \textit{Non.\ Novemb.\ a.\ 706}
= \textbf{5 November 48 BC}, the moment of the Brundisium
homecoming itself, paired in time with \textit{Att.} 11.5
of 4 November; \textbf{date correction from YEAR-precision
placeholder -0048-09-13 to day-precision -0048-11-05}; the
admission \textit{perturbati dolore animi magnisque iniuriis
metuo ne id consili ceperimus, quod non facile explicare
possimus} ``afflicted with grief of mind and great injuries, I
fear we have taken some course we cannot easily extricate
ourselves from''),
\textit{Fam.} 14.19 (Brundisium, \textit{iv K. Dec.\ a.\ 706}
= 28 November 48; Tullia's illness coming into focus; no Greek),
\textit{Fam.} 14.9 (Brundisium, \textit{a.\ d.\ xvi K. Ian.}
= 17 December 48; Cicero's shortest extant note to Terentia,
$\sim$60 words; same week as \textit{Att.} 11.7/11.8 of 19 December).
\item Worker B (4 letters spanning late 48 BC into early June 47 BC):
\textit{Fam.} 14.17 (Brundisium, approximately 22 December 48 BC;
\textbf{works.yaml had bogus placeholder -0048-12-32}; Perseus
dateline corrupt as \textit{circ.\ xl i K. Ian.}\ --- most-cited
emendation \textit{xi K. Ian.}\ = 22 December (alternative
\textit{xvi K. Ian.}\ = 17 December); \textbf{date correction
to -0048-12-22 with month precision}; the elliptical opening
\textit{S. v. h. e. v.} = \textit{si vales bene est, ego valeo}
``if you are well, it is well; I am well''),
\textit{Fam.} 14.16 (Brundisium, \textit{pr.\ Non.\ Ian.\ a.\ 707}
= \textbf{4 January 47 BC}, NOT 5 January as in placeholder
works.yaml; \textbf{date correction -0047-01-05 → -0047-01-04};
the bitter \textit{qui me de mea sententia detruserunt} ``those
men who pushed me off my own resolve'' against the Pompeian
advisers; Volumnia = almost certainly Volumnia Cytheris,
mistress of Antony, worth a future entities entry),
\textit{Fam.} 14.8 (Brundisium, \textit{a.\ d.\ iv Non. Iun.\
a.\ 707} = 2 June 47; no Greek),
\textit{Fam.} 14.21 (Brundisium, \textit{pauli post a.\ d.\
iii Non. Iun.\ a.\ 707} = ``a little after'' 3 June 47, the
shortest of the four at $\sim$50 words).
\item Worker C (4 letters of mid-June through mid-July 47 BC):
\textit{Fam.} 14.11 (Brundisium, \textit{xvii K. Quint.}
= 15 June 47; the carefully softened
\textit{nostra factum esse neglegentia} ``it came about through
our own negligence'' --- first-person plural --- the wife-side
contrast with the parallel \textit{Att.} 11.17 formula
\textit{summa culpa mea / nullo ipsius delicto} of the same
week, sent to Atticus, where the fault is Cicero's alone),
\textit{Fam.} 14.15 (Brundisium, \textit{xii K. Quint.}
= 20 June 47; salutation \textit{TVLLIVS S. D. TERENTIAE} without
\textit{SVAE} preserved verbatim per Perseus),
\textit{Fam.} 14.10 (Brundisium, \textit{vii Id. Quint.}
= 9 July 47; salutation OCR-scanno in Latin source
\textit{TERENTIAE 5VAE} silently corrected to \textit{SVAE} in
the English file; Latin source file still carries the scanno
\textit{5VAE} for the next fetch-cleanup pass to address),
\textit{Fam.} 14.13 (Brundisium, \textit{vi Id. Quint.}
= 10 July 47, same week as 14.10; the technical Roman divorce
formula \textit{nuntium remittere} ``sending the notice of
divorce'' rendered as such; the unnamed ``that fellow''
\textit{istius vis ... concitatio multitudinis} for Dolabella's
tribunician debt-relief agitation; the rhetorical pivot
\textit{miserrimis ... minime miserum} ``most wretched ... least
wretched'' preserved as a visible repetition).
\item Worker D (4 letters of August--October 47 BC, the
end-of-Brundisium and the homecoming):
\textit{Fam.} 14.24 (Brundisium, \textit{iii Id. Sext.}
= 11 August 47; ``nothing certain''),
\textit{Fam.} 14.23 (Brundisium, \textit{prid.\ Id. Sext.}
= 12 August 47; ``the letter at last''; the cautious
\textit{satis liberales} ``generous enough''),
\textit{Fam.} 14.22 (Brundisium, \textit{i K. Sept.\ a.\ 707}
= \textbf{31 August 47 BC}; \textbf{works.yaml had bogus
placeholder -0047-08-32}; \textbf{date correction to -0047-08-31};
the letter's own subscription reads \textit{K. Septemb.}\
= 1 September, the conventional one-day-apart manuscript
offset, preserved literally in the English subscription),
\textit{Fam.} 14.20 (on the road from Brundisium near Venusia,
\textit{K. Oct.\ a.\ 707} = 1 October 47, \textbf{the famous
Tusculan housekeeping letter}: have the bath ready, prepare
a small party for tomorrow's arrival; the only letter in the
batch without the \textit{S. v. b. e. v.}\ opening formula
(Cicero is in motion now, on the road home, and drops the
convention); rendered with quiet domestic restraint per
STYLE.md, no rhetorical embellishment added; \textit{labrum}
rendered ``tub'' for the bathing basin; \textit{de Venusino}
``from the Venusian district'' rather than ``Venusia'' the
town).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 10 (five entries):}
(a) \textit{Fam.} 14.6 corrected from \mbox{-0048-07-15} to
\mbox{-0048-07-14} per Perseus dateline \textit{i Id. Quint.}\
= pridie Idus Quintiles = 14 July; the body's own subscription
\textit{Idib. Quint.}\ = 15 July is the dispatch a day after
composition, the conventional one-day offset.
(b) \textit{Fam.} 14.12 corrected from year-precision
placeholder \mbox{-0048-09-13} (precision \texttt{year}) to
day-precision \mbox{-0048-11-05} per Perseus dateline
\textit{Non. Novemb.}\ = Nones of November; \texttt{date\_precision}
field upgraded from \texttt{year} to \texttt{day} in the same edit.
This places the letter on the very day of (or one day after)
the Brundisium homecoming itself, paired with \textit{Att.}
11.5 of 4 November; the year-precision placeholder was off by
nearly two months and was sorting wrong in any chronological
build.
(c) \textit{Fam.} 14.16 corrected from \mbox{-0047-01-05} to
\mbox{-0047-01-04} per Perseus dateline \textit{pr.\ Non.\ Ian.}\
= pridie Nonas Ianuarias = 4 January.
(d) \textit{Fam.} 14.17 corrected from bogus placeholder
\mbox{-0048-12-32} (precision \texttt{day}) to conjectural
\mbox{-0048-12-22} with month precision per the corrupt
Perseus dateline \textit{circ.\ xl i K. Ian.}\ (most-cited
emendation \textit{xi K. Ian.}\ = 22 December; alternative
restoration \textit{xvi K. Ian.}\ = 17 December); precision
downgraded from \texttt{day} to \texttt{month} to reflect the
conjectural day-of-month.
(e) \textit{Fam.} 14.22 corrected from bogus placeholder
\mbox{-0047-08-32} to \mbox{-0047-08-31} per Perseus dateline
\textit{i K. Sept.}\ = pridie Kalends September = 31 August;
the letter's own subscription \textit{K. Septemb.}\ (1 Sept)
is the conventional one-day-apart dispatch offset.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write
the shared jsonl directly to avoid concurrent-write
contention; the PM or a future enrichment pass should
consolidate):
\begin{itemize}
\item \textbf{Cross-letter (\textit{Fam.} 14 Brundisium-period
register).} The set of 14 Brundisium-period Terentia letters
(14.8--14.13, 14.15--14.17, 14.19, 14.21--14.24) all open with
the conventional Roman epistolary formula \textit{S. v. b. e.
v.}\ (= \textit{si vales bene est, ego valeo}, ``if you are
well, it is well; I am well'') or its scribal variant
\textit{S. v. h. e. v.}\ The English consistently renders all
variants as ``If you are well, it is well; I am well.'' The
exception is \textit{Fam.} 14.20 of 1 October 47, written
\textit{en route} from Brundisium to Tusculum after the
Caesar-meeting, which drops the formula --- Cicero is in
motion now and the practical domestic register has resumed.
The dropping of the formula at 14.20 is a load-bearing
stylistic signal worth a corpus-level note.
\item \textbf{\textit{Fam.} 14.17 corrupt dateline.}
\textit{circ.\ xl i K. Ian.}\ in Perseus is not a valid Roman
date; \textit{xl} cannot appear in an \textit{a.\ d.}\ count
(maximum gap is \textit{xix K.}). The single-character
corruption \textit{xl i} → \textit{xi} = 22 December is the
likeliest emendation; \textit{xvi} = 17 December is also
defensible. Adopted 22 December with month precision pending
a Shackleton Bailey check.
\item \textbf{\textit{Fam.} 14.11 wife-side softening.}
\textit{nostra factum esse neglegentia} ``it came about
through our own negligence'' is the wife-side softening of
the same week's \textit{Att.} 11.17 admission to Atticus
\textit{summa culpa mea / nullo ipsius delicto}. To Atticus
the fault is Cicero's alone; to Terentia it is jointly
``ours.'' Worth flagging both as a register contrast and
as evidence for Cicero's same-week multi-correspondent
practice.
\item \textbf{\textit{Fam.} 14.13 \textit{nuntium remittere}.}
The technical Roman divorce formula, rendered ``sending the
notice of divorce.'' First substantive appearance in the
Brundisium-period Terentia letters of the Tullia/Dolabella
divorce theme that runs in parallel with \textit{Att.}
11.23/11.25 of the same months.
\item \textbf{\textit{Fam.} 14.20 \textit{labrum} = tub.}
The bathing basin in a Roman bath suite, rendered ``tub''
rather than ``basin'' for the domestic register.
\item \textbf{Salutation OCR scanno in \textit{Fam.} 14.10
Latin source.} \texttt{latin/letters/047bc-ad-familiares-14-10.tex}
carries \textit{TERENTIAE 5VAE} (the \textit{5} an OCR
misread of \textit{S}); silently corrected in the English
\texttt{\textbackslash ciceroLetterOpener\{...\}} to
\textit{SVAE}. The Latin source file retains the scanno for a
future fetch-cleanup pass.
\item \textbf{\textit{Fam.} 14.19 \texttt{recipient:} field
typo in works.yaml.} \texttt{TVLLIVS TEREM'IAE SVAE} should be
\texttt{TVLLIVS TERENTIAE SVAE}. Worth normalizing during the
next metadata-cleanup pass.
\item \textbf{\textit{Fam.} 14.6 salutation \textit{SVIS S. D.}}
Bare ``to his own, greetings,'' no addressee named. Plural
verbs in the body (\textit{videatis}, \textit{scitis}) confirm
collective family address; unusual register for Book 14, worth
an entities-mentions tag for the household.
\item \textbf{Volumnia in \textit{Fam.} 14.16.} Almost
certainly Volumnia Cytheris, the actress and mistress of M.
Antonius; worth an entity registry entry on the next
enrichment pass.
\item \textbf{\textit{Fam.} 14.6 \textit{Pollex} the courier.}
Pollex (\textit{Pollicem ... extrudas} ``send Pollex packing
as soon as you can'') recurs as a household courier through
this period; worth an entities-mentions tag.
\end{itemize}

The chronological-gap warning at end of session 10 is \textbf{46
pending works dated earlier than the latest-drafted} (down from
62 at end of session 9, a clean drop of 16 = exactly this
session's draft count; the \textit{Fam.} 13.49 deep-chronology
pointer remains unchanged at 47-10-15).

\textbf{Suggested next translation batch} (when session 10 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session
10: \ldots"} and the next Cowork session opens):
\begin{itemize}
\item Slice L (\textit{Ad Familiares} book 9, the Varro / Paetus
letters of 46 BC --- substantial, intellectually charged,
marking the move out of the post-Pharsalus Brundisium-Tusculum
darkness into the Caesarian Rome accommodation). Look for
\texttt{ad-familiares-09-01} through \texttt{-09-09}, the early
Varro-correspondence cluster; several are long but their tone
is the post-Brundisium reflective voice and they should be
batched 2--3 per worker (not 4--5 like the short Terentia
batch).
\item Slice L' (\textit{Ad Familiares} book 15 leftovers, the
proconsular-Cilicia and post-Pharsalus letters of 51--47 BC,
still pending in the chronological-gap warning above).
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\item Slice M (entity-stub enrichment): the entity registry
still has $\sim$472 stub entries needing real summaries; can
be batched aggressively in parallel ($\sim$50/worker, no
inter-batch contention since each worker writes a disjoint
slice of \texttt{data/entities.json}).
\end{itemize}

\textbf{Session-9 resume notes below remain accurate} for the
entire \textit{Ad Atticum} book 11 sequence; session 10
extended the main translation track from \textit{Att.} 11.22
(Brundisium, c.\ 1 September 47) to \textit{Fam.} 14.20
(de Venusino, 1 October 47), advancing past the
Caesar-Tarentum-meeting pivot.

---

\textit{[Cowork session 9 resume notes follow.]}

\textbf{Translation state (post-Cowork-session-9):} 432 / 958
works drafted (\~45\%). Latest drafted by deep chronology:
\textit{Ad Familiares} 13.49 (47 BC, Rome, unchanged from
session 6 --- session 9 closed the entire \textit{Ad Atticum}
book 11 sequence, of which the latest is 11.22 around 1 September
47 BC, still earlier than \textit{Fam.} 13.49). Latest drafted on
the main translation pointer: \textit{Ad Atticum} 11.22
(Brundisium, c.\ 1 September 47 BC --- the Pharnaces-defeated /
Caesar-imminent / Tullia-divorce closing arc of the long
Brundisium year). \textbf{25 letters drafted across two parallel
waves of four+three workers (seven workers total), covering the
entire \textit{Ad Atticum} book 11 (early January 48 BC through
early September 47 BC).} The chronology pointer has moved from
\textit{Ad Atticum} 10.18 (Cumae, 19/20 May 49 BC) at session
start through the entire Pharsalus year and the long Brundisium
limbo: the Epirus opening 11.1--11.2 in Pompey's winter camp; the
fragmentary 11.3 (\textit{Idibus Iuniis ex castris}, the eve of
Pharsalus); the very short 11.4 of mid-July from Pompey's camp;
the Brundisium homecoming 11.5 (4 November 48, dispelling
Quintus's hostile rumours from Patrae); the apologia 11.6 (28
November 48, justifying the break with the Pompeians); the long
deliberation 11.7 (19 December 48, on the politics of return);
the same-day 11.8 (also 19 December 48); the birthday-of-grief
11.9 (3 January 47, with the \textit{quo utinam susceptus non
essem} ``Would that I had never been taken up at birth''); the
catalogue-of-ruin 11.10 (21 January 47); the same-day 11.11 and
11.12 (8 March 47, with the verbatim self-quotation from
Cicero's letter to Caesar); the mid-March 11.13 with its
\textit{sola utilia mihi esse videantur quae semper nolui}; the
April-May arc of 11.14 (c.\ 26 April), 11.15 (14 May), and the
internal-colophon-corrected 11.16 (3 June, previously
year-precision placeholder); the brief 11.17--11.21 sequence of
June--August 47 BC; and the closing 11.22--11.25 cluster of late
summer 47 BC on Tullia's divorce from Dolabella, the Pharnaces
campaign, and the long approach to Caesar's return.

\textbf{Cowork session 9 --- 25 letters drafted across two
parallel waves (seven workers total):}
\begin{itemize}
\item Wave 1 (13 letters in four parallel workers, the
\textit{Att.} 11.1--11.13 sequence, January 48 BC through
mid-March 47 BC): Worker A --- \textit{Att.} 11.1 (Epirus,
between Nones and Ides Jan.\ 48; opens with Anteros bringing
Atticus's sealed letter, financial ruin and reliance on
Philotimus, no Greek), \textit{Att.} 11.2 (Epirus, some while
after Nones Feb.\ 48; the formal \textit{cretio} of an
inheritance, anxious instructions about Tullia, no Greek),
\textit{Att.} 11.3 (Pompey's camp, Ides Iun.\ 48 = 13 June
48; the unnamed \textit{is quicum sumus} for Pompey,
\textit{abruptio} for the financial termination, no Greek);
Worker B --- \textit{Att.} 11.4 (Pompey's camp, Ides Quint.\ 48
= 15 July 48; very short note, single section without
\texttt{\textbackslash ciceroSection}, the elliptical \textit{cetera Celer}
where the courier supplies the verb), \textit{Att.} 11.5
(Brundisium, pr.\ Non.\ Nov.\ 48 = \textbf{4 November 48}, NOT
5 November as in placeholder works.yaml; Quintus's hostility at
Patrae the first appearance of the brother rupture that runs
through book 11), \textit{Att.} 11.6 (Brundisium, iv K. Dec.\ 48
= 28 November 48; the long apologia for leaving Pompey's camp,
with two daggered cruxes $\dagger$non$\dagger$ at §2 and
$\dagger$recipio tempore me domo te nunc$\dagger$ at §2 close;
the gentle valediction to Pompey \textit{integrum et castum et
gravem} rendered as the tricolon ``integrity, purity, and
weight''; no Greek);
Worker C --- \textit{Att.} 11.7 (Brundisium, xiv K. Ian.\ 48 =
19 December 48; the long deliberation letter $\sim$830 words on
the politics of return, with the \textit{lacrimae enim se subito
profuderunt} ``for the tears have suddenly burst out'' anacoluthon,
no daggered cruxes, no Greek), \textit{Att.} 11.8 (Brundisium,
\textit{xiv K. Ian.\ }48 = \textbf{19 December 48}, NOT 1 January 48
as in placeholder works.yaml --- same-day pair with 11.7; valediction
``xiii Kal. Ian.''\ = 20 Dec.\ the conventional one-day-apart
subscription oddity; no daggered cruxes, no Greek), \textit{Att.}
11.9 (Brundisium, iii Non. Ian.\ 47 = 3 January 47; the
birthday-of-grief letter with the technical \textit{quo utinam
susceptus non essem} ``Would that I had never been taken up at
birth'' ritual phrase about the father's \textit{suscipere}, the
self-correcting \textit{cessi meis vel potius parui} ``I gave way
to my own people --- or rather, I obeyed them,'' the self-indictment
tricolon \textit{meo vitio pereo; nihil mihi mali casus attulit,
omnia culpa contracta sunt}, and one daggered crux
$\dagger$benivolentie va$\dagger$ in §1);
Worker D --- \textit{Att.} 11.10 (Brundisium, xii K. Febr.\ 47
= 21 January 47; the catalogue-of-ruin \textit{urbanae res
perditae} ``the affairs of the city in ruin'' asyndeton, no Greek),
\textit{Att.} 11.11 (Brundisium, viii Idus Mart.\ 47 =
\textbf{8 March 47}, NOT 15 March as in placeholder works.yaml ---
the prefatory dateline is corrupt \textit{vir i Id. Mart.} but the
body's own postscript reads \textit{viii Idus Mart.}; same-day
pair with 11.12; HS x\_x\_x\_ rendered ``thirty thousand
sesterces''), \textit{Att.} 11.12 (Brundisium, viii Id. Mart.\ 47
= 8 March 47; the verbatim self-quotation in §2 from Cicero's
earlier letter to Caesar rendered in quotation marks; the
sardonic \textit{praeclaras generi actiones} on Dolabella's
tribunician troublemaking), \textit{Att.} 11.13 (Brundisium,
mid-March 47 BC, month precision; the bitter inversion
\textit{sola utilia mihi esse videantur quae semper nolui}
``only those things appear useful to me which I have always refused
to want,'' no Greek).
\item Wave 2 (12 letters in three parallel workers, the
\textit{Att.} 11.14--11.25 sequence, late April through early
September 47 BC): Worker E --- \textit{Att.} 11.14 (Brundisium,
c.\ vi K. Mai.\ 47 = c.\ 26 April 47; two daggered cruxes
$\dagger$et advideo tamen exspecto$\dagger$ and
$\dagger$ibi facile est, quod quale sit hic gravius
existimare$\dagger$ in §3; HS x\_x\_x\_ ``thirty thousand
sesterces''), \textit{Att.} 11.15 (Brundisium, pr.\ Id. Mai.\ 47
= 14 May 47; one daggered crux $\dagger$quem tuam demere$\dagger$
in §3; Q.\ Fufius Calenus, Cn.\ Sallustius, the dissolute son of
Aesopus; no Greek), \textit{Att.} 11.16 (Brundisium,
iii Non. Iun.\ 47 = \textbf{3 June 47}, NOT the year-precision
placeholder -0047-01-25 in works.yaml --- prefatory Perseus
dateline is corrupt as \textit{iii Nou. luot.}\ but internal
colophon \textit{iii Non. Iun.}\ is clean; content corroborates,
with Caesar still pinned at Alexandria, the Achaeans now suing
Fufius for pardon; no daggered cruxes);
Worker F --- \textit{Att.} 11.17 (Brundisium, prid.\ Id.\ aut
Id.\ Iun.\ 47 = 12 or 13 June 47; very short single-section
note, with the carefully balanced \textit{summa culpa mea} /
\textit{nullo ipsius delicto} on Tullia's misfortune by his fault
alone), \textit{Att.} 11.18 (Brundisium, xii K. Quint.\ 47 =
20 June 47; \textit{quodvis enim supplicium levius est hac
permansione} ``any punishment whatever is lighter than continuing
in this place''), \textit{Att.} 11.19 (Brundisium, xi K. Sext.\ 47
= 22 July 47; the bitter self-judgement \textit{tantum temporis
satis est dum ut in pessimis rebus aliquid caveam qui nihil
umquam cavi} ``I have time enough only for this --- to be on my
guard, amid the worst of circumstances, where I have never in my
life been on my guard at all''), \textit{Att.} 11.20 (Brundisium,
xvi K. Sept.\ 47 = 17 August 47; \textit{notio} rendered ``the
recognition of him'' for the technical formal audience-of-
recognition before Caesar), \textit{Att.} 11.21 (Brundisium,
vi aut v K. Sept.\ 47 = 27 or 28 August 47; one daggered crux
$\dagger$mallem illum$\dagger$ in §2; the deliberately bitter
litotes \textit{Sullana confers; ... moderatione paulo minus
temperata});
Worker G --- \textit{Att.} 11.22 (Brundisium, circ.\ K. Sept.\ 47
= c.\ 1 September 47; one daggered crux \textit{in
$\dagger$oppidum$\dagger$ ponat} in §2; Pharnaces-and-Caesar news),
\textit{Att.} 11.23 (Brundisium, vii Id. Quint.\ 47 = 9 July 47;
the Tullia-divorce catalogue \textit{tabulae novae /
nocturnarum expugnationum / Metellae} rendered ``new
account-books, nocturnal raids, Metella''; no daggered cruxes),
\textit{Att.} 11.24 (Brundisium, viii Id. Sext.\ 47 = 6 August 47;
two daggered cruxes $\dagger$ad me visat$\dagger$ in §1 and
$\dagger$querere$\dagger$ in §2; HS XII vs CCI$\supset\supset$
=12{,}000 vs 10{,}000 sesterces small-skim dramatic point),
\textit{Att.} 11.25 (Brundisium, iii Non. Quint.\ 47 = 5 July 47;
two adjacent daggered cruxes in §3 \textit{apud
$\dagger$epistulas velim ut possim adversas$\dagger$} and
\textit{huius miserrimae $\dagger$facultate$\dagger$ confectus
conflictor}, both badly corrupt and worth a translator-notes
entry).
\end{itemize}

\textbf{Date corrections / meta-entry cleanups committed to
\texttt{meta/works.yaml} during session 9:} (a) \textit{Att.}
11.5 date corrected from placeholder \mbox{-0048-11-05} to
\mbox{-0048-11-04} per Perseus dateline \textit{pr.\ Non.\ Nov.}\
(= pridie Nonas = 4 Nov); (b) \textit{Att.} 11.8 date corrected
from clearly-wrong placeholder \mbox{-0048-01-01} to
\mbox{-0048-12-19} per Perseus dateline \textit{xiv K. Ian.\
a.\ 706 (48)} (the body's valediction reads \textit{xiii Kal.\
Ian.}\ = 20 Dec, the conventional one-day-apart manuscript
oddity; standard Shackleton-Bailey dating assigns 19 Dec as
date of composition); (c) \textit{Att.} 11.11 date corrected
from placeholder \mbox{-0047-03-15} to \mbox{-0047-03-08} per
the body's postscript \textit{viii Idus Mart.}\ (= 8 March; the
prefatory dateline is corrupt \textit{vir i Id. Mart.});
(d) \textit{Att.} 11.16 date corrected from year-precision
placeholder \mbox{-0047-01-25} (precision year) to
day-precision \mbox{-0047-06-03} per the clean internal
colophon \textit{iii Non. Iun.}\ at end of §5 (the prefatory
Perseus dateline is corrupt as \textit{iii Nou. luot.}); the
\texttt{date\_precision} field was upgraded from \texttt{year}
to \texttt{day} in the same edit.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention; PM
or future enrichment pass should consolidate):
\begin{itemize}
\item \textbf{Cross-letter (Book 11 motif).} The book
systematically declines to name either Pompey
(\textit{is quicum sumus} ``the man I am with'') or Philotimus
(\textit{qui eas dispensavit} ``the one who has been managing
them''). The English follows the Latin in keeping these
elliptical; identifications go in the headnotes only. This is
a load-bearing stylistic decision for the entire book and
worth a single corpus-level translator-notes entry.
\item \textit{Att.} 11.1 \textit{cistophoro in Asia ... ad
sestertium bis et viciens} rendered ``in cistophori, to the
amount of twenty-two hundred thousand sesterces'' --- keeping
the Latin coin name (the cistophorus, the silver tetradrachm of
the Attalid mints continued in proconsular Asia).
\item \textit{Att.} 11.2 \textit{crevi hereditatem} rendered
``formally entered upon the inheritance under the terms of the
will'' to preserve the technical Roman ritual of \textit{cretio}.
\item \textit{Att.} 11.6 \S 2 two daggered cruxes
$\dagger$non$\dagger$ and $\dagger$recipio tempore me domo te
nunc$\dagger$ preserved verbatim with conjectural surface
renderings; the second is heavily corrupt and editorial
resolution is contested.
\item \textit{Att.} 11.7 the closing \textit{haec me excruciant}
rendered as a flat hard close ``These thoughts rack me'' to
preserve its terminal force after the long deliberation.
\item \textit{Att.} 11.9 \textit{quo utinam susceptus non essem}
rendered ``Would that I had never been taken up at birth'' to
preserve the technical Roman ritual sense of \textit{suscipere}
(the father's lifting of a newborn for acknowledgement), rather
than the easier ``Would that I had never been born.''
\item \textit{Att.} 11.9 \S 1 daggered crux
$\dagger$benivolentie va$\dagger$ preserved; rendering ``of
goodwill'' is conjectural from the corruption.
\item \textit{Att.} 11.12 \S 2 verbatim self-quotation from
Cicero's earlier letter to Caesar preserved in English
quotation marks; this is a rare structural feature worth flagging
to the apparatus.
\item \textit{Att.} 11.14 \S 3 two daggered cruxes
$\dagger$et advideo tamen exspecto$\dagger$ and
$\dagger$ibi facile est, quod quale sit hic gravius
existimare$\dagger$ preserved; second one is doubtful and worth
a translator-notes entry.
\item \textit{Att.} 11.16 prefatory Perseus dateline corrupt as
\textit{iii Nou. luot.}\ resolved to \textit{iii Non. Iun.}\
(3 June 47) via clean internal colophon at end of §5; date
correction recorded above.
\item \textit{Att.} 11.20 \textit{notio} rendered ``the
recognition of him'' for the technical formal
audience-of-recognition before Caesar (rather than the loose
``his attention'' or ``his cognizance''); worth a glossary entry.
\item \textit{Att.} 11.21 \S 3 the deliberately bitter litotes
\textit{Sullana confers; ... moderatione paulo minus temperata}
preserved without softening into the easier ``less restrained''
because the original is built on the polite-form irony of
\textit{moderatione ... temperata}.
\item \textit{Att.} 11.21 \S 2 daggered crux
$\dagger$mallem illum$\dagger$ preserved verbatim; standard
editorial reading is ``the other course'' (i.e., Caesar going
direct Patrae-to-Sicily) but the corruption is acknowledged in
the headnote.
\item \textit{Att.} 11.22 \S 2 daggered crux
\textit{in $\dagger$oppidum$\dagger$ ponat} preserved.
\item \textit{Att.} 11.24 \S 1 + \S 2 daggered cruxes
$\dagger$ad me visat$\dagger$ and $\dagger$querere$\dagger$
preserved with conservative renderings; the §3 sums
HS XII / CCI$\supset\supset$ rendered as ``12{,}000'' /
``10{,}000'' sesterces.
\item \textit{Att.} 11.25 \S 3 two adjacent badly-corrupt
daggered passages preserved verbatim with conjectural surface
renderings; both worth translator-notes entries.
\end{itemize}

The chronological-gap warning at end of session 9 is 62 pending
works dated earlier than the latest-drafted (down from 87 at
end of session 8); the pointer mismatch is still caused by the
out-of-sequence \textit{Fam.} 13.49 (47 BC) recommendation
carry-over, not by the main translation chronology, which now
stands at \textit{Att.} 11.22 (c.\ 1 September 47 BC).

\textbf{Suggested next translation batch} (when session 9 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 9:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item Slice K (\textit{Ad Familiares} books 14--15: the Tullia
/ Terentia / family-and-province letters spanning the same
49--47 BC window as the just-drafted \textit{Att.} 10--11). The
relevant pending letters are scattered across books 14 (the
Terentia/Tullia letters) and 15 (the proconsular-Cilicia and
post-Pharsalus letters). Look for \texttt{ad-familiares-14-06},
\texttt{-14-08}, \texttt{-14-09}, \texttt{-14-13},
\texttt{-14-15}, \texttt{-14-20}, \texttt{-14-23}, \texttt{-14-24}
(8 short Terentia letters of 48--47 BC). Two-wave 4+4 dispatch.
\item Slice K' (\textit{Ad Familiares} book 9, the Varro / Paetus
letters of 46 BC --- substantial, intellectually charged, and the
move out of the post-Pharsalus Brundisium-Tusculum darkness into
the Caesarian Rome accommodation). Look for \texttt{ad-familiares-09-01}
through \texttt{-09-09}, the early Varro-correspondence cluster;
several are long but their tone is the post-Brundisium reflective
voice and they should be batched 2--3 per worker.
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\end{itemize}

\textbf{The previous session-8 resume notes below remain
accurate} for the entire \textit{Ad Atticum} book 10 sequence
(the Cumae-villa / eve-of-Pompey-pursuit arc); the chronology
pointer has moved forward from \textit{Att.} 10.18 (Cumae,
19/20 May 49) to \textit{Att.} 11.22 (Brundisium, c.\ 1
September 47) on the main translation track. The \textit{Fam.}
13.49 (47 BC) out-of-sequence recommendation remains the
deep-chronology pointer.

---

\textit{[Cowork session 8 resume notes follow.]}

\textbf{Translation state (post-Cowork-session-8):} 407 / 958
works drafted (\~42\%). Latest drafted by deep chronology:
\textit{Ad Familiares} 13.49 (47 BC, Rome, unchanged from
session 6). Latest drafted on the main translation pointer:
\textit{Ad Atticum} 10.18 (Cumae, 19 or 20 May 49 BC --- Cicero still in his Cuman
villa, the eve of his ill-fated dash to Pompey: the dramatic
news of Servius Sulpicius's son's escape from Italy and the
\textit{heptam\=eniaios} ``seven-months child'' birth-omen
opening, the proverbial $K\omega\rho\upsilon\kappa\alpha\tilde{\iota}o\iota$
``eavesdroppers of Corycus'' on the coast keeping watch for
the rumour, and the close in which the brief calm gives way to
the resolution to sail). \textbf{21 letters drafted in two
parallel waves of four+three workers (seven workers total),
spanning the entire \textit{Ad Atticum} book 10 (3 April --- 20
May 49 BC) plus three carry-over \textit{Fam.} 13
recommendation letters.} The chronology pointer has moved from
\textit{Ad Atticum} 9.19 (Arpinum, 31 March 49) at session
start through the entire \textit{Ad Atticum} book 10 sequence:
the Laterium-of-Quintus opening 10.1 with the Iliad-22 Hector
quotation on dying gloriously and the elder Peducaeus's
political counsel of 63 BC; the Arcanum-of-Quintus short
notes 10.2 (Atticus's spring \textit{lalageusa}-swallow tag)
and 10.3 (a one-section request for news of Caesar's
movements); the long Cumae letter 10.4 of 15 April on Curio's
visit and the choices facing the boni; the proverbial
\textit{Arkadian} ``you ask me for Arcadia'' (= the impossible)
of 10.5; the short 10.6 with two cruxes; the
\textit{regnandi contentio est} ``it is a contest about
kingship'' of 10.7 with Cicero's striking application of
\textit{rex} to Pompey himself; the long Themistoclean
political-deliberation 10.8 with its two Thucydidean tags on
foresight and its $\sigma\tau o\rho\gamma\acute{\eta}$ /
$\sigma\acute{\upsilon}\nu\tau\eta\xi\iota\varsigma$ /
$\sigma\upsilon\mu\pi\acute{\alpha}\theta\epsilon\iota\alpha\nu$
Greek-affect cluster; the back-to-back 10.9 + 10.10 of 3 May
on Antony, Cytheris, and the parainetic
$\sigma\kappa\upsilon\tau\acute{\alpha}\lambda\eta\nu~\Lambda\alpha\kappa\omega\nu\iota\kappa\acute{\eta}\nu$
``Spartan scytale'' code-stick and the Pindar fr. 105
$\sigma\acute{\upsilon}\nu\epsilon\sigma~\dot{o}~\tau o\iota~\lambda\acute{\epsilon}\gamma\omega$
``mark what I am telling you'' code-phrase; the Vettienus
\textit{monetali / pro cos.} pun-letter 10.11 and 10.12 with
$\pi\alpha\rho\alpha\kappa\lambda\epsilon\pi\tau\acute{\epsilon}o\nu$
``I must steal away'' coinage; the
$\pi\rho\tilde{\alpha}\xi\iota\nu~\pi o\lambda\iota\tau\iota\kappa o\tilde{\upsilon}$
``a statesman's policy'' bitter 10.13 (5/7 May,
\textit{Non. Mai.}); the dictation-from-eye-trouble 10.14 of
8 May on Servius's vacillation; the \textit{\=o poll\=es agenneias}
``Oh, the depths of ignobility!'' sneer at C. Marcellus in 10.15
of 12 May; the closing-Antony-sneer 10.16 of 14 May; the
\textit{diploma} warrant-bearer 10.17 of 16 May; and the
$K\omega\rho\upsilon\kappa\alpha\tilde{\iota}o\iota$
``eavesdroppers'' close 10.18 of 19/20 May. Plus three
\textit{Fam.} 13 year-range recommendation letters
(\textit{Fam.} 13.73 for the sons of Antipater of Derbe to
Q.\ Philippus the proconsul of Asia; 13.74 the brief request
to the same Q.\ Philippus on behalf of L.\ Oppius; 13.76 the
free-and-immune-status request for Volaterrae addressed to
the \textit{quattuorviri et decuriones}, conjecturally 63 BC
per Perseus's dateline).

\textbf{Cowork session 8 --- 21 letters drafted across two
parallel waves (seven workers total):}
\begin{itemize}
\item Wave 1 (10 letters in four parallel workers, the early
\textit{Att.} 10 sequence 3 April -- 3 May 49 BC): Worker A ---
\textit{Att.} 10.1 (Laterium, 3 April; the Iliad-22 Hector
quotation $m\acute{e}~m\grave{a}n~asp\=oud\acute{i}~ge$ in the
elder Sextus Peducaeus's 63 BC counsel; daggered $\dagger$magnum
sit$\dagger$; the dilemma \textit{veniendumne sit in consilium
tyranni}), \textit{Att.} 10.2 (Arcanum, 6 April; the Pindaric
$\lambda\alpha\lambda\alpha\gamma\epsilon\tilde{\upsilon}\sigma\alpha$
spring-swallow tag), \textit{Att.} 10.3 (Arcanum, 7 April; one-
section request for news, no Greek);
Worker B --- \textit{Att.} 10.4 (Cumae, 15 April; the long
$\sim$1{,}640-word letter on Curio's visit, with three transmitted
cruxes $\dagger$non tam$\dagger$, $\dagger$illi$\dagger$,
$\dagger$quae pro illo sit suspicandum$\dagger$ preserved; the
Stoic-tinged \textit{praeclara conscientia} ``splendid self-
knowledge''), \textit{Att.} 10.5 (Cumae, 17 April; the proverbial
$Arkad\acute{i}an$ ``you ask Arcadia of me'' = the impossible,
preserved as an in-text gloss);
Worker C --- \textit{Att.} 10.6 (Cumae, mid-April; two cruxes
$\dagger$recitet et$\dagger$ and $\dagger$et tamen$\dagger$),
\textit{Att.} 10.7 (Cumae, 23 April; the
$\sigma\upsilon\nu o\delta\acute{\iota}\alpha$ ``companionship''
Greek tag and the striking application of \textit{rex} to Pompey
in the tricolon \textit{rex modestior et probior et integrior}),
\textit{Att.} 10.8 (Cumae, 2 May; the long $\sim$1{,}540-word
Themistoclean-political-deliberation letter, with two Thucydides
tags on the Themistoclean \textit{prognosis} from Thuc.\ 1.138,
the $\sigma\tau o\rho\gamma\acute{\eta}$ /
$\sigma\acute{\upsilon}\nu\tau\eta\xi\iota\varsigma$ /
$\sigma\upsilon\mu\pi\acute{\alpha}\theta\epsilon\iota\alpha\nu$
Greek-affect cluster, $\pi\lambda o \upsilon\delta o \kappa\tilde{\omega}\nu$
``looking out / on the watch'' (transmitted corrupt, likely for
$\pi o \tau\iota\delta o \kappa\tilde{\omega}\nu$), and two
preserved cruxes $\dagger$anuival dehic$\dagger$ and
$\dagger$non simul cum Pompeio$\dagger$);
Worker D --- \textit{Att.} 10.9 (Cumae, 3 May; the
$\alpha\dot{\upsilon}\theta\epsilon\nu\tau\iota\kappa\tilde{\omega}\sigma$
``on first authority'' tag), \textit{Att.} 10.10 (Cumae, 3 May,
same day, after Antony's reply; the long Antony-and-Cytheris
letter with the
$\sigma\kappa\upsilon\tau\acute{\alpha}\lambda\eta\nu~\Lambda\alpha\kappa\omega\nu\iota\kappa\acute{\eta}\nu$
``Spartan scytale'' code-stick image, the Pindar fr.\ 105
$\sigma\acute{\upsilon}\nu\epsilon\sigma~\dot{o}~\tau o\iota~\lambda\acute{\epsilon}\gamma\omega$
``mark what I am telling you'' code-phrase, and the Peripatetic
$\dot{\alpha}\nu\eta\theta o \pi o\acute{\iota}\eta\tau o \nu$ /
$\eta\theta o \upsilon\sigma~\dot{\epsilon}\pi\iota\mu\epsilon\lambda\eta\tau\acute{\epsilon}o\nu$
character-formation pair on Cicero's nephew Quintus the younger).
\item Wave 2 (11 letters in three parallel workers, the late
\textit{Att.} 10 sequence 4 -- 20 May 49 BC + three carry-over
\textit{Fam.} 13 recommendations): Worker E --- \textit{Att.}
10.11 (Cumae, 4 May; with $\dot{\upsilon}\pi o \upsilon\lambda o \nu$
``festering underneath,'' $\dot{\alpha}\phi\rho\acute{\alpha}\kappa\tau\omega$
``undecked galley,'' and the Vettienus \textit{monetali / pro cos.}
mint-master / proconsul pun-letter), \textit{Att.} 10.12 (Cumae,
5 May; with the coined verbal adjective
$\pi\alpha\rho\alpha\kappa\lambda\epsilon\pi\tau\acute{\epsilon}o\nu$
``I must steal away''), \textit{Att.} 10.13 (Cumae, 7 May; the
$\pi\rho\tilde{\alpha}\xi\iota\nu~\pi o\lambda\iota\tau\iota\kappa o\tilde{\upsilon}$
``a statesman's policy'' bitter section with the truncated
$\pi\epsilon\rho\acute{\iota}$ ``etc.'' abbreviation and the
unresolved manuscript crux $\dagger$EKITAONON$\dagger$ preserved
in the English with daggers and \textit{[Greek: EKITAONON]});
Worker F --- \textit{Att.} 10.14 (Cumae, 8 May; the
dictation-from-eye-trouble letter --- \textit{lippitudo} = ``eye-
trouble'' --- with the diminutive sneer at Servius's
\textit{lectulus} (``his own little bed'')), \textit{Att.} 10.15
(Cumae, 12 May; the
$\dot{o}~\pi o\lambda\lambda\tilde{\eta}\sigma~\dot{\alpha}\gamma\epsilon\nu\nu\epsilon\acute{\iota}\alpha\sigma$
``Oh, the depths of ignobility!'' sneer at C. Marcellus regretting
his consulship; preserved crux $\dagger$tabellarius\ldots
satis fecissest dares$\dagger$ in \S 1; the laconic
\textit{quivis licet dum modo aliquis} ``Anyone will serve, so
long as it is somebody''), \textit{Att.} 10.16 (Cumae, 14 May;
closing-Antony-sneer with the actress (Cytheris) in his litter
carried among his lictors; no Greek);
Worker G --- \textit{Att.} 10.17 (Cumae, 16 May; the
$\dot{\epsilon}\kappa\tau\acute{\epsilon}\nu\epsilon\iota\alpha\nu$
``devotion'' tag and the imperial-warrant \textit{diploma}
rendered ``warrant''; two cruxes $\dagger$vellem cetera eius$\dagger$
and $\dagger$id si cras$\dagger$), \textit{Att.} 10.18 (Cumae,
19/20 May; the $\dot{\epsilon}\pi\tau\alpha\mu\eta\nu\iota\alpha\tilde{\iota}o\nu$
``seven-months child'' premature-birth opening with
$\epsilon\dot{\upsilon}\tau\acute{o}\kappa\eta\sigma\epsilon\nu$
``the delivery was easy,'' the proverbial
$K\omega\rho\upsilon\kappa\alpha\tilde{\iota}o\iota$ ``eavesdroppers
of Corycus,'' the extended daggered passage
$\dagger$fuere infantia ita fiet$\dagger$, and the section-4
\textit{conficior} ``I am being torn apart''), \textit{Fam.}
13.73 (\textit{anno post ep.\ xliv}; Q.\ Philippus the proconsul
of Asia, the sons of Antipater the dynast of Derbe in
Lycaonia/Pisidia), \textit{Fam.} 13.74 (\textit{eod.\ temp.\
quo ep.\ xliv}; same Q.\ Philippus, the brief request for L.\
Oppius), \textit{Fam.} 13.76 (\textit{anno incerto fort.\ 691}
i.e.\ Perseus conjectures 63 BC; the request for Volaterrae's
free-and-immune status, addressed to the
\textit{quattuorviri et decuriones}).
\end{itemize}

\textbf{Date corrections / meta-entry cleanups committed to
\texttt{meta/works.yaml} during session 8:} (a) \textit{Att.}
10.2 date corrected from placeholder \mbox{-0049-04-05} to
\mbox{-0049-04-06} per Perseus dateline \textit{postr.\ Non.\
Apr.}; (b) \textit{Att.} 10.13 date corrected from
\mbox{-0049-06-06} (year precision) to \mbox{-0049-05-07} (day
precision) per Perseus dateline \textit{Non.\ Mai.}\ (= 7 May);
(c) \textit{Att.} 10.14 date corrected from
\mbox{-0049-05-15} to \mbox{-0049-05-08} per Perseus dateline
\textit{viii Id.\ Mai.}\ (transmitted in the fetched Latin file
header as the corrupt \textit{viq i Id.\ Mai.}; standard
Shackleton Bailey dating). (d) Three \textit{Fam.} 13 carry-over
recommendations (13.73, 13.74, 13.76) had their
\texttt{latin\_source\_url} corrected from the 403'd Latin Library
URL to the canonical Perseus \texttt{phi0474.phi056.perseus-lat1.xml},
and a \texttt{speech\_index: book:13,letter:N} added per entry, so
the fetcher could pull the individual letter rather than the whole
book. The bad initial fetches (full-book dumps) were overwritten
in place and re-fetched cleanly.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention; PM
or future enrichment pass should consolidate):
\begin{itemize}
\item \textit{Att.} 10.1 \S 1 the Iliad 22.304--305 Hector
quotation $m\acute{e}~m\grave{a}n~asp\=oud\acute{i}~ge$ flagged
for the allusions pass; the framing of the elder Sextus Peducaeus's
63 BC advice with a hexameter quotation is preserved without
smoothing.
\item \textit{Att.} 10.1 \S 3 the dilemma \textit{veniendumne sit
in consilium tyranni} is a topos of political philosophy worth
flagging as a possible Stoic-school allusion.
\item \textit{Att.} 10.5 the Greek proverb $Arkad\acute{i}an$
``you ask Arcadia of me'' (= the impossible) preserved as an
in-text English gloss; worth a dedicated entry in
\texttt{data/greek-phrases.json} since an English-only
rendering would lose the proverb.
\item \textit{Att.} 10.7 the tricolon \textit{regnandi contentio
est, in qua pulsus est modestior rex et probior et integrior}
rendered with deliberate threefold ``more modest, more upright,
more sound'' to preserve the figure --- and Cicero's striking
application of \textit{rex} to Pompey himself flagged for
apparatus.
\item \textit{Att.} 10.8 \S 3 the two Thucydidean tags on
Themistoclean foresight (Thuc.\ 1.138) preserved verbatim in
Greek brackets with English glosses; the first tag is truncated
in the transmitted text after $\delta\iota'$ and a standard
continuation was supplied. \textit{Regnum non modo Romano homini
sed ne Persae quidem cuiquam tolerabile} rendered ``a kingship
not merely intolerable to a Roman --- intolerable to any Persian''
to preserve the pointed contrast.
\item \textit{Att.} 10.10 the Pindar fr.\ 105 Snell-Maehler tag
$\sigma\acute{\upsilon}\nu\epsilon\sigma~\dot{o}~\tau o\iota~\lambda\acute{\epsilon}\gamma\omega$
recurs as Cicero's recurring code-phrase to Atticus for ``read
between the lines'' --- worth a corpus-level allusion note pointing
at Pindar fr.\ 105 and listing all the \textit{Atticum}
occurrences.
\item \textit{Att.} 10.10 the Peripatetic
$\dot{\alpha}\nu\eta\theta o \pi o\acute{\iota}\eta\tau o \nu$ /
$\eta\theta o \upsilon\sigma~\dot{\epsilon}\pi\iota\mu\epsilon\lambda\eta\tau\acute{\epsilon}o\nu$
pair is technical character-formation vocabulary about Cicero's
nephew --- worth a translator-note on Cicero's use of Greek
philosophical idiom for moral judgement on young Quintus.
\item \textit{Att.} 10.13 \S 3 the manuscript crux
$\dagger$EKITAONON$\dagger$ preserved as
\textit{[Greek: EKITAONON]} with daggers, unresolved.
\item \textit{Att.} 10.14 the works.yaml date \mbox{-0049-05-15}
was a placeholder that conflicted with the Perseus dateline
(transmitted corruptly as \textit{viq i Id.\ Mai.}\ but reading
as \textit{viii Id.\ Mai.}\ = 8 May per Shackleton Bailey);
corrected to \mbox{-0049-05-08} per the chronology between 10.13
(7 May) and 10.15 (12 May).
\item \textit{Att.} 10.15 \S 1 the corrupt \textit{tabellarius si
apud te esse quas satis fecissest dares} preserved between
daggers; standard Shackleton-Bailey-style emendations not
silently incorporated.
\item \textit{Att.} 10.17 \textit{diplomate} rendered ``warrant''
(rather than ``passport'') since the document is specifically
the imperial travel-warrant authorising use of the \textit{cursus
publicus}.
\item \textit{Att.} 10.18 the proverbial
$K\omega\rho\upsilon\kappa\alpha\tilde{\iota}o\iota$
``eavesdroppers of Corycus'' kept as an inline gloss ``every
eavesdropper of Corycus'' to preserve the proverb's piratical
flavour; \textit{conficior} ``I am being torn apart'' over
``I am undone'' to preserve the violent register of Cicero's
collapse.
\item \textit{Fam.} 13.76 Perseus dateline \textit{anno incerto
fort.\ 691} (= conjecturally 63 BC) reported in the headnote
and sidecar \texttt{notes}, but the entry date in works.yaml
left at the year-range placeholder \mbox{-0054-07-01} pending
a separate chronological-refinement pass on Book 13.
\end{itemize}

The chronological-gap warning at end of session 8 is 87 pending
works dated earlier than the latest-drafted (down from 108 at
end of session 7); the pointer mismatch is still caused by the
out-of-sequence \textit{Fam.} 13.49 (47 BC) recommendation
carry-over, not by the main translation chronology, which now
stands at \textit{Att.} 10.18 (19/20 May 49 BC).

\textbf{Suggested next translation batch} (when session 8 is
landed via \texttt{bash scripts/cowork\_handoff.sh "session 8:
\ldots"} and the next Cowork session opens):
\begin{itemize}
\item Slice J (\textit{Ad Atticum} 11, the post-Pharsalus
Brundisium year + the Caesarian return: Cicero in Epirus
through Patrae through the long Brundisium wait after the
disaster at Pharsalus on 9 August 48; the dictated letters of
unsettled grief; the \textit{patrem rapuit} blow of his
brother's denunciation; the 47 BC return to Italy). The book
runs \texttt{ad-atticum-11-01} through \texttt{ad-atticum-11-25}
(25 letters spanning January 48 through November 47 BC).
Two-wave 4+4 or 5+5 dispatch; the long ones are 11.3, 11.5,
11.7, 11.12, 11.15.
\item Slice B'' (further carry-over year-range
\textit{Fam.} 13 recommendation letters from Cicero's
proconsular tenure and the early-Caesarian years, if light
worker capacity remains): \texttt{ad-familiares-13-01},
\texttt{-13-02}, \texttt{-13-77}, \texttt{-13-78},
\texttt{-13-79} (the immediate neighbours of the 13.73/74/76
batch just landed).
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\end{itemize}

\textbf{The previous session-7 resume notes below remain
accurate} for the entire \textit{Ad Atticum} book 9 sequence
(Pompey-evacuates / dictation-in-illness / Caesar-interview /
Arpinum-reflection arc); the chronology pointer has moved
forward from \textit{Att.} 9.19 (Arpinum, 31 Mar 49) to
\textit{Att.} 10.18 (Cumae, 19/20 May 49) on the main
translation track. The \textit{Fam.} 13.49 (47 BC)
out-of-sequence recommendation remains the deep-chronology
pointer.

---

\textit{[Cowork session 7 resume notes follow.]}

The chronology pointer has moved from
\textit{Ad Atticum} 8.16 (Formian villa, 4 March 49) at session
start through the entire \textit{Ad Atticum} book 9 sequence:
the dictation-in-illness 9.1, the elliptical $\sim$5-line
9.2, the Tarsus / Sicily-and-Africa diplomatic-options 9.3,
the famous nine-thesis $\theta\acute{\epsilon}\sigma\epsilon\iota\varsigma$ rhetorical-exercise letter
9.4, the Iliad-18 Achilles-on-honour pair 9.5, the
Diomedes-and-Odysseus / interrupted-letter 9.6, the
\textit{beneficium sequor, non causam} 9.7 with its
$\tau\grave{o}~\sigma\upsilon\nu\acute{\epsilon}\chi o \nu$ /
$\dot{\alpha}\pi\acute{\alpha}\nu\tau\eta\sigma\iota\varsigma$ /
$\pi o \lambda\acute{\iota}\tau\epsilon\upsilon\mu\alpha$ Greek-tag
cluster, the broken-Homer Mentor-quotation 9.8, the
nightfall-pre-Liberalia 9.9 with Agamemnon's
$\tau\acute{o}\tau\epsilon~\mu o\iota~\chi\acute{\alpha}\nu o\iota$
earth-swallow tag, the long quoted-letter-dossier 9.10 with
its \textit{sullaturit / proscripturit} desideratives, the
section-skipping (no \S 3) 9.11 with the \textit{nekuia}
epithet recycled, the Mucius-Scaevola-comparison 9.12,
the Plato-Letter-7-quoting 9.13, the
\textit{authentik$\overline{\textnormal{o}}$s} short 9.14, the
\textit{t$\acute{e}$tlathi k$\acute{u}$nteron} Odyssey-tag 9.15,
the Caesar-letter-enclosing 9.16, the eve-of-interview
\textit{o tempus miserum} 9.17, the famous interview-with-Caesar
report 9.18 with Caesar's reported direct speech (\textit{veni
igitur et age de pace / an tibi ego praescribam? / ego vero
ista dici nolo}), and the Arpinum reflection 9.19 with the
\textit{boni cives amantes patriae mare infestum habebimus}
bitter inversion. \textbf{19 letters drafted in two parallel
waves of four+three workers (seven workers total).}

\textbf{Cowork session 7 --- 19 letters drafted across two
parallel waves:}
\begin{itemize}
\item Wave 1 (10 letters in four parallel workers, the early
\textit{Att.} 9 sequence 6--18 March 49 BC): Worker A ---
\textit{Att.} 9.1 ($\kappa\epsilon\nu\acute{o}\sigma\pi o \upsilon\delta\alpha$
and $\dot{\alpha}\pi\acute{\alpha}\nu\tau\eta\tau o \nu$, with the Scinio/Scipio
textual question and \textit{uni, uni hoc damus} geminated
emphasis), \textit{Att.} 9.2 (the very short
$\dot{\upsilon}\pi\grave{o}~\tau\grave{\eta}\nu~\delta\iota\alpha\lambda\tilde{\eta}\psi\iota\nu$
opening fragment of what later editors split as 9.2 + 9.2A;
\textit{Att.} 9.2A is not a separate \texttt{works.yaml} entry
and was not present in the Perseus latin file fetched here),
\textit{Att.} 9.3 (\textit{mare superum / inferum} geographical
sense, audita naviculariis the unnamed Caesar's bribes
deliberately anonymous);
Worker B --- \textit{Att.} 9.4 (the famous nine-thesis
$\theta\acute{\epsilon}\sigma\epsilon\iota\varsigma$ rhetorical-exercise
letter where Cicero stages the dialectic of the war as a series
of Greek philosophical theses; the Perseus latin file transmits
the Greek partly in beta-code, partly in Greek script, and the
worker normalised to smooth transliterations for the English
while preserving the Perseus transmission verbatim in the
parallel-sidecar Latin), \textit{Att.} 9.5 (\textit{decem
annorum peccata} = ten years of wrongs, with Iliad 18.96 +
18.98--99 Achilles quotations on dying-in-honour), \textit{Att.}
9.6 (Iliad 10.94--95 Agamemnon-sleepless quotation, the
interrupted-letter structural pivot \textit{scripta iam
epistula\ldots litterae sunt adlatae} translated by
``After the letter was already written\ldots,'' and Clodia
the mother-in-law of L.\ Metellus distinguished from the
Pro Caelio Clodia);
Worker C --- \textit{Att.} 9.7 (the \textit{beneficium sequor,
non causam} centerpiece letter; the rendering ``I am following
the obligation, not the cause'' preserves the moral-debt sense
that drives the Milo comparison; with $\tau\grave{o}~\sigma\upsilon\nu\acute{\epsilon}\chi o \nu$,
$\dot{\alpha}\pi\acute{\alpha}\nu\tau\eta\sigma\iota\varsigma$,
$\pi o \lambda\acute{\iota}\tau\epsilon\upsilon\mu\alpha$,
$\mu\acute{\eta}~\mu o\iota$, $\epsilon\dot{\iota}\delta\acute{\omega}\varsigma~\sigma o\iota~\lambda\acute{\epsilon}\gamma\omega$,
$\dot{\alpha}\chi\alpha\rho\iota\sigma\tau\acute{\iota}\alpha\varsigma$,
$\pi\lambda\acute{o}o\varsigma~\dot{\omega}\rho\alpha\tilde{\iota}o\varsigma$
Greek-tag cluster and the aposiopesis \textit{ut in Milone, ut
in\ldots} preserved), \textit{Att.} 9.8 (Odyssey 3.22
Telemachus-broken-off quotation, the \textit{sementem
proscriptionis} agricultural metaphor preserved);
Worker D --- \textit{Att.} 9.9 (Liberalia 17 March 49, the
day Pompey sails: $\sigma o\phi\iota\sigma\tau\epsilon\acute{\upsilon}\omega$ /
$\theta\acute{\epsilon}\sigma\epsilon\iota\sigma$ /
$\tau\acute{o}\tau\epsilon~\mu o\iota~\chi\acute{\alpha}\nu o\iota~\epsilon\dot{\upsilon}\rho\epsilon\tilde{\iota}\alpha~\chi\theta\acute{\omega}\nu$
Agamemnon-earth-swallow tag from Iliad 4.182/8.150, with several
daggered $\dagger$predum$\dagger$ and $\dagger$plaboque$\dagger$
cruxes), \textit{Att.} 9.10 (the long $\sim$1{,}855-word
quoted-letter dossier where Cicero quotes eight successive
letters from Atticus by date to build his self-defence; the
\textit{sullaturit / proscripturit} desiderative neologisms
rendered as the hyphenated calques ``yearning-to-be-a-Sulla,
yearning-to-proscribe''; with $\dot{\epsilon}\nu~\tau o\tilde{\iota}\sigma~\dot{\epsilon}\rho\omega\tau\iota\kappa o\tilde{\iota}\sigma$,
$\dot{\alpha}\lambda o \gamma\acute{\iota}\sigma\tau\omega\sigma$
(\texttimes\,2), $\dot{\upsilon}\pi o \kappa o \rho\acute{\iota}\zeta\eta$,
$\chi\rho\eta\sigma\mu\grave{o}\sigma$,
$\dot{\alpha}\sigma\pi o \nu\delta o \nu$ (\texttimes\,2),
$\phi\iota\lambda\acute{o}\pi\alpha\tau\rho\iota\nu$,
$\pi o \lambda\iota\tau\iota\kappa\grave{o}\nu$,
$\gamma\epsilon\nu\iota\kappa\acute{\omega}\tau\epsilon\rho o\nu$,
$\nu\acute{\epsilon}\kappa\upsilon\iota\alpha\nu$, $\dot{\alpha}\pi o \rho\tilde{\omega}$,
$\sigma\tau\epsilon\rho\kappa\tau\acute{\epsilon}o\nu$,
$\tau\grave{o}~\mu\acute{\epsilon}\lambda\lambda o \nu~\kappa\alpha\rho\alpha\delta o \kappa\acute{\eta}\sigma\epsilon\iota\sigma$,
$\dot{\upsilon}\pi\grave{o}~\tau\grave{\eta}\nu~\lambda\tilde{\eta}\psi\iota\nu$,
$\dot{\alpha}\sigma\mu\acute{\epsilon}\nu\iota\sigma\tau o\nu$
Greek-tag cluster).
\item Wave 2 (9 letters in three parallel workers, the late
\textit{Att.} 9 sequence 20--31 March 49 BC --- Pompey now at
sea, the interview-with-Caesar, the retreat to Arpinum):
Worker E --- \textit{Att.} 9.11 (with the deliberate section
skip from \S 2 to \S 4 in Perseus preserved; Atticus's
\textit{nekuia} epithet for Pompey's entourage recycled),
\textit{Att.} 9.12 (the Mucius-Scaevola pontifex-altar-killing
parallel implicit; daggered $\dagger$ad$\dagger$ finis crux
preserved), \textit{Att.} 9.13 (the Stesichorus/Plato-Phaedrus
$o\dot{\upsilon}\kappa~\dot{\epsilon}\sigma\tau'~\dot{\epsilon}\tau\upsilon\mu o \varsigma~\lambda\acute{o}\gamma o \varsigma$
tag applied to the rafts story, with the Plato Letter 7
$\alpha\dot{\iota}~\gamma\grave{\alpha}\rho~\tau\tilde{\omega}\nu~\tau\upsilon\rho\acute{\alpha}\nu\nu\omega\nu$
quotation on the requests-of-tyrants-mixed-with-compulsion);
Worker F --- \textit{Att.} 9.14 ($\alpha\dot{\upsilon}\theta\epsilon\nu\tau\iota\kappa\tilde{\omega}\sigma$
``straight out'' with two daggered $\dagger$ad ambitionem$\dagger$
and $\dagger$quis ulli$\dagger$ cruxes), \textit{Att.} 9.15
(Odyssey 20.18 $\tau\acute{\epsilon}\tau\lambda\alpha\theta\iota~\kappa\acute{\upsilon}\nu\tau\epsilon\rho o\nu$
``Endure, more dog-hearted still'' applied to the impending
disgrace, Odyssey 3.26--27 Telemachus-and-the-divine-prompting
quotation, with three daggered cruxes preserved), \textit{Att.}
9.16 (the embedded Caesar-letter-recieving plain register, no
Greek; the \textit{iam opes meas, non opem} resources-vs.-help
wordplay preserved literally);
Worker G --- \textit{Att.} 9.17 (the very short eve-of-Caesar-
interview letter, $\kappa\iota\nu\delta\upsilon\nu\acute{\omega}\delta\eta$
``perilous''), \textit{Att.} 9.18 (the famous interview-with-
Caesar report, dated 28 March 49 from Arpinum but recounting
the meeting earlier that day at the Formian villa: Caesar's
reported direct speech \textit{veni igitur et age de pace}
rendered ``Come, then, and act for peace,'' \textit{an tibi
ego praescribam?} ``Or am I to prescribe to you?,'' and
\textit{ego vero ista dici nolo} ``I will not have such things
said'' --- none softened or paraphrased; with
$\nu\acute{\epsilon}\kappa\upsilon\iota\alpha$,
$\dot{\eta}\rho\omega\sigma$ (sarcastic ``hero'' Celer),
$\kappa\alpha\tau\alpha\kappa\lambda\epsilon\grave{\iota}\sigma$
(Caesar's parting threat), $\lambda\alpha\lambda\alpha\gamma\epsilon\tilde{\upsilon}\sigma\alpha\nu$,
$\pi o\lambda\iota\tau\iota\kappa\acute{\eta}\nu$; flag: the closing
phrase \textit{haec fere. iam vereor ne te ne paeniteat me} in
Shackleton Bailey does not appear in the Perseus text fetched
into the Latin file, which ends at \textit{valde tuas litteras
nunc exspecto.} --- worth a manuscript-apparatus check, not a
mid-translation emendation), \textit{Att.} 9.19 (Arpinum,
31 March 49, the $\dot{\alpha}\nu\alpha\theta\epsilon\acute{\omega}\rho\eta\sigma\iota\sigma$
``second look'' on the enormity of leaving Italy; the bitter
inversion \textit{boni cives amantes patriae mare infestum
habebimus} rendered with the wrenched syntax preserved ``have
the sea as our hostile country, we good citizens, lovers of
our fatherland,'' and \textit{in Aegyptum nos abdemus} as
``We shall take ourselves off into Egypt'').
\end{itemize}

\textbf{Date corrections / meta-entry cleanups committed to
\texttt{meta/works.yaml} during session 7:} none. All 19
\textit{Att.} 9 entries had \texttt{date\_precision: day}
already and the Perseus dateline matched in every case --- a
welcome respite from the placeholder-correction pattern of
sessions 5 and 6.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention; PM
or future enrichment pass should consolidate):
\begin{itemize}
\item \textit{Att.} 9.1 \S 4 \textit{Scinio} read as Scipio
(Q.\ Caecilius Metellus Pius Scipio, Pompey's father-in-law);
the wordplay with \textit{vel cum genero honeste} (= with his
son-in-law, i.e.\ with Pompey) makes Scipio the obvious
referent. Flag for apparatus.
\item \textit{Att.} 9.2 the very short letter preserved as just
the opening fragment; the longer \textit{Att.} 9.2A
\textit{Postridie Idus Martias\ldots} is not in the Perseus
TEI file (and is not a separate works.yaml entry); modern
editions split what some manuscripts run together as 9.2 +
9.2A. The translation here covers only 9.2 proper.
\item \textit{Att.} 9.4 the nine-thesis $\theta\acute{\epsilon}\sigma\epsilon\iota\varsigma$
list: rendering policy for the Perseus beta-coded Greek
(grave-marks, parenthetical breathings) was to silently
normalise to transliteration in the English while preserving
the Perseus transmission verbatim in the parallel-sidecar Latin
segment. The reading of thesis 3 \textit{euelabeteon ton
katalyonta me autos airetai} as ``be on guard against the
destroyer, lest he himself be raised up [as the new tyrant]''
is the active reading; the middle/passive ``lest he himself
seize [tyranny]'' is an alternative worth a translator-note.
\item \textit{Att.} 9.7 \S 3 \textit{beneficium sequor, non
causam} rendered ``I am following the obligation, not the
cause'' --- ``obligation'' over ``favour'' / ``kindness'' to
capture the moral-debt sense that drives the Milo comparison.
The Shackleton Bailey ``It is the man, not the cause'' is an
alternative; the present rendering follows the Latin shape
more closely.
\item \textit{Att.} 9.7 \S 1 \textit{quasi animulae
instillarunt} rendered ``dripped, as it were, a little life
back into me'' --- the diminutive \textit{animulae} preserved
with ``little life,'' the medical-droplet image preserved,
balanced against Cicero's immediate self-correction
\textit{recreatum enim me non queo dicere}.
\item \textit{Att.} 9.7 \S 7 \textit{tegulam\ldots nullam
relicturum} kept literal ``not leave a single roof-tile.''
\item \textit{Att.} 9.10 \S 6 the \textit{sullaturit /
proscripturit} desiderative neologisms rendered as
hyphenated calques ``yearning-to-be-a-Sulla,
yearning-to-proscribe'' to preserve Cicero's coined morphology.
The cleanest English (``itching to be a Sulla and to
proscribe'') would flatten the joke; the calque keeps it
visible.
\item \textit{Att.} 9.10 \S 2 \textit{tamquam avis illa mare
prospecto evolare cupio}: the proverbial halcyon/seabird kept
with the demonstrative \textit{illa} ``that bird'' preserved,
rather than naming the species.
\item \textit{Att.} 9.10 \S 3 \textit{sol excidisse mihi e
mundo videtur}: Cicero openly quotes back an image Atticus
had used in an earlier letter; the rendering keeps the
attribution ``as it is said in some letter of yours.''
\item \textit{Att.} 9.13 \S 4 the corrupt clause
$\dagger$ludum cc vellem scribis\ldots quia$\dagger$ preserved
with daggers in both English and parallel-sidecar Latin.
\item \textit{Att.} 9.13 the Plato \textit{Letter 7} 329d
$\alpha\dot{\iota}~\gamma\grave{\alpha}\rho~\tau\tilde{\omega}\nu~\tau\upsilon\rho\acute{\alpha}\nu\nu\omega\nu~\delta\epsilon\acute{\eta}\sigma\epsilon\iota\sigma\ldots~o\dot{\iota}\sigma\theta'~o\dot{\tau}\iota~\mu\epsilon\mu\iota\gamma\mu\acute{\epsilon}\nu\alpha\iota~\dot{\alpha}\nu\acute{\alpha}\gamma\kappa\alpha\iota\sigma$
quotation flagged for the allusions pass.
\item \textit{Att.} 9.13 the Stesichorus / Plato-Phaedrus 243a
$o\dot{\upsilon}\kappa~\dot{\epsilon}\sigma\tau'~\dot{\epsilon}\tau\upsilon\mu o \varsigma~\lambda\acute{o}\gamma o \varsigma$
tag flagged for the allusions pass.
\item \textit{Att.} 9.15 \S 1 Odyssey 20.18 $\tau\acute{\epsilon}\tau\lambda\alpha\theta\iota~\kappa\acute{\upsilon}\nu\tau\epsilon\rho o\nu$
``Endure, more dog-hearted still'' applied to Cicero's own
endurance of the proscription possibility.
\item \textit{Att.} 9.18 the entire reported-speech passage
deserves a translator-note as a unit: Caesar's three quoted
utterances rendered as direct speech in matching English
directness (no paraphrase, no softening). The Perseus text
ends earlier than Shackleton Bailey's edition (which
includes the closing \textit{haec fere. iam vereor ne te
ne paeniteat me}); the present translation covers only
the Perseus content.
\item \textit{Att.} 9.19 \S 1 \textit{boni cives amantes
patriae mare infestum habebimus} preserved with the
wrenched syntax ``have the sea as our hostile country,
we good citizens, lovers of our fatherland'' to keep the
bitter inversion that the sea, not the country, is the
patriots' hostile ground.
\end{itemize}

The chronological-gap warning at end of session 7 is 108
pending works dated earlier than the latest-drafted (down
from 127 at end of session 6); the pointer mismatch is still
caused by the out-of-sequence \textit{Fam.} 13.49 (47 BC)
recommendation carry-over, not by the main translation
chronology, which now stands at \textit{Att.} 9.19 (31 March
49 BC).

\textbf{Suggested next translation batch} (when session 7 is
landed via \texttt{cowork\_handoff.sh "session 7: ..."} and the
next Cowork session opens):
\begin{itemize}
\item Slice I (\textit{Ad Atticum} 10, the late-March through
early-June 49 sequence: Cicero from Arpinum through the
Cuman / Pompeian / Formian villa rotation as he weighs the
follow-Pompey decision, the visits from young Quintus and
Quintus the elder, the embassy-of-the-towns reports, and
finally on 7 June the Caieta-harbour embarkation):
\texttt{ad-atticum-10-01} through \texttt{ad-atticum-10-18}
(18 letters). Two-wave 4+4 or 4+5 dispatch.
\item Slice B' (carry-over from previous sessions, year-range
recommendation letters): \texttt{ad-familiares-13-73},
\texttt{-13-74}, \texttt{-13-76} (the three remaining
year-precision \textit{Fam.} 13 recommendation letters on the
hold list). These can be folded into any wave with light
worker capacity.
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\end{itemize}

\textbf{The previous session-6 resume notes below remain
accurate} for the post-Rubicon retreat through book 8 of
\textit{Ad Atticum}; the chronology pointer has moved forward
from \textit{Fam.} 8.16 (Intimilium, 16 Apr 49) to \textit{Att.}
9.19 (Arpinum, 31 Mar 49) on the main translation track. The
\textit{Fam.} 13.49 (47 BC) out-of-sequence recommendation
carry-over from session 6 remains the deep-chronology pointer.

---

\textbf{Translation state (post-Cowork-session-6):} 367 / 958
works drafted (\~38\%). Latest drafted by deep chronology:
\textit{Ad Familiares} 13.49 (47 BC, Rome --- a short
recommendation to C. Curio, out-of-sequence carry-over from the
\textit{Fam.} 13 stuck-recommendation list). Latest drafted on
the main translation pointer: \textit{Ad Familiares} 8.16
(Intimilium in Liguria, 16 April 49 BC --- Caelius writing to
Cicero from inside Caesar's camp en route to the Spanish
campaign, justifying his defection to Caesar in the breezy /
embarrassed-bravado register that distinguishes Caelius's voice
from Cicero's). The chronology pointer has moved from
\textit{Att.} 7.26 (Formiae, 15 Feb 49) at session start through
the entire \textit{Ad Atticum} book 8 sequence (8.1--8.16, the
rolling crisis as Pompey evacuates Brundisium and Cicero in his
Formian villa records each day's news of the collapse and his
own agonising about whether to follow), plus \textit{Fam.} 16.8
(carry-over mid-Jan Tiro letter slipped past in session 5),
\textit{Fam.} 8.15 (the late-winter Caelius newsletter en route
to Spain), \textit{Fam.} 14.7 (the dramatic Caieta departure
letter, written aboard ship as Cicero finally embarks to join
Pompey on 7 June 49), and \textit{Fam.} 8.16 (the Caelius
defection letter from Caesar's camp). \textbf{21 letters drafted
in two parallel waves of four workers this session.}

\textbf{Cowork session 6 --- 21 letters drafted across two
parallel waves of four workers each (8 workers total):}
\begin{itemize}
\item Wave 1 (10 letters in four parallel workers, the early
\textit{Att.} 8 sequence + carry-over Tiro): Worker A ---
\textit{Fam.} 16.8 (mid-Jan 49 carry-over Tiro letter, with
Greek Euripides fragment on cold), \textit{Att.} 8.1 (Formiae,
16 Feb, the snide \textit{lautorum et locupletum} redefinition
of the \textit{boni}), \textit{Att.} 8.2 (Formiae, 17 Feb, with
the lamp-conceit and the daggered \textit{sed cur} crux);
Worker B --- \textit{Att.} 8.3 (Cales, 18 Feb, the dramatic
centerpiece of book 8: a $\sim$1,330-word political-deliberation
letter to Atticus listing the Pompeian inheritance with the
anaphoric \textit{ille \dots ille \dots ille} indictment and the
\textit{non accipere ne periculosum sit} crux on the triumph
question), \textit{Att.} 8.4 (Formiae, 22 Feb, written
\textit{ante lucem}, with the closing daggered Brundisium
fragment); Worker C --- \textit{Att.} 8.5, 8.6, 8.7 (Formiae,
21--23 Feb, three short dispatches including the
Iliad-17-bull-simile Greek tag at 8.5, the daggered
\textit{nihil mutasset} crux at 8.6, and the famous
\textit{malle me cum Pompeio vinci quam cum istis vincere} at
8.7); Worker D --- \textit{Att.} 8.8, 8.9, 8.10 (Formiae,
24--26 Feb, including the Sophocles \textit{Oedipus at Colonus}
1023--4 tag at 8.8 and the broken-syntax \textit{ad quintum
miliarium} sentence at 8.9; 8.10 at $\sim$135 words is one of
the shortest letters in the corpus).
\item Wave 2 (11 letters in four parallel workers, the late
\textit{Att.} 8 sequence + Caelius newsletters + Caieta
departure + carry-over recommendation): Worker E ---
\textit{Att.} 8.11 (Formiae, 1 Mar, the long \textit{moderator
rei publicae} letter that quotes Scipio in \textit{De Re
Publica} book 5 on the ideal statesman and indicts Pompey for
seeking Sullan-style \textit{dominatio} --- contains
\textit{skopos / prothespizo / Ilias} Greek tags plus the
\textit{iamque mari magno} tragic-fragment quotation and the
triple-daggered slave-conscript prophecy of next summer),
\textit{Att.} 8.12 (Formiae, 28 Feb, with the \textit{armatus
armato} figura etymologica), \textit{Att.} 8.13 (Formiae,
1 Mar, brief — the 8.13 file in Perseus contains only Cicero's
own note, not the forwarded Pompey-letter triplet 8.12A/B/C/D);
Worker F --- \textit{Att.} 8.14, 8.15, 8.16 (Formiae, 2--4 Mar,
closing book 8, with the daggered \textit{diariis} and
\textit{authemonis} cruxes, and at 8.16 the Caesar-as-Pisistratus
and Pompey-as-Marius-Sulla typologies plus the
\textit{apolitikotaton / astrategetotaton / apanteseis /
aideomai} Greek-tag cluster); Worker G --- \textit{Fam.} 8.15
(en route, 9 Mar, Caelius newsletter with the Domitius / Venus
/ Psecas in-joke at the close), \textit{Fam.} 8.16 (Intimilium
in Liguria, 16 Apr, the famous defection-to-Caesar letter with
Caesar's reported \textit{`have' mihi dixit} greeting and the
\textit{optimatem / optimum} closing pun); Worker H ---
\textit{Fam.} 14.7 (in the harbour at Caieta, 7 June 49, the
brief letter to Terentia and Tullia written aboard ship as
Cicero finally embarks to join Pompey --- MAJOR date
correction from year-precision placeholder \mbox{-0049-04-08}
to day-precision \mbox{-0049-06-07} per Perseus dateline
\textit{vii Id. Iun.}), \textit{Fam.} 13.49 (47 BC, Rome,
the short Curio recommendation that had been stuck on the
year-range carry-over list since session 1).
\end{itemize}

\textbf{Date corrections / meta-entry cleanups committed to
\texttt{meta/works.yaml} during session 6 (3 entries):}
\texttt{ad-familiares-14-07}: $-0049-04-08$ year-precision
placeholder $\to$ $-0049-06-07$ day (Perseus dateline
\textit{vii Id. Iun.} = 7 June; the dramatic Caieta-departure
letter belongs at 7 June 49, not at the unattested 8 April
book-level placeholder).
\texttt{ad-familiares-08-15}: \texttt{location\_written: circ}
parser artifact (the date hedge \textit{circ.} = \textit{circiter}
was mis-extracted into the location slot by
\texttt{fetch\_latin.py}) $\to$ \texttt{null}; also fixed the
recipient field \texttt{CAELIV5 CICERONI S} (5-for-S OCR slip)
$\to$ \texttt{CAELIVS CICERONI S}.
\texttt{ad-familiares-16-08}: \texttt{location\_written: in
Campania vel} (truncated from \textit{in Campania vel ex.~m.~Ian.~vel
Febr.}) $\to$ \texttt{in Campania} (the residual is a date hedge,
not a location).
The chronological-gap warning at end of session is 127 pending
works dated earlier than the latest drafted (up from 36) because
the latest-drafted pointer jumped to \textit{Fam.} 13.49 at
47 BC (out-of-sequence recommendation carry-over). The 127
earlier-pending count is misleading; the actual translation
chronology pointer is at \textit{Fam.} 8.16 (16 April 49 BC),
and there are only $\sim$36 letters dated earlier than that --- mostly
the long-standing year-precision \textit{Fam.} 13 recommendation
letters on the recommendations carry-over list (Slice B' below).

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention; PM
or future enrichment pass should consolidate):
\begin{itemize}
\item \textit{Att.} 8.1 \S 3 \textit{bonorum, id est lautorum et
locupletum} rendered \textit{``of the loyalists --- that is, of
the well-dressed and the well-to-do''} preserving the snide
social-register redefinition.
\item \textit{Att.} 8.2 \S 4 daggered \textit{sed cur} preserved
with daggers; lamp-conceit \textit{eadem lucerna} (writing this
letter by the same lamp by which the previous letter was burned)
rendered literally with the security-precaution sense explained
in the headnote.
\item \textit{Att.} 8.2 \S 4 Socrates / Leon of Salamis allusion
to Plato \textit{Apol.} 32c--d, flagged for allusions pass.
\item \textit{Att.} 8.3 \S 6 daggered \textit{non accipere ne
periculosum sit} on the triumph question rendered conservatively
to the standard conjectural sense; \S 4 → \S 6 section-numbering
jump (no \S 5) preserved per OCT.
\item \textit{Att.} 8.3 the anaphoric \textit{ille \dots ille
\dots ille} chain of Pompey's career indictment preserved as
repeated \textit{``he the\dots''} constructions.
\item \textit{Att.} 8.4 \S 3 closing daggered fragment
\textit{scis Gnaeum ire Brundisium desertum} rendered to the
unambiguous contextual sense though exact wording unrecoverable.
\item \textit{Att.} 8.5 \S 1 Iliad 17.430 bull-simile
(\textit{$\pi$o$\lambda\lambda$$\grave{\alpha}$ $\mu$$\acute{\alpha}$$\tau$$\eta$$\nu$ $\kappa$$\epsilon$$\rho$$\acute{\alpha}$$\epsilon$$\sigma$$\sigma$$\iota$$\nu$ $\dots$}) rendered \textit{``tossing his horns idly into the air in his rage''}; flag for allusions pass.
\item \textit{Att.} 8.6 \S 3 daggered \textit{nihil mutasset
neglegentia hoc quod cum fortiter et diligenter} preserved with
daggers in body.
\item \textit{Att.} 8.7 \S 2 \textit{malle me cum Pompeio vinci
quam cum istis vincere} preserved with the bitter-antithetical
landing \textit{``if that was my preference, it has come to
pass: I have been conquered.''}
\item \textit{Att.} 8.8 \S 1 Sophocles \textit{Oedipus at
Colonus} 1023--4 (\textit{$\pi$$\rho$$\grave{o}$$\varsigma$ $\tau$$\alpha$$\tilde{u}$$\theta$' $\dots$ $\tau$$\grave{o}$ $\gamma$$\grave{\alpha}$$\rho$ $\epsilon$$\tilde{u}$ $\mu$$\epsilon$$\tau$' $\dot{\epsilon}$$\mu$$o$$\tilde{u}$}) cited; the \textit{``for the right is with me''} reading of $\tau$$\grave{o}$ $\epsilon$$\tilde{u}$ is interpretively loaded; flag.
\item \textit{Att.} 8.9 \S 2 broken \textit{ad quintum miliarium}
sentence (lacks finite verb) rendered as paratactic interjection
preserving Cicero's shape rather than emending.
\item \textit{Att.} 8.9 \S 3 \textit{Cinneam illam crudelitatem}
kept as \textit{``the Cinnan kind of cruelty''}; Cinna's
massacres of 87 BC the implicit reference.
\item \textit{Att.} 8.11 \S 1 \textit{perfectorem} rendered
\textit{``bringer-to-completion''} preserving the formal weight
of the \textit{De Re Publica} vocabulary.
\item \textit{Att.} 8.11 \S 3 triple-daggered slave-conscript
prophecy (\textit{qaut utriusque in / iptio / universam})
rendered to broad sense.
\item \textit{Att.} 8.11 \S 3 \textit{iamque mari magno} treated
as tragic-fragment quotation (likely Pacuvius), preserved in
quotes without source-attribution in body.
\item \textit{Att.} 8.11 \S 2 \textit{genus illud Sullani regni}
rendered \textit{``that kind of Sullan kingship''} preserving
the Roman political category Cicero is naming.
\item \textit{Att.} 8.14 \S 1 daggered \textit{diariis} rendered
\textit{``daily rations''} per standard conjecture.
\item \textit{Att.} 8.15 \S 1 daggered \textit{authemonis} read
with Shackleton Bailey conjecture \textit{Athenarum}; sense:
Atticus contemplating flight to Athens.
\item \textit{Att.} 8.16 \S 2 \textit{nescio quas eius Lucerias}
rendered \textit{``certain `Lucerias' of his''} with the
proscription-list-at-Luceria reference in the headnote;
Caesar-as-Pisistratus typology preserved literally.
\item \textit{Fam.} 8.15 \S 2 daggered \textit{num} rendered to
contextual sense; closing Domitius / Venus / Psecas in-joke
(Caesar = sprung-from-Venus via Iulus; Bellienus = born-of-Psecas
slave) preserved with explanation deferred to headnote / glossary.
\item \textit{Fam.} 8.16 \S 4 Caesar's reported greeting
\textit{`have' mihi dixit} rendered \textit{``said `hail' to
me''} preserving the formal Latin colour of the cinematic
greeting moment.
\item \textit{Fam.} 8.16 \S 2 \textit{optimatem / optimum} closing
pun preserved by translating \textit{optimatem} with the technical
\textit{``optimate''} and pulling the second pole on \textit{``best.''}
\item \textit{Fam.} 14.7 \textit{Tulliolam} rendered \textit{``our
little Tullia''} and \textit{Cicero bellissimus} as \textit{``our
charming little Cicero''} matching the established affectionate-
diminutive register of the Terentia letters.
\end{itemize}

\textbf{Suggested next translation batch} (when session 6 is
landed via \texttt{cowork\_handoff.sh "session 6: ..."} and the
next Cowork session opens):
\begin{itemize}
\item Slice H (\textit{Ad Atticum} 9, the Pompey-evacuation week
and Cicero's first weeks alone after Pompey sails on 17 March
49): \texttt{ad-atticum-09-01} through \texttt{ad-atticum-09-19}
(19 letters, the rolling-crisis register continued from
\textit{Att.} 8; \textit{Att.} 9.7C and 9.11A are the famous
Caesar / Balbus exchange letters where Caesar writes courting
Cicero's neutrality and Cicero forwards them to Atticus
mid-decision). Plus the early \textit{Att.} 10 sequence
(\texttt{ad-atticum-10-01} through, depending on context budget,
\texttt{ad-atticum-10-08} or further), continuing the Formian /
Cuman villa diary through April--May 49 as Cicero finally moves
to follow Pompey to Greece. About 20--28 letters total, same
two-wave 4+4 dispatch pattern as sessions 5 and 6.
\item Slice B' (carry-over from previous sessions, year-range
recommendation letters): \texttt{ad-familiares-13-73},
\texttt{-13-74}, \texttt{-13-76} (the three remaining
year-precision \textit{Fam.} 13 recommendation letters on the
hold list; \texttt{-13-49} done this session). These can be
folded into any wave with light worker capacity.
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\end{itemize}

\textbf{Workflow:}
\begin{enumerate}
\item Cowork reads this section + \texttt{OPERATING\_PLAN.md}
+ \texttt{STYLE.md} at session start.
\item Plans next batch (translation + polishing + Tier 2 phase).
\item Dispatches parallel sub-agents with explicit work-id
lists or infrastructure-phase scope (per CLAUDE.md
\S\ ``Parallel sessions'' and OPERATING\_PLAN \S\ ``Sub-agent
prompt skeleton'').
\item Waits for completion, flips status pending $\to$ drafted
in works.yaml, corrects dates, runs
\texttt{scripts/backfill\_structural.py},
\texttt{scripts/build\_manifest.py}, \texttt{scripts/validate.py}.
\item Updates this section so the next session inherits a clean
pointer.
\end{enumerate}

\textbf{The previous session-5 resume notes below remain
accurate} for the late-50-BC homecoming + Rubicon-week +
early-Feb 49 Pompeian-retreat context; the chronology pointer
has moved forward from \textit{Att.} 7.26 (Formiae, 15 Feb 49)
to \textit{Fam.} 8.16 (Intimilium, 16 Apr 49) on the main
translation track, plus the out-of-sequence \textit{Fam.} 13.49
(47 BC) recommendation carry-over.

---

\textbf{Translation state (post-Cowork-session-5):} 346 / 958
works drafted (\~36\%). Latest drafted: \textit{Ad Atticum} 7.26
(15 February 49 BC, Formian villa --- the closing letter of
\textit{Ad Atticum} book 7, written as Pompey's Italian
position is collapsing and Cicero, sitting in his villa above
the bay, is writing the political diary of the collapse to
Atticus). The chronology pointer has moved from \textit{Ad
Familiares} 14.5 (16 Oct 50 BC, Athens) at session start
through the entire Cilician homecoming (\textit{Att.} 7.1 from
Athens on the eve of sailing, the Tiro-illness cluster
\textit{Fam.} 16.1--16.7 + 16.9 from the Ionian islands and
Brundisium as Cicero leaves Tiro behind sick at Patrae), the
overland north (\textit{Att.} 7.2 Brundisium, 7.3 Trebula, 7.4
Pompeian villa), the December 50 Formiae sequence (\textit{Att.}
7.5--7.9), and then the whole Rubicon week and the Pompeian
retreat through January and the first half of February 49 BC
(\textit{Att.} 7.10--7.26, with the Capua Tiro letters
\textit{Fam.} 16.11--16.12 and the Formiae/Minturnae Terentia
letters \textit{Fam.} 14.18, 14.14 woven in). \textbf{38 letters
drafted in two parallel waves of four workers this session.}

\textbf{Cowork session 5 --- 38 letters drafted across two
parallel waves of four workers each (8 workers total):}
\begin{itemize}
\item Wave 1 (17 letters in four parallel workers, the late-50
BC homecoming + December Formiae sweep): Worker A ---
\textit{Att.} 7.1 (Athens, 16 Oct 50, the substantial closing-
voyage letter with the Iliadic Polydamas / Hector quotation
chain at \S 4--5), \textit{Fam.} 16.1, 16.2, 16.3 (Patrae /
Alyzia, 3--6 Nov 50, the opening Tiro-illness notes with the
unusual four-person household salutations); Worker B ---
\textit{Fam.} 16.4, 16.5, 16.6, 16.7 (Leucas / Actium /
Corcyra, 7--17 Nov 50, the Tiro cluster including the three
letters all dated 7 November from successive stages of the
same day's journey); Worker C --- \textit{Att.} 7.2
(Brundisium, 27 Nov 50, the landing-in-Italy letter with the
opening Onchesmites spondaic-hexameter joke), \textit{Fam.}
16.9 (Brundisium, 28 Nov 50, the last Tiro letter from
Brundisium), \textit{Att.} 7.3 (Trebula in Pontius's villa,
9 Dec 50, the long $\sim$1{,}650-word political-assessment
letter as Cicero works north up the Appian Way) and
\textit{Att.} 7.4 (Pompeian villa, 11 Dec 50); Worker D ---
the December Formiae sweep \textit{Att.} 7.5 (18 Dec), 7.6
(19 Dec), 7.7 (c. 21 Dec --- MAJOR date crux, Perseus dateline
\textit{Iun.} is an OCR error for \textit{Ian.}), 7.8
(27/28 Dec), 7.9 (28/29 Dec).
\item Wave 2 (21 letters in four parallel workers, the
Rubicon-week + Pompeian-retreat sweep): Worker E --- the
Rubicon-week letters \textit{Att.} 7.10 (ad urbem, 18 Jan 49,
the famous \textit{subito consilium cepi} night-departure ---
MAJOR date correction from -02-01), 7.11 (in Campania, 21 Jan
--- range-midpoint correction), 7.12 (Formiae, 23 Jan), 7.13
(Minturnae, 24 Jan), 7.14 (Cales, 27 Jan); Worker F --- the
late-Jan / early-Feb mid-crisis letters \textit{Att.} 7.15
(Capua, 28 Jan), 7.16 (Cales, 29 Jan), 7.17 (Formiae, 2 Feb,
with the \textit{Sestiodesteron} nonce-coinage on Pompey's
Sestius-drafted reply), 7.18 (Formiae, 3 Feb, with the
\textit{pseudo-Hesiodic} maxim), 7.19 (Formiae, 3 Feb,
second-of-day note); Worker G --- the Pompey-retreat letters
\textit{Att.} 7.20 (Capua, 5 Feb), 7.21 (Cales, 8 Feb, before
dawn dictation), 7.22 (Formiae, evening of 8 Feb, with the
daggered \textit{cedendum de oppidis} crux at \S 2), 7.23
(Formiae, evening of 9 Feb, with the aposiopesis
\textit{etsi vivere---}), 7.24 (Formiae, 10 Feb); Worker H ---
the Tiro / Terentia / closing-Att.-7 mix \textit{Fam.} 16.11
(ad urbem, 12 Jan 49 --- off-by-one date correction from
-01-13; the first Tiro letter from Italy with political news),
\textit{Fam.} 14.18 (Formiae, 24 Jan, to Terentia and Tullia),
\textit{Fam.} 14.14 (Minturnae, 25 Jan, follow-up to Terentia
and Tullia from the southward road), \textit{Fam.} 16.12
(Capua, 29 Jan, the long Capua political-narrative letter to
Tiro), \textit{Att.} 7.25 (Formiae, 11 Feb, with the famous
epigram \textit{malas causas semper obtinuit, in optima
concidit}) and \textit{Att.} 7.26 (Formiae, 15 Feb, the closing
letter of book 7 with the Ennian \textit{si te secundo lumine}
verse-tag).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 5 (4 entries):}
\texttt{ad-atticum-07-07}: $-0050-05-23$ placeholder (Perseus
dateline garbled \textit{K. Iun.}) $\to$ $-0050-12-21$ day
(per Shackleton Bailey reading \textit{K. Ian.}; Cicero is
plainly at Formiae in late Dec 50, not at Formiae in May 50
when he was in Cilicia; the \textit{Iun.} / \textit{Ian.}
swap is an OCR/manuscript slip).
\texttt{ad-atticum-07-10}: $-0049-02-01$ placeholder
$\to$ $-0049-01-18$ day (Perseus \textit{xiv sub noctem aut
xiiii ante lucem in K. Febr.} = the night before or before
dawn on 18 Jan; a two-week correction, the famous
\textit{subito consilium cepi} letter belongs FIRST in the
Rubicon week not LAST in it).
\texttt{ad-atticum-07-11}: $-0049-01-24$ range-end
$\to$ $-0049-01-21$ midpoint (Perseus \textit{inter xiv et ix
K. Febr.} = 19--24 Jan; Shackleton Bailey midpoint reading).
\texttt{ad-familiares-16-11}: $-0049-01-13$ off-by-one
$\to$ $-0049-01-12$ day (Perseus \textit{prid. Id. Ian.}
= 12 Jan; OCR-garbled in the source as \textit{pdd.}).
Plus location-cleanup on \texttt{ad-atticum-07-04}
(\textit{location\_written} field had a fetch-script
extraction artifact \textit{``in Pompeiano iv aut''} truncated
to \textit{``in Pompeiano''}).
The chronological-gap warning at end of session is 36 pending
works dated earlier than the latest drafted (up from 34); the
new entrants are \textit{Fam.} 16.8 (Jan 49, month precision,
slipped past as the chronology pointer leapt forward) and
\textit{Fam.} 14.5 was already drafted so the count includes
mostly long-standing year-precision recommendation letters in
the \textit{Fam.} 13 series.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write
the shared jsonl directly to avoid concurrent-write contention;
PM or future enrichment pass should consolidate):
\begin{itemize}
\item \textit{Att.} 7.1 \S 4--5 the Iliadic Polydamas / Hector
quotation chain (\textit{Il.} 22.99--110 + \textit{Il.} 9.345)
used as one continuous self-rebuke; the pivot ``who? You
yourself'' across the section boundary depends on the reader
catching that Polydamas is Atticus.
\item \textit{Att.} 7.1 \S 5 the daggered \textit{ut stultus}
treated as the proverb ``let the fool speak first.''
\item \textit{Att.} 7.1 \S 6 the daggered sum \textit{cIↃ}
rendered as the standard ``about a million sesterces.''
\item \textit{Att.} 7.3 \S 3 \textit{custos urbis} as Atticus's
quotation of Cicero's own \textit{De re publica} persona;
the layered self-reference noted in headnote.
\item \textit{Att.} 7.3 \S 10 the \textit{Piraeea / Piraeum / in}
declension joke preserved in the body with the Latin terms
bracketed.
\item \textit{Att.} 7.3 \S 12 daggered \textit{satis},
\textit{aperierimus}, \textit{reum} rendered along the
conjectural sense per Shackleton Bailey.
\item \textit{Att.} 7.4 location: works.yaml carried
\textit{Brundisi} as \textit{location\_written}, corrected to
\textit{in Pompeiano} per Perseus dateline.
\item \textit{Att.} 7.7 dateline crux: Perseus
\textit{inter xiv et x K. Iun.} (impossible: Cicero in
Cilicia in May 50) treated as \textit{K. Ian.}, the
Shackleton Bailey reading; rendered as a December 50 BC
letter from Formiae.
\item \textit{Att.} 7.10 dateline crux: works.yaml carried
\textit{-0049-02-01}, corrected per Perseus \textit{xiv sub
noctem aut xiiii ante lucem in K. Febr.} to \textit{-0049-01-18}.
\item \textit{Att.} 7.11 \S 1 the unidentified iambic-trimeter
Greek tag \textit{τὴν θεῶν μεγίστην ὥστ' ἔχειν τυραννίδα}
preserved with English gloss; possibly Euripides, flag for
allusions pass.
\item \textit{Att.} 7.13 \S 3 the truncated Greek \textit{πρὸς
τὸ} with Shackleton Bailey's \textit{καλόν} supplied
(``regarding what is fitting in itself'').
\item \textit{Att.} 7.13 \S 4 truncated Greek \textit{μάντις δ'}
preserved minimally as ``the prophet.''
\item \textit{Att.} 7.13 \S 4 the obscure ``number of Plato''
reference (\textit{Republic} 8.546b--c nuptial number) flagged
in headnote.
\item \textit{Att.} 7.15 \S 2 daggered \textit{is auditus in
consilio} rendered ``he was heard out in council'' on the
conjectural sense.
\item \textit{Att.} 7.17 \textit{Sestiodesteron} (\textit{Σηστιωδέστερον})
as Ciceronian nonce-coinage from Sestius's name; rendered
``in the manner of Sestius.''
\item \textit{Att.} 7.18 the \textit{pseudohesiodeion}
(\textit{ψευδησιόδειον}) maxim with \textit{μηδὲ δίκην}
preserved minimally; Shackleton Bailey suggests a
``not even a lawsuit between friends'' line.
\item \textit{Att.} 7.20 the Pompey-as-Phalaris /
Pompey-as-Pisistratus running typology of tyranny worth
flagging across the Att 7--8 sequence.
\item \textit{Att.} 7.21 \textit{φαινοπροσωπεῖν} hapax in
extant Cicero; rendered ``to show their faces.''
\item \textit{Att.} 7.22 \S 2 daggered \textit{cedendum de
oppidis} rendered ``I think the right course is to give
way; about whether to leave the towns I need counsel.''
\item \textit{Att.} 7.23 the aposiopesis \textit{etsi vivere---}
preserved as ``though to go on living---'' with the dash.
\item \textit{Att.} 7.25 the epigram \textit{malas causas
semper obtinuit, in optima concidit} rendered ``He carried
his bad causes through always; in the best of causes he
has collapsed.''
\item \textit{Att.} 7.26 the embedded verse \textit{si te
secundo lumine hic offendero} (likely Ennian iambic
trimeter) preserved in quotation marks as Caesar's threat
quoted; flag for allusions pass.
\item \textit{Fam.} 14.14 the manuscript subscription
\textit{VIII K. Quint.} (July) universally corrected by
editors to \textit{VIII K. Febr.}; translated as the
emended January date with the slip noted.
\item \textit{Fam.} 14.14 ``potestis in homo amens'' Perseus
text is corrupt for \textit{sin homo amens}; rendered
``but if a man out of his mind\dots''
\item \textit{Fam.} 16.4 \textit{ius enim dandum tibi non fuit}
taken as ``broth'' (the food sense, standard medical reading)
not \textit{ius} as legal noun.
\item \textit{Fam.} 16.4 \textit{omnes Graeci} (``first because
all Greeks are careless'') rendered flat per STYLE.md, no
softening of the ethnic crack.
\item \textit{Fam.} 16.5 the Perseus \textit{Leucade so
proficiscens} where \textit{so} is plainly an OCR artifact;
rendered as ``on the point of setting out from Leucas.''
\item \textit{Fam.} 14.18 / 14.14 / 16.12 the standard Cicero
political-news register: the Tiro letter (16.12) carries the
full Capua narrative; the Terentia letters carry household-
practical instructions.
\end{itemize}

\textbf{Suggested next translation batch} (when session 5 is
landed via \texttt{cowork\_handoff.sh "session 5: ..."} and
the next Cowork session opens):
\begin{itemize}
\item Slice G (the \textit{Ad Atticum} 8 sequence --- mid-February
through early March 49 BC, the rolling crisis as Pompey
abandons Italy from Brundisium and Cicero in his Formian
villa records each day's news of the collapse and his own
agonising about whether to follow): \texttt{ad-atticum-08-01}
through \texttt{ad-atticum-08-16} (16 letters, mostly short to
medium, very parallelisable; \textit{Att.} 8.3 to Vibullius
on the night Pompey crosses is the dramatic centerpiece).
Plus \texttt{ad-familiares-16-08} (Jan 49 carry-over Tiro
letter, slipped into the chronological gap when the pointer
leapt past mid-Jan), \texttt{ad-familiares-08-15} (9 Mar 49,
Caelius newsletter), \texttt{ad-familiares-14-07} (April 49,
Terentia letter --- a major one, \textit{the Caieta departure}
letter where Cicero finally sails to join Pompey), and
\texttt{ad-familiares-08-16} (16 Apr 49, Caelius newsletter
from inside Caesar's camp --- the famous defection-to-Caesar
letter). About 20 letters total, similar two-wave pattern to
session 5.
\item Slice B' (carry-over from previous sessions, year-range
recommendation letters): \texttt{ad-familiares-13-49} (47 BC,
re-fetch needed --- the orphan placeholder stub from session
1 still in latin/letters/054bc- prefix should be removed by
\texttt{cowork\_handoff.sh}; the entry's date is now correct
at $-0047-10-15$ but the latin file at the new $047bc-$ prefix
needs fetching), \texttt{-13-73}, \texttt{-13-74},
\texttt{-13-76} (the four year-precision \textit{Fam.} 13
recommendation letters still on the hold list).
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\end{itemize}

\textbf{Workflow:}
\begin{enumerate}
\item Cowork reads this section + \texttt{OPERATING\_PLAN.md}
+ \texttt{STYLE.md} at session start.
\item Plans next batch (translation + polishing + Tier 2 phase).
\item Dispatches parallel sub-agents with explicit work-id
lists or infrastructure-phase scope (per CLAUDE.md
\S\ ``Parallel sessions'' and OPERATING\_PLAN \S\ ``Sub-agent
prompt skeleton'').
\item Waits for completion, flips status pending $\to$ drafted
in works.yaml, corrects dates, runs
\texttt{scripts/backfill\_structural.py},
\texttt{scripts/build\_manifest.py}, \texttt{scripts/validate.py}.
\item Updates this section so the next session inherits a clean
pointer.
\end{enumerate}

\textbf{The previous session-4 resume notes below remain
accurate} for the Cilician-proconsulship homecoming context;
the only thing that has changed is that the chronology pointer
has moved forward from \textit{Fam.} 14.5 (Athens, 16 Oct 50)
to \textit{Att.} 7.26 (Formiae, 15 Feb 49).

---

\textbf{Translation state (post-Cowork-session-4):} 308 / 958
works drafted (\~32\%). Latest drafted: \textit{Ad Familiares}
14.5 (16 October 50 BC, Athens --- the brief Terentia note
written as Cicero is about to sail for Italy at the end of
his Cilician proconsulship). The chronology pointer has moved
from \textit{Ad Atticum} 5.20 (21 Dec 51 BC) at session start
through the entire 50 BC year of the Cilician proconsulship:
the Laodicea assizes (Feb 50), the Salaminian-loan / Brutus--
Scaptius affair (the heart of \textit{Att.} 6.1--6.3), the
spring--summer Caelius newsletter exchange, the
Cato--Cicero supplicatio pair (\textit{Fam.} 15.5--15.6), the
homeward journey letters from Cilicia through Tarsus, Rhodes,
Ephesus, and Athens, and the last-minute Athens note to
Terentia (\textit{Fam.} 14.5) on the eve of departure.
\textbf{27 letters drafted in two parallel waves of four
workers this session.}

\textbf{Cowork session 4 --- 27 letters drafted across two
parallel waves of four workers each (8 workers total):}
\begin{itemize}
\item Wave 1 (14 letters in four parallel workers):
Worker A --- the Feb 50 Laodicea-assizes cluster
\textit{Fam.} 14.5 (Athens, mid-Oct note to Terentia, dropped
in this batch by chronology of recipient/category convenience),
13.54, 13.58, 13.59, 13.63 (Feb 50 recommendation letters from
Laodicea to Thermus, C. Titius Rufus, Curtius Peducaeanus, and
Silius Nerva on behalf of Marcilius, Custidius, Fadius, and
Laenius); Worker B --- the long Salaminian-loan letter
\textit{Att.} 6.1 (24 Feb 50, Laodicea, $\sim$3{,}500 English
words across 24 sections --- the major Brutus--Scaptius
account, the self-portrait of Cicero's administration, the
Mucius-Scaevola edict as model, all wrapped in the running
news-to-Atticus); Worker C --- the Feb--Apr 50 Appius and
Caelius mix \textit{Fam.} 3.7, 3.9, 2.11, 2.14 (the patching-
up letter to Appius after his complaint; the support letter
to Appius under prosecution; the spring Caelius reply with
the \textit{simiolus} joke; the one-paragraph quick brush-off);
Worker D --- the spring--summer 50 Atticus journey letters
\textit{Att.} 6.4, 6.5, 6.7, 6.6 (Jun--Aug 50, the
\textit{epoche} / \textit{epoche} Sceptic pun, the Greek-cipher
Philotimus/Milo-estate ledger, the Tarsus and Rhodes notes).
\item Wave 2 (13 letters in four parallel workers): Worker E
--- the substantive May--Jun Laodicea Atticus letters
\textit{Att.} 6.2 ($\sim$1{,}890 English words, 10 sections;
the continuation of the Salaminian-loan account plus the
self-portrait of provincial integrity) and \textit{Att.} 6.3
($\sim$1{,}610 English words, 9 sections; the camp letter
with Pompey-as-stationary joke, the nephew Quintus, and the
Brutus loans to Ariobarzanes); Worker F --- the Cicero
Cilician-camp Caelius replies \textit{Fam.} 2.13 (early May
50, MAJOR date correction from Oct year-placeholder), 2.12
(the famous \textit{Urbem, urbem, mi Rufe, cole et in ista
luce vive} homesickness from the Cilician camp), 2.15 (Side,
early Aug, the curio-and-supplicatio negotiation with the
\textit{alterum me} on Quintus); Worker G --- the Caelius
newsletter run \textit{Fam.} 8.11 (Apr--May, the Curio-
defection bombshell with \textit{scaena rei totius}), 8.13
(late May / early Jun, the Dolabella--Tullia marriage news
and the Hortensius-dying coda), 8.12 (Sep, the Lex Scantinia
grievance against Appius), 8.14 (Sep 24, the famous
\textit{in dissensione domestica} political-realism passage,
\textit{lomentum aut nitrum} on the censorship); Worker H ---
the Cato--Cicero supplicatio pair plus the homecoming Atticus
letters \textit{Fam.} 15.5 (Cato's chilly reply,
\textit{praerogativam} as metaphor), 15.6 (Cicero's icy-
courteous response, the Naevius \textit{laetus sum laudari}
fragment quoted fresh), \textit{Att.} 6.8 (Ephesus, 1 Oct,
the nephew \textit{numquid moleste fers de illo qui se solet
anteferre patruo sororis tuae fili?} swipe), \textit{Att.}
6.9 (Athens, 15 Oct, the rich Sceptic \textit{epechein /
athetesis / epoche} cluster, the closing \textit{in arce
Athenis statio mea} as Caesar moves four legions on
Placentia).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 4 (6 entries):}
\texttt{ad-familiares-14-05}: $-0050-02-06$ year-placeholder
$\to$ $-0050-10-16$ day (Perseus \textit{a. d. xvii K. Novemb.}
= 16 Oct; eight-month correction, the Terentia note belongs
in mid-October not early Feb).
\texttt{ad-familiares-02-13}: $-0050-10-18$ book-level fallback
$\to$ $-0050-05-04$ day (Perseus \textit{inter K. et Non.
Maias} = 1--7 May; mid-point chosen for the JSON ISO date).
A five-month correction; the letter belongs in early-May
chronologically, not Oct.
\texttt{ad-familiares-08-11}: $-0050-05-15$ placeholder
$\to$ $-0050-04-30$ day (Perseus \textit{ex. m. Apr. aut in.
Mai.} = late-April / early-May; 30 Apr is the canonical
compromise point).
\texttt{ad-familiares-08-13}: $-0050-06-13$ placeholder
$\to$ $-0050-06-01$ day (Perseus \textit{ex. m. Mai. aut in.
Iun.} = late-May / early-Jun; 1 Jun the canonical compromise).
\texttt{ad-familiares-15-05}: $-0050-05-15$ placeholder
$\to$ $-0050-04-30$ day (Perseus \textit{ex. m. Apr. vel in.
Mai.}; end-Apr per the canonical reading).
\texttt{ad-atticum-06-08}: $-0050-09-31$ INVALID DATE
(September has only 30 days) $\to$ $-0050-10-01$ day
(Perseus \textit{K. Oct.} = 1 Oct).
The chronological-gap warning at end of session is 34 pending
works dated earlier than the latest drafted, up from 22 at
end of session 3; this is the expected effect of moving the
chronology pointer ten months forward (from Dec 51 BC to Oct
50 BC) into a year with several remaining year-precision
pending entries scattered across the 51--47 BC range.

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write
the shared jsonl directly to avoid concurrent-write contention;
PM or future enrichment pass should consolidate):
\begin{itemize}
\item \textit{Att.} 6.1 \S 5 \textit{centesimis ... quaternas
centesimas} --- rendered explicitly as ``twelve percent
compounded'' / ``forty-eight percent'' to make the moral arithmetic
of the Salaminian loan readable; flag for any later commentary pass.
\item \textit{Att.} 6.1 \S 16 the Latin breaks off at just
$\tau o$\dots\ (unfinished Greek phrase, probably
\textit{to atopotaton}); rendered as ``But the strangest thing''
as a defensible guess from context.
\item \textit{Att.} 6.1 \S 23 daggered Lucceius passage
rendered with \textit{[text corrupt]} markers; \S 25
\textit{Genuarii} flagged the same way.
\item \textit{Att.} 6.1 \S 14 \textit{Q. Muci P. f.} (Q. Mucius
Scaevola Pontifex, whose Asiatic edict Cicero is consciously
emulating); the genealogy abbreviation preserved.
\item \textit{Att.} 6.2 \S 3 the Phlious / Opous / Sipous
declension joke --- left as Greek-bracketed transliteration
without an English gloss; the joke \emph{is} the Greek forms.
\item \textit{Att.} 6.2 \S 7 \textit{nec perpetuis sed
renovatis quotannis} --- rendered ``not running continuously
but renewed every year''; deliberately resisted the post-medieval
``simple interest'' / ``compound interest'' vocabulary.
\item \textit{Att.} 6.2 \S 8 \textit{Spartaco minus multi primo
fuerunt} --- preserved Cicero's savage rhetorical bite.
\item \textit{Att.} 6.3 \S 1 unidentified Greek hexameter
($\pi o\lambda\lambda\grave\alpha\ \delta'\ \dot\varepsilon\nu\
\mu\varepsilon\tau\alpha\iota\chi\mu\acute\iota\omega\
\nu\acute o\tau o\varsigma\ \kappa\upsilon\lambda\acute\iota\nu
\delta\varepsilon\iota\ \kappa\acute\upsilon\mu\alpha\tau'\
\varepsilon\dot\upsilon\rho\varepsilon\acute\iota\eta\varsigma\
\dot\alpha\lambda\acute o\varsigma$); allusion source pending,
flag for a future allusions-sidecar pass.
\item \textit{Att.} 6.3 \S 7 Lucilius Granius line preserved as
direct quotation; suspected Lucilius fragment, flag.
\item \textit{Att.} 6.3 \S 8 \textit{de sorore} rendered ``about
his mother'' --- a deliberate relation-flip so the boy Quintus's
perspective lands; should be logged.
\item \textit{Att.} 6.4 \S 2 \textit{$\mu\upsilon\sigma\tau\iota
\kappa\acute\omega\tau\varepsilon\rho o\nu$} preceding a corrupt
Greek-script ledger --- rendered as Greek-paraphrase since the MS
text is corrupt at \textit{$\nu o\acute\eta\sigma\eta\varsigma$}.
\item \textit{Att.} 6.5 \S 2 the long Greek-script ledger
(24 / 48 minae, ``Crotonian'' / ``Chersonesian'' assets, the
\textit{Conon} agent) most likely the Philotimus / Milo-estate
matter; surface arithmetic translated, referents left to headnote.
\item \textit{Att.} 6.6 \S 3 the Sceptic
\textit{$\dot\varepsilon\pi\acute\varepsilon\chi\varepsilon\iota\nu$
/ $\dot\varepsilon\pi o\chi\dot\eta\varsigma$} pun on Atticus
``suspending judgment'' on the succession question --- a
deliberate philosophical wink to the philhellene Epicurean.
\item \textit{Att.} 6.9 \S 3 \textit{epechein / athetesis /
epoche} cluster preserved with English glosses; the conceptual
distinction is the joke.
\item \textit{Att.} 6.9 \S 3 \textit{$\varphi\upsilon\rho\alpha
\tau o\widehat\upsilon$} (``kneader / muddler / schemer'')
rendered ``schemer''; alternatives ``intriguer'' (Hofmann),
``muddler''.
\item \textit{Fam.} 3.7 \S 5 \textit{Appietas / Lentulitas}
rendered ``Appius-ness / Lentulus-ness'' (with quote-marks)
to preserve the coinage bite.
\item \textit{Fam.} 3.7 \S 6 Iliadic tag (Iliad 1.174--75,
Achilles to Agamemnon) plus \textit{philaitios}; preserved
the quote and the gloss.
\item \textit{Fam.} 3.9 \S 2 \textit{longi subselli iudicatio}
(Pompey's coinage) rendered ``the judgment of `the long bench'''
with the gloss attributed to Pompey in the body.
\item \textit{Fam.} 2.12 \S 2 \textit{Urbem, urbem, mi Rufe,
cole et in ista luce vive} --- preserved the anaphora as ``The
City, my dear Rufus, the City''; \textit{peregrinatio} rendered
``foreign service'' rather than ``travel''; \textit{sordidast}
rendered ``squalid''.
\item \textit{Fam.} 2.13 \S 3 \textit{veternus civitatis}
rendered ``the lethargy of the state'' with the medical-torpor
metaphor continued in ``frozen over into peace'' for
\textit{congelasse otio}.
\item \textit{Fam.} 2.13 \S 1 \textit{kōmikos martys} ---
Cicero's New-Comedy stage-witness idiom for Phania.
\item \textit{Fam.} 2.15 \S 1 the launch-prompt brief said
panther-vocabulary is in 2.15; correction: it is in 2.11, not
2.15. 2.15 is the Curio-and-supplicatio negotiation plus the
Tullia--Dolabella marriage note; the panther material is in
2.11 \S 2.
\item \textit{Fam.} 8.11 \S 3 \textit{praevaricator causae
publicae} (``collusive prosecutor of the public cause'')
technical term, worth a translator-notes line.
\item \textit{Fam.} 8.13 \S 2 \textit{frequens senatus in alia
omnia iit} (the technical \textit{in alia omnia ire})
rendered ``a full Senate went against''; the daggered
$\dag$\textit{aut non curet} rendered with editorial sense.
\item \textit{Fam.} 8.12 the launch-prompt brief described 8.12
as a panther-letter; correction: 8.12 is entirely the Lex
Scantinia grievance against Appius. The panther-and-aedile-
games material is in 8.9 (already drafted), 8.2, 8.4, 8.6.
\item \textit{Fam.} 8.14 \S 3 the marquee \textit{in dissensione
domestica} passage rendered with the cognate ``honourable'' for
\textit{honestiorem partem} and the bare ``stronger'' for
\textit{firmiorem}; \textit{civiliter} rendered ``by civil means''
(avoiding the older ``civilly'').
\item \textit{Fam.} 8.14 \S 4 \textit{lomentum aut nitrum}
(bean-meal cosmetic paste or natron) preserved as two grades
of beautifying agent so the joke on the censorship lands.
\item \textit{Fam.} 8.14 \S 4 \textit{curre, per deos atque
homines!} --- ``Run, by gods and men!''; Roman oath, not
Christianised.
\item \textit{Fam.} 15.5 \S 2 the doubled-subjunctive
architecture (\textit{si ... mavis ... gaudeo; quod si ...
mavis, neque ... et triumpho multo clarius est ...}) rendered
with the hinge ``then I have two things to say'' to preserve
Cato's pivot without flattening the conditional.
\item \textit{Fam.} 15.5 \textit{praerogativam} rendered
``foretaste'' (metaphorical sense) rather than the technical
``first vote'' of the centuriate.
\item \textit{Fam.} 15.6 the Naevius \textit{laetus sum laudari
me, ... abs te, pater, a laudato viro} fragment rendered freshly
from the Latin, deliberately not echoing Shackleton Bailey's
phrasing.
\item \textit{Fam.} 15.6 \textit{voluntatis, non enim dicam
``cupiditatis''} --- the praeteritio preserved as ``my wish
--- for I will not call it `my craving'''.
\item \textit{Fam.} 13.54 / 13.58 / 13.59 / 13.63 launch-prompt
brief miscalled the recipients; the actual Latin (and works.yaml
\textit{recipient} fields) are: 13-54 to Q. Minucius Thermus
for young M. Marcilius; 13-58 to C. Titius Rufus urban praetor
for L. Custidius; 13-59 to C. Curtius Peducaeanus praetor for
M. Fadius; 13-63 to P. Silius Nerva propraetor for M. Laenius.
Translated to the actual Latin, not the brief.
\item Perseus typo flagged: 13-63 dateline ``\textit{foetasse}''
(should be \textit{fortasse}); the typo is preserved in
works.yaml's location\_written field too. Worth a metadata
cleanup pass at the PM level.
\end{itemize}

\textbf{Suggested next translation batch} (when session 4 is
landed via \texttt{cowork\_handoff.sh "session 4: ..."} and
the next Cowork session opens):
\begin{itemize}
\item Slice F (the 49 BC opening --- Caesar's crossing of the
Rubicon and Cicero's return to Italy in the middle of a civil
war; one of the most chronologically dense and politically
charged stretches of the corpus): \texttt{ad-atticum-07-01}
through \texttt{ad-atticum-07-26} (the great Att 7 sequence
from Athens in mid-Nov 50 through the Brundisium crossing
and the long stationed-near-Formiae sequence as Cicero
agonises over which side to take). Many of these are short
to medium; several substantial (7.7, 7.9, 7.11, 7.13).
\texttt{ad-familiares-16-01} through \texttt{-16-09} (the
Tiro illness-at-Patrae letters from late 50, with Cicero
leaving Tiro behind at Patrae as he sails for Italy). The
Caelius newsletters \texttt{ad-familiares-08-15, -08-16,
-08-17} (the late-50 / early-49 Caelius bulletins as the
civil-war crisis unfolds). \textit{Fam.} 14.6 and 14.7
(further Terentia letters; check dates).
About 30--40 letters, similar parallelisable pattern to
this session.
\item Slice B' (carry-over from previous sessions, year-range
recommendation letters): \texttt{ad-familiares-13-49}
(47 BC, re-fetch needed --- the orphan placeholder stub from
session 1 still in latin/letters/054bc- prefix should be removed
by \texttt{cowork\_handoff.sh}; the entry's date is now correct
at $-0047-10-15$ but the latin file at the new $047bc-$ prefix
needs fetching), \texttt{-13-73}, \texttt{-13-74},
\texttt{-13-76} (the four year-precision \textit{Fam.} 13
recommendation letters still on the hold list).
\item Slice C (substantial speeches blocking the year-precision
sweep, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC), \texttt{partitiones-oratoriae},
\texttt{pro-plancio}, \texttt{pro-rabirio-postumo},
\texttt{pro-scauro}.
\end{itemize}

\textbf{Workflow:}
\begin{enumerate}
\item Cowork reads this section + \texttt{OPERATING\_PLAN.md}
+ \texttt{STYLE.md} at session start.
\item Plans next batch (translation + polishing + Tier 2 phase).
\item Dispatches parallel sub-agents with explicit work-id
lists or infrastructure-phase scope (per CLAUDE.md
\S\ ``Parallel sessions'' and OPERATING\_PLAN \S\ ``Sub-agent
prompt skeleton'').
\item Waits for completion, flips status pending $\to$ drafted
in works.yaml, corrects dates, runs
\texttt{scripts/backfill\_structural.py},
\texttt{scripts/build\_manifest.py}, \texttt{scripts/validate.py}.
\item Updates this section so the next session inherits a clean
pointer.
\end{enumerate}

\textbf{The previous resume notes below remain accurate} for
chronological sweep work; the only thing that has changed is the
chronology pointer has moved forward.

\textbf{Translation state (post-Cowork-session-3):} 281 / 958 works
drafted (\~29\%). Latest drafted: \textit{Ad Atticum} 5.20
(21 December 51 BC, Cilicia --- the long closing letter of
Atticus book 5, summing up the Cilician campaign through the
fall of Pindenissus on 17 December, the Saturnalia gift of
plunder to the soldiers, the supplicatio play in the senate,
and the closing on Tullia). The chronology pointer has moved
from \textit{Fam.} 2.7 (19 Dec 51 BC) at session start through
the entire mid-year Cilician sweep to the close of 51 BC.
The whole \textit{Att.} 5 book is now drafted end-to-end ---
the spring journey-letters from Pompeii to Tarentum (already
drafted), the early-summer Brundisium-and-Actium sequence
(5.8 from session 2), the Aegean crossing (5.9 Actium, 5.10
Athens, 5.11 Athens, 5.12 Delos, 5.13 Ephesus on landing in
Asia), the inland march through the conventus (5.14 Tralles,
5.15 Laodicea, 5.16--5.17 on the road to Iconium and the
camp), the news of the Parthian invasion (5.18 from the camp
at Cybistra, 5.19 Pomptinus's arrival), and the year-end
campaign summary (5.20). The Caelius-newsletter run is now
substantially populated: 8.3 (June, on the elder Curio's
death), 8.4--8.5 (Aug, the consular candidate Hirrus and the
impending tribunate of the younger Curio), 8.8 (early Oct,
with the full senate-debate text and the senators-absent
register --- the longest of the Caelius letters), 8.9 (Sep,
elections), 8.10 (Nov, Parthian rumours). The Cicero-side of
the gossip-correspondence drafted in matched pairs (2.8, 2.9,
2.10). The Appius correspondence reaches its crisis with
3.5--3.6 and the long expostulation 3.8 (8 Oct). The
senatorial dispatches are in: 15.1 (Cybistra, 19 Sep, the
first Parthian-threat dispatch), 15.2 (22 Sep, the longer
follow-up to the senate, magistrates, and tribunes), 15.3
(30 Aug, the first Cato letter), 15.7 (21 Sep, the courtesy
note to C. Marcellus cos.-elect), 15.10 (Nov, the
supplicatio-support letter to M. Marcellus cos. 51).
+29 letters drafted in two parallel waves this session.

\textbf{Cowork session 3 --- 29 letters drafted across two
parallel waves of four/two workers:}
\begin{itemize}
\item Wave 1 (20 letters in four parallel workers): Worker A ---
the Atticus 5 Aegean-crossing letters \textit{Att.} 5.9, 5.10,
5.11, 5.12, 5.13 (June--July 51 BC, the slow journey east from
Actium through Athens to Ephesus); Worker B --- the Atticus 5
inland-march and Parthian-news letters 5.14, 5.15, 5.16, 5.17,
5.18 (July--September, ending with the news of the Parthian
crossing of the Euphrates from the camp at Cybistra); Worker C
--- the Caelius newsletters and Cicero's first response
\textit{Fam.} 8.3, 8.4, 8.5, 8.9, 2.8 (June--September, the
running political bulletin from Rome and Cicero's instructions
for the Roman-news service); Worker D --- the Appius
correspondence and senatorial dispatches \textit{Fam.} 3.5,
3.6, 15.1, 15.3, 15.7 (July--September, the increasingly
strained handover with Appius and the formal dispatches to
the senate and Cato on the Parthian situation).
\item Wave 2 (9 letters in two parallel workers): Worker E ---
\textit{Att.} 5.19 (22 Sep), \textit{Fam.} 15.2 (22 Sep
senate dispatch), 15.10 (Nov, to M. Marcellus on the
supplicatio), and the long 3.8 (8 Oct, the great Appius
expostulation, $\sim$1{,}650 English words); Worker F ---
the autumn Caelius newsletter run \textit{Fam.} 8.8 (early
Oct, the senate-debate transcript and the famous
absentees-register, $\sim$1{,}820 English words), 2.9, 8.10,
2.10 (Cicero from Pindenissus camp), and the closing
\textit{Att.} 5.20 (21 Dec, $\sim$1{,}510 English words ---
the year-end campaign summary).
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 3 (7 entries):}
\texttt{ad-atticum-05-09}: $-0051-07-01$ year $\to$
$-0051-06-17$ day (Perseus \textit{Acti xvii K. Quint.}; the
worker chose 17 June; the strict inclusive-counting reading
would be 15 June, but the worker's choice is defensible and
within the Tyrrell--Purser conventional range).
\texttt{ad-atticum-05-11}: $-0051-07-07$ year $\to$
$-0051-07-06$ day (Perseus \textit{pr. Non. Quint.} = pridie
Nonas = day before 7 July).
\texttt{ad-atticum-05-15}: $-0051-08-05$ Nones $\to$
$-0051-08-03$ day (Perseus \textit{iii Non. Sext.} and the body
itself confirms; arrival at Laodicea was 31 July, writing day
was 3 August).
\texttt{ad-atticum-05-20}: $-0051-12-29$ year-end $\to$
$-0051-12-21$ day (Perseus range \textit{inter a. d. xii et iv
K. Ian.} = 21--29 Dec; aligned to the early end of the range
per the worker's JSON dating).
\texttt{ad-familiares-08-08}: $-0051-10-15$ month $\to$
$-0051-10-02$ day (Perseus \textit{in. m. Oct.} = beginning
of October).
\texttt{ad-familiares-08-10}: $-0051-12-01$ year $\to$
$-0051-11-18$ day (Perseus \textit{xiiii K. Dec.} and the body's
\S 3 confirms: ``I am writing this letter on a.d. xiiii K.
Decembris'' = 18 November).
\texttt{ad-familiares-02-10}: $-0051-07-15$ placeholder
$\to$ $-0051-11-15$ day --- a four-month correction (Perseus
\textit{a. d. xvii K. Decembr.}; placeholder was wildly wrong).
File rename not required (same year-prefix \texttt{051bc-}).
The chronological-gap warning at end of session is 22 pending
works dated earlier than the latest drafted (down from 50 at
end of session 2; the gap is closing as the chronological
sweep fills out 51 BC).

\textbf{Foundation infrastructure built this session:}
\texttt{OPERATING\_PLAN.md} added (the multi-session strategy,
the per-session loop, the multi-letter-per-agent dispatch
pattern); \texttt{scripts/cowork\_handoff.sh} added (one-command
session landing for Alexander); \texttt{CLAUDE.md} updated with
the Cowork operating model section. Scheduled task
\texttt{cicero-2hr-translation} registered (every 2 hours,
auto-runs while the Cowork app is open). Two metadata fixes:
\textit{Fam.} 13.49 \texttt{speech\_index} corrected to
\texttt{book:13,letter:159} (Perseus TEI typo upstream) and
date moved to $-0047-10-15$ per dateline; \textit{Q.fr.} 3.6
marked \texttt{no\_perseus: true} (combined with 3.5 in Perseus
TEI = SB 3.5b; translate together).

\textbf{Cowork session 1 --- 22 letters drafted across four
parallel batches:}
\begin{itemize}
\item Batch 1 (autumn 54 BC, 7 letters): \textit{Att.} 4.15--4.19
(complete second-half-54 Atticus sweep), \textit{Q.fr.} 2.10 and
2.11 (date corrected from year-precision placeholders to 13 and
14 Feb 54 BC per Perseus datelines).
\item Batch 2 (late summer / autumn 54 BC, 5 letters):
\textit{Q.fr.} 2.14 (27 Jul) and 2.15 (29 Aug, date refined),
\textit{Fam.} 7.9, 7.16, 7.17 (the Trebatius series; 7.17 date
refined from year to month precision per Perseus dateline).
\item Batch 3 (December 54 BC / early 53 BC, 5 letters):
\textit{Fam.} 1.9 (the long apologia to Lentulus Spinther,
~5650 English words across 26 sections; the political
centerpiece of the post-exile correspondence), \textit{Fam.}
7.10 (Trebatius), \textit{Q.fr.} 3.9 (last surviving letter to
Quintus in book 3), \textit{Fam.} 2.4 (to the young Curio),
\textit{Fam.} 7.11 (Trebatius).
\item Batch 4 (early 53 BC, 5 letters): \textit{Fam.} 2.5 (Curio),
3.1 (the first letter to Appius Claudius Pulcher, opening
book 3 of Familiares and the awkward Cilicia-handover
correspondence), 7.13, 7.18 (Trebatius), 16.14 (to Tiro --- the
first letter in the Tiro sequence to be drafted in this period).
\item Batch 5 (spring 53 BC -- March 52 BC, 12 letters via the
new multi-letter-per-agent pattern --- 4 agents \texttimes\
3 letters each): Tiro group \textit{Fam.} 16.15, 16.10, 16.16
(Quintus's joy letter on Tiro's manumission, date corrected
from year-precision Sept placeholder to late May 53 BC per
Perseus dateline); Trebatius group \textit{Fam.} 7.12, 7.14,
7.15; Curio group \textit{Fam.} 2.6 (the substantive
Milo-consulship appeal), 2.1, 2.2 (condolence on the elder
Curio); mixed group \textit{Fam.} 2.3 (Curio), 5.16 (the
philosophical Titius consolation), 7.27 (the sharp Fadius
putdown).
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention; PM
or future enrichment pass should consolidate):
\begin{itemize}
\item \textit{Att.} 4.15 \S 4 \textit{pusilla quae nunc laborat}
(Tullia vs. personified spirit; chose personal/Tullia reading).
\S 7 \textit{indices gloriosi} (book-roll title-tabs ``title-pages'').
\item \textit{Att.} 4.16 \S 4 \textit{Aureliani} (corrupt MS;
chose the proper-name reading).
\item \textit{Att.} 4.17 \S 1, \S 7 daggered lacunae (rendered as
ellipsis + \textit{[text corrupt]}); \textit{lex Coctia} preserved
with note ``so the manuscripts.''
\item \textit{Att.} 4.18 \S 1, \S 4 daggered Greek-script lacunae
(passed through with \texttt{\textbackslash textgreek\{...\}}).
\item \textit{Att.} 4.19 \S 1 \textit{$\delta\acute{\epsilon}\rho\rho\epsilon\iota\varsigma$}
contested with $\delta\epsilon\iota\lambda\acute{\iota}\alpha\varsigma$;
preserved Perseus printed reading.
\item \textit{Q.fr.} 2.10 launched-prompt date discrepancy
corrected to 13 Feb 54 BC per Perseus dateline; ditto 2.11 to 14 Feb 54.
\item \textit{Q.fr.} 2.11 \S 1 \textit{Idus Decimus erat Caelio dies}
(SB emends to \textit{Idibus Februariis}; preserved Perseus).
\item \textit{Q.fr.} 2.14 \S 2, \S 4 daggered cruxes preserved.
\item \textit{Q.fr.} 2.15 \S 3 \textit{Sundeipnous Sophokleous}
(earliest reference to a play by Quintus Cicero, with Marcus's
``no good'' verdict).
\item \textit{Q.fr.} 3.9 \S 2 \textit{HS cccↃ} corrupt sum; \S 8
\textit{Porcia / Pomponia} preserved as MS Porcia.
\item \textit{Fam.} 1.9 \S 21 \textit{cum dignitate otium} ---
Cicero's signature political formula; should anchor a
\textit{Pro Sestio} / \textit{De Re Publica} crossref pass.
\S 19 Terence \textit{Eunuchus} 440--45 inset (set as a quote
block).
\item \textit{Fam.} 3.1 \S 1 Greek pun coinage \textit{Polias}
$\sim$ \textit{Appias} (Cicero's cult-title joke for Appius's
Minerva).
\item \textit{Fam.} 7.13 the technical-civil-law puns
(\textit{consuli}, \textit{ex iure manum consertum}) flagged in
headnote rather than body.
\item \textit{Fam.} 16.14 \textit{repraesentare} for the promised
manumission (the traditional 53 BC date for Tiro's manumission;
Cicero's enigmatic ``I'll bring it forward'').
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 1 (5 entries):} \texttt{ad-quintum-fratrem-02-10}
$-0054-07-15$ year $\to$ $-0054-02-13$ day;
\texttt{-02-11} $-0054-08-16$ year $\to$ $-0054-02-14$ day;
\texttt{-02-15} $-0054-08-15$ month $\to$ $-0054-08-29$ month;
\texttt{ad-familiares-07-17} $-0054-10-18$ year $\to$
$-0054-10-29$ month. These move the affected letters into the
day/month-precision tier and may trigger a finer chronological
re-ordering in subsequent manifest regenerations.

\textbf{Sandbox caveats from session 1} (relevant to
re-running this kind of session from a Cowork sandbox):
\begin{enumerate}
\item Sandbox has no SSH access to \texttt{origin} --- pushes
and fetches all fail. Cowork in this session translated, edited
\texttt{meta/works.yaml}, ran regeneration scripts (backfill /
manifest / validate), but did \emph{not} commit. All session-1
output is untracked/modified in the working tree, awaiting an
Alexander-side commit + push.
\item Sandbox cannot delete files. A leftover
\texttt{.git/index.lock} from an early \texttt{git status} call
is blocking all git writes from the sandbox side. Before the
session-1 batch can be committed: \texttt{rm .git/index.lock}
in the local repo, then \texttt{git add -A \&\& git commit -m
"Cowork session 1: +22 letters drafted (54 BC autumn sweep
through April 53 BC) \&\& git push}.
\item A failed \texttt{fetch\_latin.py ad-familiares-13-49} early
in the session produced a whole-book Latin Library dump; the
file was overwritten with a placeholder stub explaining the
issue. \texttt{git clean -f
latin/letters/054bc-ad-familiares-13-49.tex} will remove the
stub before the next attempt on the year-range \textit{Fam.} 13
batch.
\end{enumerate}

\textbf{Cowork session 2 --- 20 letters drafted across four
parallel batches:}
\begin{itemize}
\item Batch 1 (spring/summer 52 BC closure, 4 letters):
\textit{Fam.} 5.18 (consolation to T. Fadius the exile),
13.2 (recommendation of C. Avianius Evander to Memmius ---
note: the launch-prompt summary mis-identified the subject,
the workers translated what is in the Latin), 13.3
(recommendation of A. Fufius to Memmius), 13.75 (to T. Titius
the legate on C. Avianius Flaccus and the Pompeian grain
commission). Metadata fix this batch: \textit{Fam.} 5.18's
\texttt{latin\_source\_url} switched from
\texttt{thelatinlibrary.com/cicero/fam5.shtml} (which dumped
the whole book on fetch) to the Perseus TEI; the bad-dump
file was overwritten by a forced re-fetch.
\item Batch 2 (Cilicia journey opening, 5 letters):
\textit{Fam.} 7.2 (the M. Marius pre-departure note with the
``little ape'' \textit{simiolus} for Bursa), 15.14 (to C. Cassius
proquaestor of Syria --- \textbf{major date correction:} from
year-precision $-0051-03-03$ to month-precision $-0051-10-15$;
the dateline is unambiguously from the camp at Aras Alexandri
in October 51 BC, post-Carrhae, with Cicero already imperator,
not the spring-of-51 letter the meta entry described), 3.2
(the cordial first letter to Appius Pulcher about the
proconsular handover), 13.47 (recommendation to L. Silius
for Egnatius of Sidicinum, date refined from $-0051-04-04$
year to $-0051-03-29$ month), 2.7 (\textbf{major date correction:}
from year-precision $-0051-04-12$ to day-precision $-0051-12-19$;
the Perseus dateline places this firmly at Pindenissus on
19 December 51 BC --- the moral-tutor letter is to an already-
installed tribune, not a tribune-elect, and Cicero is already
imperator).
\item Batch 3 (the May 51 BC Atticus 5 journey-letters,
6 letters): \textit{Fam.} 3.3 (\textbf{date correction:}
from year-precision Rome to day-precision Brundisium 22 May 51 ---
§1's internal dateline ``\textit{A. d. xi K. Iun. Brundisium
cum venissem}'' settles it); \textit{Att.} 5.8 (Brundisium,
ca. 2 June, the opening letter chronologically of Atticus
book 5 --- financial-and-libellus details, the news of the
elder Caecilia, Pomptinus's joining the march); 5.2
(Pompeii, 10 May, the journey south with the
\textit{strategema} pun); 5.3 (Trebula, 11 May, the
one-section note with Greek \textit{spoudaioteron}); 5.4
(Beneventum, 12 May, with the obstructive
\textit{numera!} obstruction-formula and two Greek
philosophical adverbs); 5.5 (Venusia, 14 May, the short
Pomptinus-and-finances note with Greek
\textit{dialogous}).
\item Batch 4 (late May / June 51 BC and the Cilician
operations, 5 letters): \textit{Att.} 5.6 (near Tarentum,
19 May, on Caesar's debt and the journey east);
\textit{Fam.} 15.4 (\textbf{date correction:} from
year-precision $-0051-05-21$ to month-precision
$-0051-12-15$ --- the great Cato letter narrates operations
through the 57-day siege of Pindenissus that concluded in
mid-December 51 BC; the Perseus dateline ``\textit{ex. a. 703
vel in. 704}'' supports late 51 / early 50 BC, conventionally
dated to early January 50 BC by Shackleton Bailey); 8.1 (the
first Caelius newsletter to Cicero, 24 May, the founding
agreement of the Caelius gossip-correspondence with the
\textit{embaeneticam facere} hapax); 3.4 (Brundisium, 5 June,
to Appius); 13.1 (Athens, late June / early July, the famous
letter to Memmius asking him not to demolish Epicurus's
\textit{parietinae} --- one Greek phrase
\textit{hypomnematismon} for ``memorandum'').
\end{itemize}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl}} (Cowork did not write the
shared jsonl directly to avoid concurrent-write contention):
\begin{itemize}
\item \textit{Fam.} 5.18: \textit{optime actum cum eo videatur
esse, qui quam levissima poena ab hac re p. discesserit} ---
\textit{discesserit} deliberately rendered ``parted from''
rather than ``departed'' so the political-exile sense reads
through without reducing to a death-metaphor.
\item \textit{Fam.} 13.2: \textit{sacrarium} rendered
``shrine-house'' (the word does double duty for private chapel
and atelier-space; worth flagging).
\item \textit{Fam.} 13.3: \textit{tam gratum mihi id erit quam
quod gratissimum} --- the deliberately-stretched superlative,
a Ciceronian courtesy-formula.
\item \textit{Fam.} 13.75: Perseus printed \texttt{me ad te
quam so saepissime scribere} --- the \textit{so} is an MS
intrusion; emended to \textit{quam saepissime}.
\item \textit{Fam.} 2.7 \S 4: \textit{tum quasi a $\dag$senatuore}
--- daggered crux; rendered ``from one who was, so to speak,
merely a senator,'' preserving the contrast with \textit{nunc
a tr. pl.}
\item \textit{Fam.} 7.2 \S 3: \textit{simiolus} (``little ape'')
--- a Plautine register choice over a smoother modern epithet.
\item \textit{Fam.} 13.47: \textit{illa nostra ceciderunt}
--- the unspecified failed venture between Cicero and Silius;
flag-not-resolve in the headnote.
\item \textit{Fam.} 15.14 \S 1: \textit{M. Fadium} (manuscripts;
some editors prefer \textit{M. Fabium}; followed Perseus).
\item \textit{Att.} 5.4: \textit{ne quid ad senatum consule!}
/ \textit{aut numera!} --- the obstructive Senate formulae
(``do not lay it before the Senate, consul!'' / ``call the
count!''), preserved as direct quotation. Numeral
\texttt{DCCC} as ``eight hundred thousand sesterces.''
\item \textit{Att.} 5.5 \S 2: \textit{HS XX et DCCC} --- the
doubled-numeral financial sum is a known crux; SB reads the
total as 820{,}000 HS.
\item \textit{Att.} 5.4 \S 1 and 5.5 \S 2: daggered cruxes
(\textit{me ille illud labat}; \textit{esse satis faciemus
satis}) preserved with obeli.
\item \textit{Att.} 5.6: \textit{de Caesaris nomine}
rendered ``Caesar's debt'' (the loan Cicero took before
departing for Cilicia).
\item \textit{Fam.} 15.4: the \textit{supplicatio} / \textit{honor
rebus bellicis} pair rendered ``thanksgiving'' / ``the honour
for things done in war'' rather than expanding to ``triumph''
(the substantive distinction matters for the later Cato vote).
\item \textit{Fam.} 8.1: \textit{embaeneticam facere} ---
hapax for running a bathing-business; rendered literally.
\item \textit{Fam.} 13.1: \textit{parietinae} (Epicurus's
``ruined walls'') --- preserved literal; the philosophical
courtesy-formula at the close is the substantive point.
\end{itemize}

\textbf{Date corrections committed to \texttt{meta/works.yaml}
during session 2 (5 entries):}
\texttt{ad-familiares-15-14}: $-0051-03-03$ year $\to$
$-0051-10-15$ month (Aras Alexandri in October, not Rome in
March; Cicero already imperator).
\texttt{ad-familiares-13-47}: $-0051-04-04$ year $\to$
$-0051-03-29$ month (Perseus dateline \textit{ex. m. Martio
a. 703}).
\texttt{ad-familiares-02-07}: $-0051-04-12$ year $\to$
$-0051-12-19$ day (Pindenissus camp \textit{a.d. xiv K. Ianuar.
a. 703}).
\texttt{ad-familiares-03-03}: $-0051-04-24$ year $\to$
$-0051-05-22$ day (Brundisium per §1's internal
\textit{A. d. xi K. Iun.} dateline).
\texttt{ad-familiares-15-04}: $-0051-05-21$ year $\to$
$-0051-12-15$ month (late 51 BC at Tarsus, post-Pindenissus,
per Perseus \textit{ex. a. 703 vel in. 704}). These corrections
expanded the chronological-gap warning from 17 to 50 pending
works dated earlier than the latest drafted; this is expected
(several letters jumped from a placeholder April 51 BC date
into late 51 / December 51 BC).

\textbf{Metadata fix this session:} \texttt{ad-familiares-05-18}
\texttt{latin\_source\_url} was pointing at the Latin Library
(which 403s and on fallback dumps the whole book \texttt{fam5.shtml});
switched to the Perseus TEI URL the rest of \textit{Fam.} 5
uses, and the bad whole-book file was overwritten by a forced
re-fetch (the script's ``already fetched, skipping'' guard
required zeroing the file first via a brief inline Python call).

\textbf{Sandbox caveats from session 2} (same as session 1):
\begin{enumerate}
\item Sandbox has no SSH access to \texttt{origin} --- pushes
and fetches all fail. Cowork in this session translated, edited
\texttt{meta/works.yaml}, ran regeneration scripts (backfill /
manifest / validate), but did \emph{not} commit. All session-2
output is untracked/modified in the working tree, awaiting an
Alexander-side commit + push via
\texttt{bash scripts/cowork\_handoff.sh "session 2: ..."}.
\item The \texttt{.git/index.lock} from session 1 is still
present in the local repo and is blocking all git writes from
the sandbox. \texttt{cowork\_handoff.sh} removes it before
staging.
\item The orphan placeholder stub
\texttt{latin/letters/054bc-ad-familiares-13-49.tex} from
session 1 also remains; \texttt{cowork\_handoff.sh} removes
it before staging.
\end{enumerate}

\textbf{Translator-notes worth logging in
\texttt{data/translator-notes.jsonl} from session 3} (Cowork
did not write the shared jsonl directly to avoid
concurrent-write contention; PM or future enrichment pass
should consolidate):
\begin{itemize}
\item \textit{Att.} 5.9 the \textit{X X et DCCC} numerals
(Tyrrell--Purser): identity of the sum (sestertia? denarii?)
disputed; rendered ``twenty thousand and eight hundred''.
\item \textit{Att.} 5.10 \S 5 \textit{sursum deorsum}
daggered crux preserved with obeli; the joke about
``philosophy in Athens going much up-and-down'' is
intelligible despite the corruption. The four Greek phrases
\textit{erdoi tis} (\textit{Margites} tag), \textit{dysexeilēta},
\textit{bathytēs}, \textit{meletē} all worth a
greek-phrases.json entry.
\item \textit{Att.} 5.11 \S\S 6, 7 two daggered cruxes
(\textit{in praefectis excusatio iis}; \textit{nomanaria});
the truncated proverb \textit{hoiaper hē...} restored
elliptically. Six Greek phrases.
\item \textit{Att.} 5.12 \textit{akra Gyreōn} = Homer
\textit{Od.} 4.500 (allusions sidecar candidate).
\item \textit{Att.} 5.13 the ``five hundred and sixtieth day
after the battle of Bovillae'' --- Cicero's private
date-clock from the Clodius killing (18 Jan 52 BC); worth a
crossref/glossary entry on Cicero's private calendar of the
year. \textit{Domesticus scrupulus} preserved as opaque per
Cicero's own discretion (the Tullia-marriage worry).
\item \textit{Att.} 5.15 \S 2 \textit{clitellae bovi sunt
impositae; plane non est nostrum onus} --- quoted iambic
proverb; preserved as flagged metrical quotation in the
headnote. \textit{versura} (rolling over a debt) and
\textit{tarde tibi redditu iri} daggered crux --- glossary
candidates.
\item \textit{Att.} 5.18 \S 1 \textit{inter caesa et porrecta}
--- sacrificial proverb, the slaying-and-laying-out interval;
kept literal per STYLE.md. \S 4 \textit{exhibeo pupillum}
legal term for ``producing one's ward in court'' --- study-mode
glossary candidate.
\item \textit{Att.} 5.19 the corrupt closing tag
\textit{†iam Romae†} preserved with daggers.
\item \textit{Att.} 5.20 the Perseus text skips \S 5 (a
manuscript-tradition gap, not editorial); the parallel JSON
preserves the gap. \S 4 \textit{loreolam in mustaceo
quaerere} (Bibulus ``looking for his little laurel in a
baker's tart'') --- Ciceronian one-liner, kept literal for
the bridal-cake-laurel image. \S 6 \textit{recte
πεφυσίωμαι} (``rightly puffed up'') --- half-ironic
Greek self-deflation. \S 9 \textit{Phemio quaeritur κέρας}
opaque musical-instrument reference. Seven Greek phrases
across the letter for the greek-phrases.json backfill.
\item \textit{Fam.} 3.8 \S 8 \textit{med esse acerbum sibi,
uti sim dulcis mihi} --- almost certainly Terence
\textit{Adelphoe} Demea-line (allusion sidecar candidate).
\S 5 \textit{Brundisi neque ad praefectum fabrum Corcyrae}
--- dense syntax preserved. The parodic anaphora
\textit{disputabant, ego contra disserebam; dicebant, ego
negabam} preserved in English.
\item \textit{Fam.} 8.3 \S 1 daggered \textit{† sed tanti
sed me hercules †} preserved; the \textit{non inepto}
self-reflexive joke in Caelius's mimicry of Cicero noted.
\item \textit{Fam.} 8.4 \S 1 \textit{Lentuli cruris repulsi
vultum} --- Caelius's name-pun on Lentulus \textit{Crus}
(``leg''); scholar-mode note candidate.
\item \textit{Fam.} 8.8 the senate-debate text (\S\S 5--8)
set off as a transcribed senatus consultum at formal
register, distinct from Caelius's narrative voice. Two
daggered cruxes in \S\S 1--2 rendered as
``\texttt{[textual crux]}''. The Pompey ``stick'' line in
\S 9 deserves a translator-note.
\item \textit{Fam.} 8.9 the daggered \textit{Curionem
prorsus Curionem} (\S 1) and the daggered Pompey-Caesar
sentence (\S 5) preserved with obeli. \textit{columnariis}
(``loiterers under the columns of the Forum'') kept literal.
\item \textit{Fam.} 8.10 \S 2 \textit{velificatus aliquoi}
(``to spread sails for someone,'' a nautical metaphor for
political toadying) --- glossary candidate. \S 3 daggered
\textit{aut sit aut non erit istic bellum aut} restored as
``either there is, or will be, no war out there.''
\item \textit{Fam.} 2.10 \S 2 the self-quotation
\textit{hicine est ille, qui urbem? quem senatus?...}
preserved with ellipsis; the consulship-saviour self-echo.
\item \textit{Fam.} 15.1 the official senatorial salutation
\textit{M. TVLLIVS M. F. CICERO PROCOS. S. D. COS. PR. TR.
PL. SENATVI} preserved verbatim, and the \textit{S. v. v.
b. e. e. q. v.} formula expanded inline as ``If you are in
good health, it is well; I myself am in good health.''
The closing \textit{utinam saluti nostrae consulere
possimus! dignitati certe consulemus} preserved the
\textit{consulere/consulemus} ring-composition.
\item \textit{Fam.} 15.2 the unusual MS forms \textit{Artuasdes}
(Artavasdes), \textit{Eusebes et Philorhomaeum} (titles of
Ariobarzanes) noted. Same opening formula expansion as 15.1.
\item \textit{Fam.} 15.7 the unusual salutation
\textit{S. N.} (where one expects \textit{S. D.}) preserved
verbatim per the project rule on salutations.
\item \textit{Fam.} 15.10 the salutation form
\textit{M. CICERO IMP. S. D. C. MARCELLO C. R COS.} where
\textit{C. R} appears to be a corruption of \textit{C. F.}
(``C. filio'') preserved as-is. The Perseus dateline
\textit{Tarsi vel ex. a. 703 vel in. 704} is genuinely
indeterminate between late 51 and early 50 BC; the
placeholder $-0051-11-27$ is one defensible point inside
the window and was kept.
\end{itemize}

\textbf{Sandbox caveats from session 3} (same as sessions 1
and 2):
\begin{enumerate}
\item Sandbox has no SSH access to \texttt{origin}. Cowork
translated, edited \texttt{meta/works.yaml}, ran regeneration
scripts, but did \emph{not} commit. All session-3 output is
untracked/modified in the working tree, awaiting an
Alexander-side commit + push via
\texttt{bash scripts/cowork\_handoff.sh "session 3: ..."}.
\item The \texttt{.git/index.lock} from earlier sessions is
still present and is blocking all git writes from the
sandbox. \texttt{cowork\_handoff.sh} removes it before
staging.
\item The orphan placeholder stub
\texttt{latin/letters/054bc-ad-familiares-13-49.tex} from
session 1 also remains; \texttt{cowork\_handoff.sh} removes
it before staging.
\end{enumerate}

\textbf{Suggested next translation batch} (when session 3 is
landed via \texttt{cowork\_handoff.sh "session 3: ..."} and
the next Cowork session opens):
\begin{itemize}
\item Slice E (the 50 BC continuation, opening on the
\textit{Att.} 5/6 boundary --- the entire Cilician
proconsulship turnover and the long march back through
Asia and Greece, dense with day-precision dates):
\texttt{ad-familiares-14-05} (to Terentia, ca. mid-Jan 50,
the brief illness-greeting from Laodicea),
the \textit{Fam.} 13 propraetor-cluster letters
(\texttt{-13-54}, \texttt{-13-58}, \texttt{-13-59},
\texttt{-13-63}, \texttt{-13-65} all dated to early Feb 50
during the Laodicea \textit{conventus} --- these may need
metadata cleanup since the placeholder dates may be
year-precision; check Perseus datelines),
\texttt{ad-familiares-03-07} and \texttt{-03-09} (the
continuing Appius correspondence in early 50, with the
news of Appius's prosecution by Dolabella),
\texttt{ad-familiares-02-11} through \texttt{-02-15} (the
Caelius newsletters across the 50 BC year, and Cicero's
responses),
\texttt{ad-atticum-06-01} through \texttt{-06-09} (the
Atticus 6 sequence, from the Feb 50 Laodicea letters with
Brutus's Salaminian loan affair through the summer march
back and the late-50 letters from Athens on Caesar's
imminent crossing),
\texttt{ad-familiares-08-11, -08-12, -08-13, -08-14}
(continued Caelius newsletters into late 50 BC),
\texttt{ad-familiares-15-05, -15-06} (Cato's reply to
\textit{Fam.} 15.4 on the supplicatio, and Cicero's
response). About 30--40 letters, easily parallelisable.
The Cato reply (15.5) and Cicero's response (15.6) are
the substantive heart of the supplicatio thread that
opened in session 2 with 15.4.
\item Slice B' (the year-range \textit{Fam.} 13 recommendation
letters that were on the previous suggested-batch hold list):
\texttt{ad-familiares-13-49} (47 BC after the
session-0 \texttt{speech\_index} correction --- needs
re-fetching now that the entry is fixed; the orphan
placeholder stub from session 1 should be removed by
\texttt{cowork\_handoff.sh}),
\texttt{-13-73}, \texttt{-13-74}, \texttt{-13-76}.
\item Slice B' (the year-range \textit{Fam.} 13 recommendation
letters that were on the previous suggested-batch hold list):
\texttt{ad-familiares-13-49} (47 BC after the
session-0 \texttt{speech\_index} correction --- needs
re-fetching now that the entry is fixed),
\texttt{-13-73}, \texttt{-13-74}, \texttt{-13-76}.
\item Slice C (the year-precision speeches and rhetoric ---
substantial works, dispatch one per session not in parallel):
\texttt{pro-milone} (52 BC, the next chronologically pending
speech, blocking the chronology pointer at 52 BC),
\texttt{partitiones-oratoriae}, \texttt{pro-plancio},
\texttt{pro-rabirio-postumo}, \texttt{pro-scauro}.
\end{itemize>

\textbf{Suggested polishing-pass batch} (also dispatchable in
parallel; doesn't conflict with translation):
\begin{itemize}
\item Enrich the 472 entity stubs in \texttt{data/entities.json}
(those with \texttt{summary: "(stub --- to be enriched)"}).
Stubs were auto-generated from sidecar references in earlier
sessions; replace placeholder summaries with real entries
(canonical name, aliases, summary, external IDs where known
\textemdash{} DPRR for people, Pleiades for places, Wikidata for
either). Walk through systematically.
\item Backfill judgment-heavy sidecars on the 161 already-drafted
works that don't yet have entity-mention or glossary files.
Pro Quinctio is the worked example for what "complete" looks like.
\end{itemize}

\textbf{Multi-surface progress (all on \texttt{main}):} Tier 1
hyperlinked PDF shipped as \texttt{build/output/cicero-v0.3-scholar.pdf}
(Greek tooltips pending gloss data; entity links and
cross-references live). Tier 2 web edition Phases 2.1 (skeleton),
2.2 (per-work pages with English-default + Latin-toggle), 2.3
(chronology timeline with life events), 2.4 (entity glossary
index), 2.6 (letter-network table), 2.8a (Greek catalogue), and
2.11 (agent discoverability \textemdash{} \texttt{llms.txt},
sitemap, per-work JSON mirrors) all shipped. Live at
\url{https://tastydrinks.github.io/cicero-by-claude/}. Pending
Tier 2 phases: 2.5 (hover prosopography), 2.7 (full-text search),
2.9 (apparatus profile toggle), 2.10 (visual polish + mobile),
2.12 (EPUB export).

\textbf{Workflow:}
\begin{enumerate}
\item Cowork reads this section + \texttt{PLAN.md} at session start.
\item Plans next batch (translation + polishing + Tier 2 phase).
\item Dispatches parallel sub-agents with explicit work-id lists or
infrastructure-phase scope (per CLAUDE.md \S{} ``Parallel sessions'').
\item Waits for completion, runs
\texttt{bash scripts/finalize\_parallel\_batch.py} to merge work
to \texttt{main}, regenerate derived files, and validate.
\item Updates this section so the next session inherits a clean
pointer.
\end{enumerate}

\textbf{The previous resume notes below remain accurate} for
chronological sweep work; the only thing that has changed is the
chronology pointer has moved forward.

A parallel-assignment session drafted six undated
recommendation letters from \textit{Ad Familiares} 13 ---
the cluster Cicero sent during his Cilician proconsulship
of 51--50 BC to the propraetors of the neighbouring
provinces, written about the same season as \textit{Fam.}
13.53. To Q. Minucius Thermus, propraetor of Asia: 13.55
(the case of Cicero's legate M. Anneius against the people
of Sardis) and 13.56 (the M. Cluvius of Puteoli debt
collection across Mylasa, Alabanda, Heraclea Salbace,
Bargylia, Caunus --- the letter that carries four Greek
technical terms in beta-code: \textit{Mulaseis},
\textit{Alabandeis}, \textit{ekdikoi},
\textit{hupothekas}). To P. Silius, propraetor of Bithynia:
13.61 (the eight-million-sesterce debt of Nicaea to the
Pinnius estate, on which Cicero was guardian and second
heir to the boy), 13.62 (the brief intimate letter
combining thanks for Atilius's case with the request that
brother Quintus be received as Cicero would be ---
\textit{te in meo aere esse}, the account-book idiom), 13.64
(Tiberius Claudius Nero's debut in provincial diplomacy:
Pausanias of Alabanda, the city of Nysa as a hereditary
Claudian client, and Servilius Strabo --- with the
recurring \textit{magnum theatrum habet ista provincia}
figure for the foreign command as the public stage), and
13.65 (P. Terentius Hispo and the \textit{societas
scripturae}, the publican company on the pasturage-tax of
the Asian provinces).

The metadata required correction: all six entries had
pointed at the 403'd Latin Library and lacked
\textit{speech\_index}. They are in fact in Perseus's TEI
corpus; the entries now point there and carry the right
\textit{book:13,letter:N} indices. Thirteen new person
entities (Anneius, Thermus, Silius, Cluvius, Euthydemus,
Philocles, Pinnius pater + filius, Atilius, Ti. Claudius
Nero, Pausanias, Servilius Strabo, Hispo) and eight new
place entities (Sardis, Mylasa, Alabanda, Heraclea Salbace,
Bargylia, Caunus, Nicaea, Nysa) registered. Four entries
added to greek-phrases.json; six to letter-network.json;
one to translator-notes.jsonl.

The previous resume pointer below remains the right one
for chronological sweep work going forward.

A parallel-assignment session drafted three works in
continuous mode --- the two Marcellus letters of \textit{Ad
Familiares} 15 (15.8 to C. Marcellus consul-elect for 50,
15.9 to M. Marcellus consul of 51, both written from the
Cilician road in late summer 51 BC and carrying placeholder
54 BC dates per the book-level metadata) --- and then, in
the same session, the long task of \textit{De Re Publica},
the six-book dialogue of 54--51 BC. The translation follows
the Perseus edition (palimpsest text of books 1--3 plus
fragments of books 4--6 in standard Powell / Ziegler
numbering). The body covers the preface and Scipio's
constitutional analysis (book 1), the historical case study
of the Roman state through the seven kings and the early
Republic (book 2), the Carneades / Laelius debate on justice
with the famous \textit{vera lex} formulation (book 3), the
fragmentary remains on civic education and the
\textit{rector rei publicae} (books 4--5), and book 6 ---
the closing fragments and the Somnium Scipionis (6.9--29)
preserved through Macrobius. The de-re-publica entry adds
sidecars at section grain (entities-mentions, glossary,
allusions, crossrefs) and the structural-backfill script has
regenerated the parallel corpus and the corpus-wide
greek-phrases / letter-network files.

The previous resume pointer below remains the right one for
chronological sweep work going forward.

A parallel-assignment session drafted ten letters scattered
across the long pendents in the middle of 56 BC and the
spring of 55 BC: the recommendation letters \textit{Fam.}
13.51 (P. Caesius, undated placeholder), 13.6 (Q. Valerius
Orca, propraetor of Africa, late 56), and \textit{Fam.} 5.3
(Q. Metellus Nepos to Cicero from Hither Spain, late 56);
\textit{Fam.} 7.3 (M. Marius --- the post-Pharsalus
retrospective of summer 46 BC, sitting in the manifest as a
56 BC placeholder pending the date correction; \textit{vir
ille summus nullus imperator fuit}); \textit{Fam.} 1.8 (the
last Lentulus Spinther letter of January 55, the open
acknowledgement that politics is now Pompey's and study is
the consolation); \textit{Fam.} 16.13 (Cicero to Tiro from
Cumae, 10 April --- the first surviving Tiro letter, the
manifest 55 BC year likely to need correction to 53 BC);
\textit{Q. fr.} 2.7 (mid-Feb 55, the night call on Pompey,
the consul-Crassus-from-Senate-to-house escort, the bribery
SC); and three Cumae-bay Atticus letters of late April /
early May 55 (\textit{Att.} 4.9 from Naples on Pompey's
\textit{Hispaniam iactans}; \textit{Att.} 4.10 from Cumae
with the famous chair-under-Aristotle preference for
Atticus's study over the consuls' sella curulis;
\textit{Att.} 4.11 with the gladiator joke and the Greek
\textit{ouden} on news from Rome). The corpus-wide sidecars
gained 31 new entities (the post-Pharsalus retrospective
brought in Lentulus Crus, C. Marcellus, and Juba; the Tiro
letter brought in Tiro and Menander; the Cumae letters
brought in Faustus, Aristotle, Philotimus, Dionysius, the
two Demetrii, M. Valerius Messalla Rufus, L. Papirius Paetus,
and the cluster of bay-of-Naples places).

The previous resume pointer --- the chronology is clean
through mid-March 56 BC --- still stands for chronological
sweep work. The fifth continuous session drafted the early-56
BC dense political sequence of letters and \textit{Pro
Sestio}: \textit{Fam.} 1.1 (13 Jan), 1.3 (mid-Jan), 1.2
(17 Jan), 1.4 (~18 Jan), \textit{Q. fr.} 2.2 (19 Jan),
\textit{Att.} 4.4 (30 Jan), \textit{Fam.} 1.5a (~5 Feb),
1.5b (~10 Feb), \textit{Q. fr.} 2.3 (12--15 Feb),
\textit{Q. fr.} 2.4 (mid-March, after the 11 March Sestius
acquittal), and \textit{Pro Sestio} itself (March 56, the
great political defence with the \textit{cum dignitate
otium} digression at \textsection 96--143 and the
optimate-front high-water mark of the year).
This session also did the metadata cleanup: Fam. 1.5 split
into 1.5a + 1.5b per Perseus's manuscript division (the
previous single entry had the wrong Latin Library URL and
no speech\_index); Att. 4.4A and 4.8A added (present in
Perseus, missing from the manifest); placeholder dates
corrected against the Perseus datelines for Q.fr. 2.4
(year-precision Jan placeholder $\to$ March), Fam. 1.6
(November placeholder $\to$ March), Q.fr. 2.5
(year-precision Feb $\to$ April 8 day), Q.fr. 2.6 (March
placeholder $\to$ May), Att. 4.5 (year-precision Oct $\to$
April month).

As of the sixth session the four mid-56 BC speeches that
follow Pro Sestio (\textit{De Provinciis Consularibus},
\textit{De Haruspicum Responsis}, \textit{Pro Balbo}) are
drafted, along with \textit{Ad Familiares 5.12} to Lucceius.

A second parallel-assignment session of the same period
drafted the six mid-55 BC works the launch prompt named:
\textit{Q. fr.} 2.8 (May 55, the gentle ``you are not
interrupting me'' to Quintus, with the Asician-litter
recollection of M. Marius); \textit{Att.} 4.12 (May 55,
single-section dinner-arranger with the joke about playing
a trick on the senate's decree by dining at the Crassipes
gardens); \textit{De Oratore} (all 862 sections across three
books --- the longest single work drafted in any session of
this project; the mature dialogue replacing the boyish
\textit{De Inventione}, with the great Tusculan plane-tree
frame, the elegy for Crassus opening Book 3, and the
Caesar-Strabo humour digression at 2.217--289); \textit{In
Pisonem} (all 118 sections including the 19 fragments --- the
most violent invective in the corpus, with the
me-vs-tibi consulship parallel of \textsection 2--7, the
Macedonian-disgrace catalogue, and the Philodemus and
\textit{cedant arma togae} centre); \textit{Fam.} 13.40 to
Q. Ancharius (Piso's successor in Macedonia); and \textit{Fam.}
7.1 to M. Marius on Pompey's dedication-games --- the elephants,
Aesopus's failed \textit{si sciens fallo}, and \textit{humaniter
vivere}. Sidecars emitted comprehensively for all six. About 100
new entities added to entities.json --- the De Oratore cast
(L. Crassus, M. Antonius, Scaevola the Augur, Cotta, Sulpicius,
Catulus, Caesar Strabo) and the Greek philosophers (Plato,
Aristotle, Theophrastus, Socrates, Demosthenes, Carneades,
Charmadas, Thucydides, Herodotus, Theopompus, Ephorus, Xenophon,
Hippias, Pisistratus, Pericles, Anaxagoras, Aeschines, Hannibal,
Marius, Cato the Elder, Scipio Aemilianus, Simonides), the In
Pisonem cast (L. Piso, A. Gabinius, Antonius Hybrida, Lentulus
Spinther, M. Lucullus, the elder Catulus, Torquatus, Cn. Dolabella,
C. Curio, M. Marcellus, M. Regulus, P. Rutilius Rufus, L. Opimius,
Q. Metellus Numidicus, Gellius, T. Albucius, C. Cotta cos. 75,
Sex. Clodius, C. Piso Frugi, Philodemus, King Cotys), and laws
and texts (Twelve Tables, lex Aelia Fufia, lex Iulia de
repetundis, lex Pompeia iudiciaria, ius civile, Plato's Phaedrus,
Accius's Clytaemnestra, Equus Troianus). The build-system
addition: a \texttt{\textbackslash ciceroBook\{N\}} command in
build/preamble.tex for multi-book works, used to mark Books 2
and 3 within \textit{De Oratore}; ready for \textit{De Re Publica}
and \textit{De Legibus}.
The next chronological items, then, are the early-56 BC
items the assigned-list session jumped over (which an
earlier session had not yet picked up): \textbf{\textit{In
Vatinium}} (early March 56, the cross-examination of
Vatinius from the Sestius trial that survives as a separate
work, if not already drafted by the parallel-session work
on the early-56 sequence), and the parallel post-Luca
items \textit{Fam.} 1.6 (March 56), \textit{Att.} 4.4A
(April/May 56, the famous library letter from Antium with
Tyrannio), \textit{Pro Caelio} (4 April 56, day-precision:
the Clodia speech, if not already drafted), \textit{Q.
fr.} 2.5 (8 April 56 from Anagnia), \textit{Att.} 4.5--4.8
(April/May 56), \textit{Q. fr.} 2.6 (May 56), \textit{Fam.}
1.7 (July 56), \textit{Att.} 4.8A (autumn 56), then
\textit{In Pisonem} (Aug/Sept 55 BC), \textit{Pro Plancio},
\textit{Pro Rabirio Postumo}, and \textit{Pro Milone},
with \textit{De Oratore} (55 BC), \textit{De Re Publica}
(54 BC), and \textit{De Legibus} (52 BC) interleaved.

Forward from the exile correspondence the chronology runs:

- **late 59 BC** --- \textit{Att.} 2.18, 2.19, 2.21--2.25
  (the Vettius affair, the political mood as Caesar's
  consular year closes, Cicero's growing fear of Clodius's
  coming tribunate); \textit{Att.} 3.1 begins the exile
  letters of 58 BC.
- **58 BC} --- the exile correspondence: \textit{Att.} 3 and
  the early \textit{Q. fr.} from Thessalonica and Dyrrachium.
- **57--52 BC** --- the post-exile speeches \textit{Pro
  Sestio}, \textit{In Vatinium}, \textit{De Provinciis
  Consularibus}, \textit{Pro Caelio}, \textit{De Domo Sua},
  \textit{De Haruspicum Responso}, \textit{Pro Plancio},
  \textit{Pro Rabirio Postumo}, \textit{Pro Milone}, with
  \textit{De Oratore} (55 BC), \textit{De Re Publica} (54 BC),
  \textit{De Legibus} (52 BC) and the great triple letter
  book of 54 BC interleaved.
- **51--47 BC** --- the Cilician proconsulship and the civil
  war, with \textit{Ad Familiares}, \textit{Ad Atticum}, and
  \textit{Ad Quintum Fratrem} dense throughout.
- **46--43 BC** --- the philosophical torrent
  (\textit{Brutus}, \textit{Orator}, \textit{Academica},
  \textit{De Finibus}, \textit{Tusculanae}, \textit{De Natura
  Deorum}, \textit{De Divinatione}, \textit{De Senectute},
  \textit{De Amicitia}, \textit{De Officiis}), the late
  forensic speeches (\textit{Pro Marcello}, \textit{Pro
  Ligario}, \textit{Pro Rege Deiotaro}), the 14
  \textit{Philippics}, and the dense final-year letters of
  44--43 BC, closing on \textit{Ad M. Brutum} and Cicero's
  death at Formiae in December 43 BC.

Run \texttt{bash scripts/session\_start.sh} at the start of each
session: it fast-forwards your session branch to
\texttt{origin/main}, runs the validator, and prints the
chronologically next pending work.

## Generated index

A complete chronological table of contents lives in `MANIFEST.md` and is
regenerated by `scripts/build_manifest.py` from `meta/works.yaml`.
