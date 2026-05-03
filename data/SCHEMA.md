# data/ — schemas for the structured corpus sidecars

The canonical artifact of *cicero-by-claude* is the bound English volume.
Underneath that, the project also emits a set of structured **sidecar
files** that capture information a single reader of the bound volume can't
easily extract on their own — but a translator reading every word of the
corpus in order can produce as a side effect.

The sidecars are intended for three audiences:

1. **Future readers of the volume** who want apparatus the basic edition
   omits — a glossary of named entities, a list of Cicero's Greek phrases,
   a letter-network appendix, etc. These are surfaced via the build's
   `--profile` flag (see `build/PROFILES.md`).
2. **Future agents and ML systems** that want a clean parallel
   classical-Latin/English corpus, named-entity tagged, with allusion and
   cross-reference signals — a kind of resource that does not currently
   exist for any major classical author.
3. **Scholars, hobbyists, and Alexander himself** who want to interrogate
   the corpus structurally rather than just read it.

This document is the binding reference for the schemas. When a new artifact
type is added, its schema is documented here first.

---

## Conventions

- All sidecar files are JSON (corpus-wide files) or JSONL
  (`translator-notes.jsonl`).
- Encoding is UTF-8.
- Every file carries `schema_version: 1` at its top level. Bump when the
  schema changes incompatibly; add migration code in
  `scripts/validate.py`.
- Per-work sidecar files follow the same path convention as
  `english/`, `latin/`, `headnotes/`:
  `data/<artifact>/<category>/<NNN>(bc|ad)-<id>.json`.
  E.g. `data/parallel/speeches/081bc-pro-quinctio.json`.
- Per-work `id` always matches the `id` field in `meta/works.yaml`. The
  validator enforces this.
- Section references use a `loc` string keyed to the standard scholarly
  section number, optionally suffixed with a sentence index:
  `"5"` (whole section 5), `"5.2"` (sentence 2 of section 5),
  `"5.2-5.4"` (range).
- Entity IDs are kebab-case slugs prefixed with type:
  `person:sex-naevius`, `place:forum-romanum`, `office:consul`,
  `law:lex-plautia`. The canonical entity list lives in `data/entities.json`.

## Determinism

Sidecar files are emitted in a stable order so diffs are readable:

- Per-work sidecars: segments / mentions / refs in document order.
- Corpus-wide sidecars (`greek-phrases.json`, `letter-network.json`,
  `entities.json`): sort key noted per artifact below.

## File map

| Artifact | Path | Scope |
|---|---|---|
| Sentence-aligned parallel corpus | `data/parallel/<category>/<id>.json` | per work |
| Greek-phrase catalogue | `data/greek-phrases.json` | corpus-wide |
| Letter-network metadata | `data/letter-network.json` | corpus-wide (letters only) |
| Entity registry | `data/entities.json` | corpus-wide |
| Entity mentions | `data/entities-mentions/<category>/<id>.json` | per work |
| Cross-references | `data/crossrefs/<category>/<id>.json` | per work |
| Allusions | `data/allusions/<category>/<id>.json` | per work |
| Glossary notes (realia) | `data/glossary/<category>/<id>.json` | per work |
| Translator's notes log | `data/translator-notes.jsonl` | corpus-wide append-only |

---

## 1. Sentence-aligned parallel corpus

**Path**: `data/parallel/<category>/<id>.json`

**Purpose**: clean parallel Latin/English data, sentence- or
section-aligned. The single largest contemporary single-translator
parallel corpus for any classical Latin author.

**Schema**:

```json
{
  "schema_version": 1,
  "id": "pro-quinctio",
  "category": "speeches",
  "title_latin": "Pro Quinctio",
  "title_english": "For Publius Quinctius",
  "date": "-0081-07-01",
  "source_latin": "Perseus phi0474.phi001 (Clark, OCT 1909)",
  "translator": "Claude (Anthropic), via cicero-by-claude",
  "license": "CC BY-NC-SA 4.0",
  "alignment_grain": "sentence",
  "segments": [
    {
      "loc": "1.1",
      "section": 1,
      "lat": "quae res in civitate duae plurimum possunt …",
      "eng": "The two things that count for most in our state …",
      "notes": null
    },
    {
      "loc": "1.2",
      "section": 1,
      "lat": "eloquentia Q. Hortensi ne me in dicendo impediat …",
      "eng": "That the eloquence of Quintus Hortensius will hinder me …",
      "notes": null
    }
  ]
}
```

**Field rules**:

- `alignment_grain`: `"sentence"` or `"section"`. Prefer sentence-level
  where boundaries are clear in the Latin (most prose). Fall back to
  section-level when sentence boundaries are ambiguous (e.g. heavily
  fragmented works).
