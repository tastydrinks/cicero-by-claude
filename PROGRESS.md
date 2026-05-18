# Progress

This file tracks the state of the translation effort. Auto-generated entries
are derived from `meta/works.yaml`; the prose summary at the top is hand-edited
as milestones are reached.

## Status summary

- **Drafted**: 160 works end-to-end across all categories.
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
