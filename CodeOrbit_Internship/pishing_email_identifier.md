# Phishing Email Identifier — Checklist & Sample Analysis

**Project by:** _<Avisha Masih>_
**Internship:** CodeOrbit Tech — Cyber Security Internship (Batch 7)

## 1. Purpose

This report explains how to identify phishing emails by examining common red
flags, and applies that checklist to five sample emails.

## 2. Phishing Red-Flag Checklist

| Sr.No. | Red Flag | What to Look For |
|---     |----------|-------------------|
|   1    | **Urgent / threatening language** | "Act now," "account suspended," "24 hours or your account will be closed" |
|   2    | **Mismatched or suspicious links** | Hover over links — displayed text vs. actual URL differ, misspelled domains (e.g. `paypa1.com`) |
|   3    | **Unknown or spoofed sender** | Sender address doesn't match the company domain, or uses a free email service |
|   4    | **Generic greeting** | "Dear Customer" instead of your actual name |
|   5    | **Requests for sensitive info** | Asking for passwords, OTPs, card numbers via email |
|   6    | **Poor grammar / spelling** | Unusual phrasing, typos, awkward translations |
|   7    | **Unexpected attachments** | `.exe`, `.zip`, or macro-enabled files you didn't request |
|   8    | **Too-good-to-be-true offers** | Lottery wins, unexpected refunds, prize claims |

## 3. Sample Emails — Analysis

### Sample 1 — "Account Suspended"
> From: security@paypa1-support.com
> Subject: URGENT: Your account will be suspended in 24 hours
> Body: "Click here to verify your account immediately or it will be permanently locked."

**Verdict:** 🚩 Phishing
**Signs:** Urgent language, misspelled domain (`paypa1` not `paypal`), generic threat, pressure to click immediately.

---

### Sample 2 — "Invoice Attached"
> From: billing@amaz0n-orders.com
> Subject: Your invoice #88213 is attached
> Body: "Please find your invoice attached. Open to review charges." (Attachment: invoice.zip)

**Verdict:** 🚩 Phishing
**Signs:** Spoofed domain (`amaz0n` with a zero), unexpected zip attachment, no personal greeting.

---

### Sample 3 — "Team Meeting Reminder"
> From: priya.sharma@codeorbittech.in
> Subject: Reminder: Team sync at 4 PM today
> Body: "Hi Avisha, just a reminder about our sync call today at 4 PM. See you there!"

**Verdict:** ✅ Legitimate
**Signs:** Matches known company domain, personal greeting, no links/attachments, plausible internal context.

---

### Sample 4 — "You've Won a Prize!"
> From: rewards@lucky-draw-winners.net
> Subject: Congratulations! You've won $1000 Gift Card
> Body: "Click below and enter your bank details to claim your reward within 12 hours."

**Verdict:** 🚩 Phishing
**Signs:** Too-good-to-be-true offer, urgency, unknown sender domain, requests banking details.

---

### Sample 5 — "Password Reset Request"
> From: no-reply@github.com
> Subject: Reset your GitHub password
> Body: "We received a request to reset your password. If this wasn't you, ignore this email. [Reset Password]"

**Verdict:** ✅ Likely Legitimate (but verify)
**Signs:** Matches official domain, no urgent threats, standard security-notification format. Best practice: don't click the link directly — go to github.com manually to reset if needed.

## 4. Key Takeaways

1. Always check the **actual sender domain**, not just the display name.
2. Hover over links before clicking — never trust the visible text alone.
3. Legitimate companies rarely ask for sensitive info (passwords, OTP, card numbers) over email.
4. When in doubt, go directly to the official website instead of clicking email links.
5. Urgency and fear are the most common psychological tactics used in phishing.

---
*Prepared as part of the CodeOrbit Tech Cyber Security Internship (Batch 7), Task 3: Phishing Email Identifier.*