- `loc`: `"<section>.<sentence>"` for sentence grain, `"<section>"` for
  section grain. Sentence numbers reset per section, start at 1.
- `lat` / `eng`: trimmed plain text. LaTeX macros are stripped — readers
  of this corpus should see the prose, not the typesetting.
- `notes`: optional free-form string. Use sparingly for things like
  "Latin lacuna here," "English contracts a doublet."
- Backfill from drafted works produces section-grain segments only; a
  later refinement pass can split to sentence-level.

**Order**: segments in document order.

---

## 2. Greek-phrase catalogue

**Path**: `data/greek-phrases.json`

**Purpose**: every Greek phrase Cicero deploys, with Cicero's surrounding
context and (where identifiable) the source he is quoting. No standalone
catalogue of Cicero's Greek exists; this corpus is small (a few hundred
entries) but useful and otherwise inaccessible.

**Schema**:

```json
{
  "schema_version": 1,
  "entries": [
    {
      "id": "gr-0001",
      "work": "ad-atticum-01-19",
      "loc": "10",
      "greek_original": "πολίτευμα",
      "transliteration": "politeuma",
      "english_gloss": "political programme",
      "context": "Cicero on his consular politeuma",
      "suspected_source": null,
      "source_certainty": "unknown",
      "register": "technical",
      "notes": null
    }
  ]
}
```

**Field rules**:

- `id`: `gr-NNNN` zero-padded, monotonic, never reused.
- `work`: matches a `meta/works.yaml` `id`.
- `loc`: section reference into the work.
- `greek_original`: the Greek as Perseus carries it. May be empty if Perseus
  carries only the Latin transliteration.
- `transliteration`: ASCII transliteration (Beta-code or simple Latin).
- `english_gloss`: short literal English meaning.
- `context`: ≤ 1 sentence describing why Cicero reaches for the Greek here.
- `suspected_source`: `null` if unknown; else short reference like
  `"Homer, Iliad 9.319"` or `"Plato, Republic 517"`.
- `source_certainty`: one of `"high"`, `"medium"`, `"low"`, `"unknown"`.
- `register`: one of `"quotation"`, `"technical"`, `"colloquial"`,
  `"jocular"`, `"euphemistic"`, `"in-joke"`. Multiple may apply; pick the
  dominant one.

**Order**: entries sorted by `(work_chronological_date, loc)`.

---

## 3. Letter-network metadata

**Path**: `data/letter-network.json`

**Purpose**: graph-shaped data on Cicero's correspondence — sender,
recipient, place, date, topics, mood. Derived initially from
`meta/works.yaml` and from the Latin file dateline, then enriched
during translation.

**Schema**:

```json
{
  "schema_version": 1,
  "letters": [
    {
      "id": "ad-atticum-03-15",
      "sender": "M. Tullius Cicero",
      "sender_id": "person:cicero",
      "recipient": "T. Pomponius Atticus",
      "recipient_id": "person:atticus",
      "place_written": "Thessalonica",
      "place_written_id": "place:thessalonica",
      "place_received": null,
      "place_received_id": null,
      "date": "-0058-08-19",
      "date_precision": "day",
      "topics": ["exile", "self-reproach", "atticus's-silence"],
      "mood": "anguished",
      "length_sections": 8,
      "carries_greek": true
    }
  ]
}
```

**Field rules**:

- `topics`: short kebab-case tags. A controlled vocabulary will emerge
  organically; keep it minimal at first. Free additions are fine; the
  validator does not enforce a closed set.
- `mood`: one of `"businesslike"`, `"warm"`, `"anguished"`, `"angry"`,
  `"jocular"`, `"hurried"`, `"formal"`, `"intimate"`, `"resigned"`,
  `"triumphant"`, `"anxious"`, `"despondent"`, `"affectionate"`. Add
  to this list as needed.
- `place_received`: usually unknown for Cicero's letters; leave `null`
  unless the Latin or the editorial tradition is explicit.
- `length_sections`: integer count, derived from the Latin file.
- `carries_greek`: true if any Greek phrase from this letter is in
  `greek-phrases.json`.

**Order**: letters sorted by `(date, id)`.

---

## 4. Entity registry

**Path**: `data/entities.json`

**Purpose**: canonical list of every distinct person, place, office,
institution, law, festival, etc. mentioned in the corpus. Per-work
mention files reference these by `id` to avoid duplication.

**Schema**:

