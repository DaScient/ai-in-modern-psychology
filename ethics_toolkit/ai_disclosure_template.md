# AI Disclosure and Transparency Template

A user-facing disclosure template for AI products in psychology. Adapt for your
specific deployment; have it reviewed by a clinician *and* a person from the
target population *before* publication.

> Companion to Chapters 10 (*Therapy Chatbots*), 19 (*Recommender Systems*),
> and 21 (*Regulation and Governance*).

## 1. What this system does

> *Example: "**MoodCheck** is a conversational tool that asks you about your
> mood, suggests cognitive-behavioural exercises, and tracks your symptoms
> over time. It is not a substitute for therapy."*

State, in one paragraph, what the system does and what it does not do. Avoid
clinical claims you have not validated.

## 2. Who built it and who pays for it

> *Example: "Built by Example Health Inc., a US-incorporated company. The
> service is free to users; we earn revenue from optional premium features
> and from anonymised aggregate-trends licensing to academic researchers."*

Name the responsible legal entity and the funding model. Conflicts of
interest, including parent companies and major investors, belong here.

## 3. How it works (in two paragraphs)

> *Example paragraph 1: "When you write a message, MoodCheck classifies your
> mood using a language model trained on 200 000 clinically annotated
> messages. The classification is shown in your dashboard..."*
>
> *Example paragraph 2: "If MoodCheck detects language suggesting a crisis,
> it pauses the conversation and shows you crisis-line numbers for your
> region. It does not contact anyone on your behalf."*

Explain the inference pipeline at a level a non-technical user can follow.
Distinguish what the system *does* automatically from what it *does not*.

## 4. What it gets wrong

> *Example: "MoodCheck misses approximately one in five crisis-language
> messages in our internal evaluation. It is more accurate for English than
> for other languages. It does not currently detect..."*

State known false-negative and false-positive rates, populations on which
performance is weaker, and explicit failure modes. The temptation to
underplay this section is the single most common ethical failure of AI
disclosures.

## 5. Data: what we collect, why, and for how long

| Data element | Purpose | Retention | Shared with |
|--------------|---------|-----------|--------------|
| Chat messages | Generate responses | 90 days | Cloud LLM provider (no training) |
| Mood scores | Show your trend | Until you delete | Nobody |
| Account email | Login | Until you delete | Email service provider |

State exactly *what* is collected, *why*, *how long*, and *who else sees it*.
"For service improvement" is not a sufficient purpose.

## 6. Your choices

- **Opt out of analytics:** ____________________________
- **Delete your data:** ________________________________
- **Export your data:** ________________________________
- **Contact us:** ______________________________________

## 7. When to seek help instead

> *Example: "If you are in crisis, please call **988** (US) or your local
> emergency number. If you have ongoing symptoms, please see a licensed
> clinician — MoodCheck is not a replacement for therapy."*

## 8. Updates to this disclosure

When this disclosure changes, current users will be notified in-app and by
email. Past versions are archived at `<URL>`.

---

**Disclosure version:** _______ **Last updated:** _______ **Reviewed by:** _______
