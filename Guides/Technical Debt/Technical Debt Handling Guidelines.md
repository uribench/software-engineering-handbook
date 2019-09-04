# Technical Debt Handling Guidelines

In this article we will address the following aspects of Technical Debt (TD):

1. [What is TD and what it is not?][1]
2. [Why address TD?][2]
3. [Handling TD][3]:
    1. Branding, language and engaging with stakeholders
    2. Architectural debt
    3. Measurement
4. [Execution starting points][4]:
    1. Backlog 
    2. Prevention


## What is Technical Debt and What is not?

The distinction between **what is TD** and **what is not TD** is given here for practical purposes and is not an academic one. ​Read this as an aid in understanding your spend on TD.

### What is Technical Debt?

One way to identify what is TD uses the following three causalities:

- Deliberate
- Outdated
- Bit rot

#### Deliberate ​

Technical debt comes from trading technical learning and code design improvement for market learning and product design improvement, in order to gain shorter time to value, and time to market advantages over slower competitors. ​

#### Outdated ​

Past decisions that don't support new insights.​

#### Bit rot ​

Gradual deterioration through many small changes.​


### What is Not Technical Debt?

The following causalities are **not** considered here as TD:

- Software Obsolescence
- Portfolio Diversity
- Security
- Additional non-TD causalities

They are not considered here as TD mainly because they are typically handled anyway using other business justifications as described in the following sections. Therefore, "branding" them as TD is a missed opportunity.

#### Software Obsolescence

A software (version) is obsolete when it is not possible to get guaranteed support for bug fixes and updates (e.g., security patches) on that version by an approved supplier.

    Examples:  Operating Systems (OS), libraries, compilers, platform components, drivers.

Software obsolescence is transitive. If an OS goes obsolete, it almost always triggers library, compiler or platform component obsolescence. Hardware obsolescence can also trigger software obsolescence.

Software obsolescence is not technical debt because: 

- Delivering secure software which complies to applicable legal constraints is a business promise and with business value.
- Technical debt can be locally and pro-actively prevented and addressed. However, the cost of change for software obsolescence is unavoidable.

#### Portfolio Diversity

Portfolio diversity debt comes from the costs associated with all maintained software branches and configuration diversity that are still active in the installed based.

    Examples: 12 year support guarantees which result in maintenance, FCO costs, option packages

Portfolio diversity is not technical debt because:

- It is introduced by business requests and can be backed with service revenue.

- Portfolio diversity policies are imposed by the business on the software technical community and not managed within that community.

- Option diversity can be profitable when costs are made transparent.

- Portfolio diversity can be pro-actively managed through clear end-of-life policies.

- Business leaders will be prepared to retire unprofitable portfolio diversity if they better understand all costs involved.

#### Security

Security debt comes from the costs associated with the promise given to customers to deliver secure software for a committed period.

Security is not technical debt because:

- Business leaders are prepared to pay to deliver secure software which complies to applicable legal constraints.

#### Additional non-TD causalities

Following are several additional causalities that are not considered here as TD. Note that only causalities that were not discussed in details above are listed here:

- Features directly contributing to a customer need​
- Enabler features​
- Defects (though the presence of defects can indicate technical debt)​
- Hardware obsolescence​
- Legacy (as it can be an asset that is well structured under test delivering customer value)​


## Why Address Technical Debt?

Addressing TD is economical for the following reasons:

- Increase development speed by lowering the cost of change 
- Lower the cost of non-quality by decreasing the number of defects 
- Lower the cost of development by reducing the inventory of maintained lines of code 


## Handling Technical Debt

### Branding and Language Recommendations

#### Do Use

* Increase Speed of change or Innovation speed
* Modernize, Keep up to standards & best practices
* Easier to retain and recruit new talent
* Reduces complexity and in so reduces cost of Maintainability
* Improves Cost of non-quality
* “Product” or “System” Health
* Replacing the “band-aid”
* “Prevention”

#### Avoid

* Refactoring
* Technical Debt
* Bug fixing
* Re-writing 

### Stakeholders

- Look for business opportunities to solve prioritized technical debt items.
- Make solving debt part of your estimates.
- “Ride the waves of opportunity”:

    * Use the ‘boy scout’ rule i.e “Always leave the campground cleaner than you found it.”
    * Reframe software obsolescence as must do for ‘security and compliance’
    * Use hardware obsolescence as code down opportunity
    * Use high business value features as an tech debt reduction opportunity
    * Discuss portfolio rationalization as an R&D efficiency opportunity

### Architectural Debt

Often, dealing with existing technical debt involves the refactoring of existing code in order to refine the separation of concerns, and hence redefine the boundaries among the architectural modules. As an example, when adding a new feature requires modifying existing code to accommodate the new functionality, it means that the existing boundaries are not well defined.

As technical debt refers to the costs of ‘changeability’ these Architectural transformations to keep the solution sustainable would contribute to addressing technical debt. However, we would advise to keep this items separate but remain tightly referenced.

The Architects should then play a significant role in our journey of managing technical debt effectively.

### Measurement

#### Do

- Only estimate opportunities you intend to follow up on
- Determine the ‘impact’ by using t-shirt sizes (eg S,M,L…)
- Understanding how broadly tech debt is affecting speed and/or quality
- Prioritize technical debt using ‘impact’
- Determine the ‘effort’ for high impact opportunities
- Estimate using your team’s estimation method and definition of done
- Spot relevant opportunities using tools
- Experiment with quantification tools trying to spot correlation

#### Do Not

- Be over precise
- Don’t over analyze
- Don’t over rely on quantification tools

## Execution starting points

### Backlog

The benefits of using a backlog for handling technical debt are:

- A technical debt backlog can bring a common understanding of what technical debt means in our context and the common causes.  
- It allows us to capture intentional technical debt decisions.  
- It can also reflect something of our culture towards technical debt as we see our regular commitment to retiring technical debt.  
- If combined with an improvement backlog it can capture quality initiatives, process improvements, devOps practices as well as technical debt.  

Following are few suggestions when using a backlog:

Have a continuous improvement backlog that is: 

1. Treated as an equal citizen:
    * Stories are defined, refined and estimated as any other 
    * Prioritized
    * Included in the scope of each PI, not “only if we have time”

2. Measured and trended:
    * Example - Predictability measure (80% of committed) measured separately for this group of backlog items to prevent (or make visible) when de-prioritized during PI.

### Prevention

Where is it cheapest to prevent debt?

1. Have a policy.
2. Introduce specific automatic quality gates in the CI pipeline to indicate where technical debt may be increasing and break the build or emit clear warnings that require further action.
3. Consider in a Definition of Done:
    * Static analysis
    * Dynamic analysis
    * Reviewed code
    * No tech debt increase
    * Unit tests

---

[1]: #what-is-technical-debt-and-what-is-not
[2]: #why-address-technical-debt
[3]: #handling-technical-debt
[4]: #execution-starting-points