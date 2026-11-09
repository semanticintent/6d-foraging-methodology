# Trigger Keywords Reference

> **"Language patterns reveal severity. Train your systems — and your teams — to listen."**

This comprehensive reference catalogs **trigger keywords** by dimension and urgency level. Use this for:
- Automated alert configuration
- Team training on escalation protocols
- Natural language processing (NLP) in support/monitoring systems
- Incident severity classification

---

## How to Use This Reference

### For Automated Systems

Configure your monitoring, ticketing, and communication platforms to flag these keywords:

**Example: Zendesk/ServiceNow alert rule**
```
IF ticket.body CONTAINS ["lawsuit", "breach of contract", "canceling", "legal action"]
THEN severity = HIGH
AND notify = executive_team
AND SLA = 1_hour_response
```

### For Human Training

Train support, sales, customer success, and operations teams to recognize and escalate these patterns:

**Example: CSM training**
- **See "reconsidering"** in renewal call → Flag as medium urgency, notify manager
- **See "unacceptable"** in email → Flag as high urgency, escalate to executive sponsor within 1 hour
- **Customer goes silent** after complaint → Track as early churn signal

### Urgency Scoring

Each keyword maps to a **Sound (urgency) score** in the 3D lens:

| Urgency Level | Sound Score | Response Time |
|--------------|-------------|---------------|
| **High** | 8-10 | Executive escalation within 1 hour |
| **Medium** | 4-7 | Manager review within 24 hours |
| **Low / Early Warning** | 1-3 | Track pattern over time |

---

## D1: Customer Impact Keywords

### High Urgency (Sound = 8-10)

**Legal/Contractual Threats:**
```
"lawsuit"                    "legal action"               "attorney"
"breach of contract"         "material breach"            "sue"
"arbitration"                "litigation"                 "court"
"cease and desist"           "not what we signed up for"  "contractual obligation"
```

**Immediate Churn Signals:**
```
"canceling"                  "terminating contract"       "ending relationship"
"switching to [competitor]"  "already signed with"        "moving to"
"stop payment"               "demand refund"              "cancellation notice"
"unacceptable"               "unacceptable service"       "this is unacceptable"
```

**Escalation Language:**
```
"escalating to CEO"          "calling your boss"          "executive escalation"
"speaking to leadership"     "taking this higher"         "demand to speak to"
"board of directors"         "investor notification"      "public disclosure"
```

**Action Required:**
- Executive sponsor assigned within 1 hour
- Root cause analysis initiated immediately
- Customer communication plan within 4 hours
- Daily executive updates until resolved

---

### Medium Urgency (Sound = 4-7)

**Dissatisfaction Signals:**
```
"disappointed"               "very disappointed"          "let down"
"expected better"            "expected more"              "not meeting expectations"
"frustrated"                 "frustrating experience"     "continuously frustrated"
"concerned about"            "growing concern"            "becoming concerned"
```

**Renewal Risk:**
```
"reconsidering"              "reconsidering options"      "reevaluating"
"considering alternatives"   "shopping around"            "looking at competitors"
"will not renew"             "unlikely to renew"          "renewal at risk"
"budget review"              "cost cutting"               "procurement review"
```

**Service Issues:**
```
"not working as advertised"  "doesn't do what you said"   "missing features"
"support unresponsive"       "slow response"              "haven't heard back"
"need clarification"         "need explanation"           "need to discuss"
"quality declining"          "service degraded"           "not like before"
```

**Action Required:**
- Manager review within 24 hours
- Customer health score updated
- Retention plan if revenue >$X threshold
- Weekly monitoring until resolved

---

### Low Urgency / Early Warning (Sound = 1-3)

**Passive Inquiries:**
```
"just wondering"             "curious about"              "quick question"
"any updates on"             "status update"              "just checking"
"for future reference"       "down the road"              "eventually"
"thought it would be"        "assumed this would"         "expected this to"
```