```json
{
  "schema_version": 1,
  "entities": [
    {
      "id": "person:cicero",
      "type": "person",
      "canonical_name": "Marcus Tullius Cicero",
      "short_name": "Cicero",
      "aliases": ["M. Cicero", "Tully"],
      "external_ids": {
        "dprr": "TulliusM.f.M.n.1529",
        "wikidata": "Q1541"
      },
      "summary": "The orator, statesman, and philosopher; author of the corpus.",
      "first_appearance": "pro-quinctio",
      "categories": ["self"]
    },
    {
      "id": "place:forum-romanum",
      "type": "place",
      "canonical_name": "Forum Romanum",
      "short_name": "the Forum",
      "aliases": ["the Forum"],
      "external_ids": {
        "pleiades": "423025"
      },
      "summary": "The civic and judicial heart of the city of Rome.",
      "first_appearance": "pro-quinctio",
      "categories": ["rome", "civic-space"]
    }
  ]
}
```

**Entity types**:

- `person` — historical individual.
- `place` — toponym, region, or building.
- `office` — magistracy or institutional role (consul, tribune, aedile).
- `institution` — body or assembly (Senate, comitia, college of pontiffs).
- `law` — named statute.
- `event` — datable historical event (the Catilinarian conspiracy, the
  battle of Pharsalus).
- `festival` — religious or civic festival.
- `unit` — military unit by name (Legio X).
- `god` — divinity or personification.
- `text` — a referenced literary or legal text by another author.

**Field rules**:

- `id`: `"<type>:<slug>"`, slug is kebab-case.
- `external_ids`: opportunistic. Common keys: `dprr` (Digital Prosopography
  of the Roman Republic), `pleiades` (gazetteer), `wikidata`, `loeb`,
  `ocd5` (Oxford Classical Dictionary 5e). All optional; populate when
  known, leave unset when not.
- `summary`: ≤ 2 sentences. This is the text that feeds the backmatter
  glossary in study/scholar editions.
- `first_appearance`: the work in which this entity is first tagged.
- `categories`: free-form tags for grouping in the glossary
  (e.g. `["family"]`, `["political-enemy"]`, `["literary"]`).

**Order**: entities sorted by `(type, id)`.

---

## 5. Entity mentions

**Path**: `data/entities-mentions/<category>/<id>.json`

**Purpose**: every entity occurrence in a work, with its surface form and
section. Drives the index and the glossary.

**Schema**:

```json
{
  "schema_version": 1,
  "id": "pro-quinctio",
  "mentions": [
    {
      "loc": "1",
      "surface": "Q. Hortensi",
      "entity_id": "person:hortensius",
      "in": "lat"
    },
    {
      "loc": "1",
      "surface": "Quintus Hortensius",
      "entity_id": "person:hortensius",
      "in": "eng"
    }
  ]
}
```

**Field rules**:

- `surface`: the literal text as it appears in the source.
- `in`: `"lat"`, `"eng"`, or `"both"`. Prefer `"both"` when surface forms
  are aligned by translation; emit two entries with `"lat"`/`"eng"` when
  Latin and English render the entity differently (almost always the case).
- Mentions for the same entity in the same `loc` may appear multiple times
  if the surface form varies; otherwise emit one per surface-form change.

**Order**: by document order (`loc` ascending, language pair: lat then
eng within a `loc`).

---

## 6. Cross-references

**Path**: `data/crossrefs/<category>/<id>.json`

**Purpose**: when Cicero refers (explicitly or implicitly) to another
work in his own corpus, or to one of his own earlier passages within the
same work, capture it.

**Schema**:

```json
{
  "schema_version": 1,
  "id": "de-officiis",
  "refs": [
    {
      "from_loc": "1.34",
      "to_work": "de-re-publica",
      "to_loc": "3",
      "kind": "self_reference",
      "certainty": "high",
      "note": "Cicero recalls his own argument in the lost portion of De Re Publica book 3."
    }
  ]
}
```

**Field rules**:

- `from_loc`: section ref within the current work.
- `to_work`: `id` of another work in `meta/works.yaml`. Use `"self"` for
  references back into the same work.
- `to_loc`: section ref within the target.
- `kind`: one of:
  - `self_reference` — explicit "as I said in X" or "I have written elsewhere."
  - `paraphrase` — re-uses the same example or argument.
  - `verbatim` — reproduces a phrase or sentence.
  - `echo` — looser thematic recurrence.
- `certainty`: `"high"`, `"medium"`, `"low"`. Use `"low"` for thematic
  echoes that may be coincidence.

**Order**: by `from_loc` ascending.

---

## 7. Allusions

**Path**: `data/allusions/<category>/<id>.json`

**Purpose**: candidate quotations and allusions to other ancient authors
(Homer, Ennius, Plautus, the Twelve Tables, Plato, etc.). Flag-not-resolve:
this records suspected sources. A later verification pass — human or
agentic — confirms.

**Schema**:

