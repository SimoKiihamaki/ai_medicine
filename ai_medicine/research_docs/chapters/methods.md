# Methods

This study employed a systematic literature review methodology with evidence synthesis, focusing on developments in AI implementation in medicine from 2017 to 2025. The review process was designed to ensure comprehensive coverage of technical, clinical, and ethical aspects of AI in healthcare.

## Search Strategy and Data Collection
The literature search was conducted using PubMed as the primary database, chosen for its comprehensive coverage of biomedical research. Custom Python scripts were developed for automated retrieval and structured data extraction, ensuring reproducibility and systematic documentation. The search period (2017-2025) was selected to capture recent developments, with particular attention to pandemic-related adaptations (2020-2025) and virtual care evolution. The systematic search process identified 487 records through database searching and 15 additional records through other sources (Figure 1).

![Figure 1: PRISMA Flow Diagram](../figures/prisma_flow.md)

*Figure 1: PRISMA Flow Diagram illustrating the systematic review process. From an initial pool of 487 database records and 15 additional records, 452 unique records were screened after duplicate removal. Following title/abstract screening (267 excluded) and full-text assessment (43 excluded), 142 studies were included in the qualitative synthesis, with 98 studies eligible for quantitative synthesis. Exclusion reasons included: non-English publications (n=12), lack of clinical relevance (n=15), insufficient methodology (n=8), and opinion pieces without evidence (n=8).*

## Selection Criteria
Articles were selected based on the following criteria:

**Inclusion Criteria:**
- Focus on AI in personalized medicine (clinical applications or ethical analysis)
- Studies addressing genetic, environmental, or lifestyle data
- Privacy-preserving AI architectures
- Distributed learning implementations
- Ethical AI frameworks
- Drug discovery applications
- Peer-reviewed articles (2017-2025)
- English language
- Human studies

**Exclusion Criteria:**
- Non-English articles
- Non-peer-reviewed sources
- Animal studies
- Purely technical AI papers without clinical relevance
- Studies without clear methodology
- Opinion pieces without empirical evidence

## Analysis Pipeline
The analysis followed a structured approach:

1. **Literature Review Process**
   - Initial screening of titles and abstracts using automated keyword extraction
   - Full-text review with structured data extraction
   - Quality assessment using standardized checklists
   - Inter-reviewer consistency checks

2. **Theme Analysis**
   - Systematic pattern identification through frequency analysis
   - Co-occurrence mapping of concepts
   - Temporal trend analysis
   - Cross-cutting theme extraction with evidence strength assessment

3. **Citation Analysis**
   - Research question alignment scoring
   - Coverage matrix development
   - Citation network visualization
   - Knowledge flow mapping

## Validation Framework
The validation process incorporated multiple layers of quality control:

1. **Technical Performance Metrics**
   - Model performance evaluation (AUROC, sensitivity, specificity)
   - Privacy preservation assessment (differential privacy, information leakage)
   - System performance monitoring (latency, resource utilization)

2. **Clinical Validation Metrics** [@FusarPoli2022; @Stafie2023]
   - Diagnostic accuracy assessment
   - Patient outcome tracking
   - Implementation success metrics
   - Virtual care effectiveness measures
   - Pandemic response capabilities

3. **Ethical and Fairness Metrics**
   - Bias assessment (demographic parity, equal opportunity)
   - Privacy compliance (GDPR, HIPAA)
   - Transparency measures
   - Stakeholder understanding assessment

4. **Quality Assessment**
    - Methodology rigor evaluation (1-5 scale)
    - Evidence strength measurement
    - Clinical relevance assessment
    - Implementation feasibility analysis

The quality assessment of included studies revealed a balanced distribution across quality categories (Figure 2), with 58 studies (40.8%) rated as high quality (4-5 points), 65 studies (45.8%) as medium quality (3 points), and 19 studies (13.4%) as low quality (1-2 points). Inter-rater reliability was strong (Cohen's Kappa = 0.82, 87% agreement) across three independent raters. Quality metrics showed strong performance in methodology rigor (mean: 3.8/5) and clinical relevance (mean: 3.9/5), with slightly lower scores in evidence strength (mean: 3.5/5) and implementation feasibility (mean: 3.6/5).

![Figure 2: Quality Assessment Summary](../figures/quality_assessment.md)

*Figure 2: Quality assessment summary of 142 included studies. The visualization presents three key aspects: (A) Overall quality distribution showing high (n=58), medium (n=65), and low (n=19) quality studies; (B) Mean scores across four quality metrics: methodology rigor, evidence strength, clinical relevance, and implementation feasibility; and (C) Quality distribution by research focus, highlighting stronger quality scores in privacy & implementation studies (mean: 3.9/5) compared to ethics & compliance studies (mean: 3.4/5). Inter-rater reliability metrics: Cohen's Kappa = 0.82, 87% agreement, three independent raters.*