**Minor Friction:**
```
"is this normal"             "is this expected"           "does everyone experience"
"not urgent but"             "when you get a chance"      "low priority"
"nice to have"               "would be great if"          "feature request"
"slightly confusing"         "minor issue"                "small problem"
```

**Action Required:**
- Log for pattern analysis
- Review in monthly customer health review
- No immediate escalation unless pattern emerges

---

## D2: Employee Impact Keywords

### High Urgency (Sound = 8-10)

**Resignation Signals:**
```
"I'm done"                   "I quit"                     "putting in notice"
"resignation"                "last day"                   "two weeks notice"
"can't do this anymore"      "I'm out"                    "looking for other jobs"
"accepted another offer"     "leaving for"                "found new position"
```

**Burnout/Mental Health:**
```
"burned out"                 "completely burned out"      "can't take it anymore"
"mental health"              "breaking point"             "at my limit"
"unsustainable"              "this is unsustainable"      "not sustainable"
"exhausted"                  "physically exhausted"       "mentally drained"
```

**Hostile Environment:**
```
"hostile environment"        "toxic"                      "harassment"
"discrimination"             "bullying"                   "hostile workplace"
"unsafe"                     "threatening"                "retaliation"
"HR complaint"               "EEOC"                       "legal action"
```

**Action Required:**
- Immediate HR involvement
- Manager 1:1 within 4 hours
- Retention plan if critical role
- Exit interview if departure confirmed
- Legal review if hostile environment claims

---

### Medium Urgency (Sound = 4-7)

**Workload Stress:**
```
"overwhelmed"                "swamped"                    "drowning"
"too much on my plate"       "can't keep up"              "underwater"
"need help"                  "need support"               "can't do this alone"
"understaffed"               "not enough people"          "we're short-handed"
```

**Work-Life Balance:**
```
"no work-life balance"       "always working"             "no time off"
"working weekends"           "late nights"                "missed dinner again"
"haven't seen my family"     "sacrificing personal time"  "all-consuming"
```

**Recognition Issues:**
```
"underappreciated"           "not valued"                 "taken for granted"
"no recognition"             "thankless"                  "nobody notices"
"unfair"                     "playing favorites"          "unequal treatment"
"no growth"                  "dead end"                   "going nowhere"
```

**Action Required:**
- Manager check-in within 48 hours
- Workload review and rebalancing
- Recognition plan (if applicable)
- Career development conversation (if growth concerns)

---

### Low Urgency / Early Warning (Sound = 1-3)

**Career Exploration:**
```
"just curious about"         "hypothetically"             "asking for a friend"
"career paths"               "what are my options"        "advancement opportunities"
"development opportunities"  "learning budget"            "training available"
"how do other teams"         "what's it like in"          "transfer options"
```

**Policy Questions:**
```
"work from home policy"      "remote work"                "flexible schedule"
"PTO policy"                 "parental leave"             "sabbatical"
"is it just us"              "do other companies"         "industry standard"
```

**Action Required:**
- Document for trend analysis
- Include in next 1:1
- No immediate action unless pattern across multiple employees

---

## D3: Revenue Impact Keywords

### High Urgency (Sound = 8-10)

**Contract/Legal:**
```
"penalty clause"             "breach of contract"         "contract violation"
"termination for cause"      "material breach"            "sue for damages"
"demand refund"              "withholding payment"        "stop payment"
"lawsuit"                    "legal action"               "attorney involvement"
```

**Financial Crisis:**
```
"revenue restatement"        "write-off"                  "impairment"
"audit finding"              "material weakness"          "fraud"
"going concern"              "bankruptcy"                 "cash crisis"
```

**Immediate Revenue Loss:**
```
"canceling contract"         "terminating immediately"    "stop all work"
"invoice dispute"            "refuse to pay"              "not paying this"
"chargeback"                 "payment reversal"           "demand credit"
```

