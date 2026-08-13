# Evntry Blog — Writing Guide

Use this document when writing or editing blog posts. The [Claude.ai system prompt](#claudeai-system-prompt) at the bottom is a ready-made block you can paste before asking Claude to draft a new article.

---

## Where articles live

All English articles go in:

```
src/content/blog/en/<slug>.mdx
```

`<slug>` is the kebab-case version of the title — all lowercase, hyphens only, no underscores or special characters. The slug becomes the URL:

| Title | File | URL |
|---|---|---|
| Stop Losing Money to Ticket Fees | `stop-losing-money-to-ticket-fees.mdx` | `/blog/stop-losing-money-to-ticket-fees` |
| How to Sell Out Your Next Event | `how-to-sell-out-your-next-event.mdx` | `/blog/how-to-sell-out-your-next-event` |

---

## Frontmatter

Every `.mdx` file must start with a YAML frontmatter block between `---` markers.

```yaml
---
title: "Your Article Title"
description: "One or two sentence teaser. Used in the blog index card and social previews. 120–160 characters. No trailing period."
date: 2026-08-13
tag: "Pricing"
lang: en
---
```

| Field | Type | Required | Notes |
|---|---|---|---|
| `title` | string | ✅ | Title-case, quoted. Rendered automatically as the page heading. |
| `description` | string | ✅ | Short teaser for cards and SEO. Don't repeat the title word-for-word. |
| `date` | date | ✅ | `YYYY-MM-DD` — **no quotes**. Quoting it causes a build error. |
| `tag` | string | ✅ | Single category label. Capitalised. E.g. `"Pricing"`, `"Promotion"`, `"Operations"`, `"Product"`. |
| `lang` | string | ✅ | Always `en` for English articles. |
| `ogTitle` | string | ❌ optional | Override the social/OG title only if it needs to differ from `title`. Omit when not needed. |

---

## Article structure

```
1. Lead paragraph      — the hook; larger font automatically, no heading before it
2. ## Section (×3–5)  — each covers one point; renders with an orange left border
3. ---                 — horizontal rule separating article body from FAQ
4. ## FAQ              — H2 label, then H3 for each question
```

### Lead paragraph
The very first paragraph of the body gets a larger font treatment (18 px vs 16 px) automatically. Just start writing — **no `#` heading before it**. 2–3 strong sentences that hook the reader and frame the article.

### H2 section headings
Use `##` for all main section headings. Keep them **title case** (not ALL CAPS). Aim for 3–5 sections.

```markdown
## Where Traditional Platforms Take Their Cut
```

### H3 for FAQ questions
Use `###` inside the FAQ block — not `**bold text**` inside a paragraph. The layout styles `###` distinctly from body text.

```markdown
## FAQ

### Does Evntry really charge zero fees to fans?

Yes. Fans pay exactly the ticket price you set...
```

### Horizontal rule
Use `---` on its own line between the article body and the FAQ section. Renders as a thin divider with generous whitespace. Use it once per article.

---

## Supported Markdown elements

| Element | Syntax | Notes |
|---|---|---|
| Lead paragraph | First `<p>` in body | Larger, auto-styled — no heading prefix |
| Section heading | `## Heading` | Orange left border, title case |
| Sub-heading / FAQ question | `### Heading` | Smaller bold heading |
| Bold | `**text**` | Brightens text; use sparingly |
| Italic | `*text*` | Standard italic |
| Unordered list | `- item` | Bulleted |
| Ordered list | `1. item` | Numbered |
| Horizontal rule | `---` | Thin divider line |
| Blockquote | `> text` | Left-border pull quote |

### Do NOT use

- **`# H1`** — the layout injects the title as H1 from frontmatter. Adding another H1 breaks the page.
- **`#### H4` and below** — unstyled; use `###` instead.
- **Images** — not yet supported. Don't include `![]()` image syntax until image support is added.
- **Raw HTML or JSX components** — not set up.

---

## Writing tone

**Audience:** Venue owners and event organisers — bars, clubs, small theatres, promoters. 50–500 capacity. Practical, busy people who distrust marketing filler.

**Voice:**
- Direct. Say the thing plainly.
- No hype. No "game-changing", "revolutionary", "seamless", "unlock", "empower".
- No filler: "in today's world", "it's important to note that", "without further ado", "dive into".
- Short sentences. Vary length. Long paragraphs → break them.
- First person plural (`we`, `our`) as Evntry. Second person (`you`, `your`) for the reader.
- Be honest about trade-offs, including when Evntry isn't the right fit.

**Length:** 800–1,500 words. Long enough to be useful; short enough to read in one sitting.

---

## Before you commit — checklist

- [ ] File is at `src/content/blog/en/<slug>.mdx`
- [ ] Slug matches the title in kebab-case
- [ ] All required frontmatter fields present
- [ ] `date` is bare `YYYY-MM-DD` — no quotes
- [ ] No `# H1` heading in the body
- [ ] First paragraph is plain text with no heading before it
- [ ] FAQ questions use `### H3`
- [ ] `---` divider appears once, between body and FAQ
- [ ] No images
- [ ] Run `npm run build` locally to confirm no errors

---

## Claude.ai system prompt

Paste this at the top of your conversation in Claude.ai (or as a system prompt) before asking it to write or revise an Evntry article. It tells Claude exactly what format and tone to use.

---

```
You are writing a blog post for Evntry, a ticketing platform for venue owners and event organisers (bars, clubs, small theatres — 50–500 capacity). The audience is practical, busy people who distrust marketing fluff.

OUTPUT a valid MDX file with this exact structure:

---
title: "Article Title Here"
description: "One or two sentence teaser, 120–160 characters, no trailing period."
date: YYYY-MM-DD
tag: "Category"
lang: en
---

[Lead paragraph — 2–3 sentences, no heading before it]

## Section One

[Body paragraphs]

## Section Two

[Body paragraphs]

## Section Three

[Body paragraphs]

[Add 1–2 more ## sections as needed. Target 3–5 total.]

---

## FAQ

### Question one?

Answer.

### Question two?

Answer.

### Question three?

Answer.

RULES:
- No # H1 in the body — the title is injected automatically from frontmatter.
- Section headings use ## in title case (not ALL CAPS).
- FAQ questions use ### (not **bold** inside a paragraph).
- Use --- alone on a line exactly once, between the article body and the FAQ.
- No images. No HTML. No JSX.
- date is bare YYYY-MM-DD with no quotes.
- 800–1,500 words total.
- Voice: direct, plain, no hype. Short sentences. No filler phrases ("in today's world", "it's important to note", "game-changing", "dive into").
- Bold (**text**) for key terms or numbers — use sparingly.
- End FAQ answers honestly, including when the answer is "this might not be the right fit for you."
```