```json
{
  "schema_version": 1,
  "id": "pro-archia",
  "allusions": [
    {
      "loc": "19",
      "surface": "...",
      "suspected_source": "Ennius, Annales fr. 374 Skutsch",
      "kind": "quotation",
      "certainty": "high",
      "translator_note": "Verbatim from the famous proem; Cicero introduces it as such."
    }
  ]
}
```

**Field rules**:

- `kind`: one of `"quotation"`, `"paraphrase"`, `"echo"`, `"reference"`.
- `certainty`: `"high"` (introduced as a quotation, or fragment match);
  `"medium"` (wording or imagery is distinctive); `"low"` (thematic only).
- `suspected_source`: best canonical reference; for fragmentary authors
  use the standard collection's numbering (Skutsch for Ennius, ROL for
  earlier Roman, Kassel-Austin for Greek comedy, etc.).

**Order**: by `loc` ascending.

---

## 8. Glossary notes (realia)

**Path**: `data/glossary/<category>/<id>.json`

**Purpose**: short explanatory notes for things a reader without a
classical background might miss — *kalends*, the *aedile*, the
*sponsio*, the *pontifices*, particular families, particular places.
**These do NOT become inline footnotes in the reading edition** (per
`STYLE.md`). They feed the backmatter glossary in study/scholar
editions.

**Schema**:

```json
{
  "schema_version": 1,
  "id": "in-catilinam-01",
  "notes": [
    {
      "loc": "1",
      "anchor": "patres conscripti",
      "entity_id": "institution:senate",
      "note": "The senators in formal session; the address that opens every senatorial speech."
    }
  ]
}
```

**Field rules**:

- `anchor`: the surface form in the English translation that the note
  attaches to. (Some readers will encounter the Latin in a side-by-side
  edition; in that case the same note suffices for both languages.)
- `entity_id`: optional. When present, links to the entity registry —
  the glossary builder can dedupe to one entry per entity rather than
  printing the same note many times.
- `note`: ≤ 2 sentences. Keep it tight; the volume aspires to clean
  apparatus.
- One note per work per anchor. If an anchor recurs, the per-work file
  has it once; the build pipeline handles re-resolution by `entity_id`.

**Order**: by `loc` ascending.

---

## 9. Translator's notes log

**Path**: `data/translator-notes.jsonl`

**Purpose**: append-only log of non-obvious rendering decisions. When a
Latin word or phrase admits multiple English renderings and the choice
matters, the translator logs the choice and the reason in one short line.
Useful as methodology, useful as training signal, useful when someone
later wants to argue with a reading.

**Schema** (one JSON object per line):

```json
{"work": "pro-quinctio", "loc": "11", "lat": "scurra", "eng": "buffoon", "alternatives": ["jester", "wit", "wag"], "note": "STYLE.md asks for cognate weight where it lands; 'buffoon' picks up the contemptuous edge.", "date": "2026-05-03"}
```

**Field rules**:

- One JSON object per line; no surrounding array.
- `date`: ISO `YYYY-MM-DD`.
- `lat`: the source word or phrase being adjudicated.
- `eng`: the chosen English rendering.
- `alternatives`: optional array of considered alternatives.
- `note`: the reason. ≤ 2 sentences.
- Translators are encouraged to be selective: log only when the choice
  is genuinely contested. Routine renderings need no entry.

**Order**: chronological by entry. Append-only.

---

## Build profiles

The bound volume can be built in three reader-selectable profiles. See
`build/PROFILES.md` for the full description; the schemas are agnostic
to which profile consumes them.

| Profile | Inline apparatus | Backmatter |
|---|---|---|
| `reading` (default) | none | chronology, brief index of works |
| `study` | none | `reading` + glossary of names, Greek catalogue, allusion index, letter-network appendix |
| `scholar` | small section-anchored markers, marginal section numbers | `study` + cross-reference index, allusion full apparatus, translator's-notes appendix |

The reading edition stays faithful to `STYLE.md`'s "no footnoting in the
translation itself." Inline markers in the scholar edition are anchored
in the margin, not in the prose body.

---

## Validator checks

`scripts/validate.py` enforces:

- Each per-work sidecar's `id` matches a `meta/works.yaml` `id`.
- Each `entity_id` referenced in a mention/note/letter resolves in
  `data/entities.json`.
- Each `to_work` in a crossref resolves in `meta/works.yaml`.
- Each `work` in a Greek-phrase or letter-network entry resolves.
- All required fields are present with valid types.
- `schema_version` is `1` on every artifact.
- File paths follow the per-work convention.

Warnings (non-fatal):

- A drafted work missing one of its sidecars.
- An entity in `entities.json` with no mentions in the corpus.
- A glossary note whose anchor cannot be substring-found in the
  English translation.