**Action Required:**
- CFO notification within 1 hour
- Legal review if contractual
- Cash flow impact assessment
- Customer/contract recovery plan
- Board notification if material ($X threshold)

---

### Medium Urgency (Sound = 4-7)

**Negotiation/Pricing:**
```
"renegotiate"                "need better pricing"        "price too high"
"discount"                   "concession"                 "credit"
"competitor quoted"          "price matching"             "price reduction"
"budget cut"                 "reduced budget"             "spending freeze"
```

**Payment Issues:**
```
"delayed payment"            "payment plan"               "extending terms"
"cash flow issue"            "budget constraints"         "approval pending"
"procurement review"         "sourcing review"            "vendor consolidation"
```

**Margin Pressure:**
```
"cost reduction"             "efficiency gains"           "do more with less"
"scope reduction"            "feature cuts"               "downgrade"
"competitive bid"            "RFP process"                "vendor comparison"
```

**Action Required:**
- Sales/account manager review within 24 hours
- Pricing/contract flexibility assessment
- Revenue impact modeling
- Executive sponsor if strategic account

---

### Low Urgency / Early Warning (Sound = 1-3)

**Future Planning:**
```
"next fiscal year"           "budget planning"            "next cycle"
"strategic review"           "long-term planning"         "roadmap discussion"
"exploring options"          "market research"            "benchmarking"
"vendor evaluation"          "assessing needs"            "requirements gathering"
```

**Action Required:**
- Log for quarterly business review
- Upsell/cross-sell opportunity tracking
- No immediate escalation

---

## D4: Regulatory Impact Keywords

### High Urgency (Sound = 8-10)

**Violations/Enforcement:**
```
"violation"                  "regulatory violation"       "compliance violation"
"fine"                       "penalty"                    "sanction"
"cease and desist"           "consent order"              "enforcement action"
"license suspended"          "license revoked"            "operating authority"
"criminal"                   "criminal investigation"     "fraud"
```

**Legal Actions:**
```
"subpoena"                   "investigation"              "regulatory investigation"
"SEC investigation"          "DOJ investigation"          "OIG investigation"
"audit failure"              "failed audit"               "adverse opinion"
"material weakness"          "significant deficiency"     "control failure"
```

**Immediate Jeopardy (Healthcare-specific):**
```
"immediate jeopardy"         "threat to patient safety"   "harm to residents"
"license termination"        "CMS termination"            "survey findings"
```

**Action Required:**
- Legal/Compliance team notification within 1 hour
- Executive team briefing immediately
- External counsel engagement (if needed)
- Remediation plan within 24 hours
- Board notification

---

### Medium Urgency (Sound = 4-7)

**Audit Findings:**
```
"audit finding"              "deficiency"                 "observation"
"non-compliance"             "gap"                        "control gap"
"remediation required"       "corrective action"          "action plan"
"certification gap"          "accreditation risk"         "license renewal"
```

**Documentation/Process:**
```
"documentation missing"      "records incomplete"         "no evidence of"
"policy violation"           "procedure not followed"     "deviation from standard"
"training expired"           "certification lapsed"       "not current"
"deadline approaching"       "renewal pending"            "inspection scheduled"
```

**Action Required:**
- Compliance team review within 24 hours
- Remediation plan within 1 week
- Tracking until closure
- Monthly compliance report update

---

### Low Urgency / Early Warning (Sound = 1-3)

**Proactive Compliance:**
```
"new regulation"             "proposed rule"              "draft guidance"
"industry guidance"          "best practice"              "standard update"
"peer comparison"            "benchmarking"               "gap assessment"
"voluntary disclosure"       "proactive review"           "self-assessment"
```

**Action Required:**
- Compliance team awareness
- Impact assessment within 30 days
- No immediate action required

---

## D5: Quality Impact Keywords

### High Urgency (Sound = 8-10)

