# Progress

This file tracks the state of the translation effort. Auto-generated entries
are derived from `meta/works.yaml`; the prose summary at the top is hand-edited
as milestones are reached.

## Status summary

- **Drafted**: 153 works end-to-end across all categories.
- **Drafted**: 147 works end-to-end across all categories.
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

## Where to resume now

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