**Safety/Critical Failures:**
```
"recall"                     "safety incident"            "serious injury"
"fatality"                   "death"                      "life-threatening"
"critical defect"            "safety defect"              "design flaw"
"contamination"              "hazardous"                  "toxic"
"data breach"                "security incident"          "hack"
```

**System Failures:**
```
"system failure"             "total failure"              "catastrophic"
"complete outage"            "data loss"                  "data corruption"
"cannot recover"             "unrecoverable"              "critical error"
```

**Regulatory Quality (Healthcare/Manufacturing):**
```
"never event"                "sentinel event"             "serious adverse event"
"patient harm"               "wrong-site surgery"         "medication error (fatal)"
"major nonconformance"       "stop-ship"                  "production halt"
```

**Action Required:**
- Immediate incident response team activation
- Root cause analysis initiated
- Customer notification (if applicable)
- Regulatory reporting (if required)
- Executive escalation

---

### Medium Urgency (Sound = 4-7)

**Defects/Errors:**
```
"defect"                     "bug"                        "error"
"rework"                     "redo"                       "needs correction"
"didn't meet spec"           "out of tolerance"           "off-spec"
"failed inspection"          "failed QC"                  "rejected"
"customer complaint"         "quality complaint"          "dissatisfaction"
```

**Returns/Warranty:**
```
"return"                     "RMA"                        "send back"
"warranty claim"             "covered under warranty"     "replacement needed"
"refund request"             "doesn't work"               "not functioning"
```

**Action Required:**
- Quality team investigation within 24 hours
- Root cause analysis
- Corrective action plan
- Customer communication (if external)

---

### Low Urgency / Early Warning (Sound = 1-3)

**Process Improvements:**
```
"workaround"                 "manual fix"                 "temporary solution"
"known issue"                "acknowledged bug"           "backlog item"
"tech debt"                  "technical debt"             "legacy limitation"
"needs improvement"          "could be better"            "enhancement"
"minor issue"                "cosmetic defect"            "low priority"
```

**Action Required:**
- Log in defect tracking system
- Prioritize in backlog
- Review in sprint planning / quality review

---

## D6: Operational Impact Keywords

### High Urgency (Sound = 8-10)

**System Outages:**
```
"system down"                "outage"                     "complete failure"
"critical failure"           "P1"                         "Sev1"
"cannot operate"             "business stopped"           "production halted"
"data loss"                  "corruption"                 "unrecoverable"
```

**Incidents:**
```
"incident"                   "major incident"             "critical incident"
"disaster recovery"          "failover"                   "emergency"
"all-hands"                  "war room"                   "crisis mode"
```

**Action Required:**
- Incident commander assigned immediately
- War room established
- Customer communication within 1 hour (if external-facing)
- Executive updates every 30 minutes
- Post-incident review required

---

### Medium Urgency (Sound = 4-7)

**Performance Issues:**
```
"workaround"                 "manual process"             "temporary fix"
"bottleneck"                 "slowdown"                   "degraded performance"
"waiting on"                 "blocked by"                 "dependency"
"delayed"                    "behind schedule"            "slipping"
"capacity issue"             "resource conflict"          "contention"
```

**Action Required:**
- Operations team review within 24 hours
- Bottleneck analysis
- Resource reallocation plan
- Stakeholder communication

---

### Low Urgency / Early Warning (Sound = 1-3)

**Efficiency Opportunities:**
```
"inefficient"                "could be better"            "optimization opportunity"
"nice to have"               "future improvement"         "enhancement"
"tech debt"                  "legacy system"              "dated infrastructure"
"minor friction"             "slight delay"               "small inefficiency"
"process improvement"        "streamlining"               "automation candidate"
```

**Action Required:**
- Log in improvement backlog
- Review in quarterly planning
- No immediate action

---

## Cross-Dimensional Keywords

Some keywords indicate **multiple dimensions** simultaneously:

### "Audit" (Regulatory + Quality + Operational)
- Regulatory audit → Compliance review
- Quality audit → Process/product inspection
- Operational audit → Efficiency review

**Action:** Determine audit type, then apply appropriate dimension keywords.

### "Complaint" (Customer + Quality + Regulatory)
- Customer complaint → Service/product dissatisfaction
- Quality complaint → Defect/specification failure
- Regulatory complaint → Violation/non-compliance

**Action:** Classify by complaint source and subject matter.

### "Incident" (Operational + Quality + Regulatory + Employee)
- Operational incident → System/process failure
- Quality incident → Defect/error event
- Regulatory incident → Compliance violation
- Employee incident → Workplace safety/HR issue

**Action:** Multi-dimensional scoring required.

---

## NLP Configuration Examples

### Email/Ticket Scanning (Python/Regex)

```python
# High-urgency customer keywords
HIGH_URGENCY_CUSTOMER = [
    r'\blawsuit\b', r'\blegal action\b', r'\bcanceling\b',
    r'\bunacceptable\b', r'\bbreach of contract\b'
]

# Check email body
import re
for pattern in HIGH_URGENCY_CUSTOMER:
    if re.search(pattern, email_body, re.IGNORECASE):
        urgency = "HIGH"
        notify_executive_team()
        break
```

### Slack/Teams Alert Bot

```javascript
// Monitor #customer-feedback channel
const mediumUrgencyKeywords = [
  'reconsidering', 'disappointed', 'frustrated',
  'expected better', 'concerned about'
];

slackBot.on('message', (msg) => {
  const text = msg.text.toLowerCase();
  const matched = mediumUrgencyKeywords.find(kw => text.includes(kw));

  if (matched) {
    notifyChannel('#customer-success-alerts', {
      severity: 'MEDIUM',
      keyword: matched,
      message: msg.text,
      action: 'Manager review within 24h'
    });
  }
});
```

---

## Industry-Specific Keyword Additions

### Healthcare
**High Urgency:**
- "patient safety event", "harm to patient", "wrong-site surgery"
- "immediate jeoparty", "CMS survey", "state investigation"

### Financial Services
**High Urgency:**
- "SEC investigation", "FINRA violation", "insider trading"
- "Wells notice", "AML violation", "wire fraud"

### Manufacturing
**High Urgency:**
- "line down", "stop-ship", "customer stop order"
- "OSHA citation", "environmental release", "major spill"

### SaaS
**High Urgency:**
- "data breach", "security vulnerability", "unauthorized access"
- "platform outage", "database corruption", "P1 incident"

---

## Contextual Modifiers

Keywords can be **amplified or dampened** by context:

### Amplifiers (increase urgency)
```
"multiple", "all", "every", "systemic", "widespread"
"recurring", "ongoing", "continuous", "persistent"
"critical", "urgent", "immediate", "emergency"
```

**Example:** "ongoing lawsuit" > "potential lawsuit"

### Dampeners (decrease urgency)
```
"potential", "possible", "might", "could", "maybe"
"in the future", "eventually", "someday"
"minor", "small", "slight", "cosmetic"
```

**Example:** "potential concern" < "major concern"

---

## Next Steps

<div class="next-steps">

**📖 [Quick Reference Card](quick-card.md)** — Urgency scoring guide

**📚 [Glossary](glossary.md)** — Define trigger keyword and related terms

**🔍 [Observable Properties](../framework/observable-properties.md)** — See keywords in context by dimension

**📊 [Scoring Methodology](../framework/scoring.md)** — How keywords map to Sound scores

</div>

<style>
.next-steps {
  background: #161b22;
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
  border-left: 4px solid #ffa500;
}

.next-steps a {
  color: #58a6ff;
  text-decoration: none;
  font-weight: 600;
}

.next-steps a:hover {
  text-decoration: underline;
}
</style>

---

**Remember:** Your systems only catch what they're trained to hear. Configure wisely. 🪶
