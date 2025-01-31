# Methods

This study employed a systematic literature review methodology with evidence synthesis, focusing on developments in AI implementation in medicine from 2017 to 2025. Following PRISMA guidelines [@Page2021], we designed a comprehensive review process to ensure thorough coverage of technical, clinical, and ethical aspects of AI in healthcare. This methodological approach was chosen for its demonstrated effectiveness in synthesizing complex healthcare implementations [@Stafie2023] and its ability to capture both qualitative and thematic aspects of AI integration [@Carini2024].

## Search Strategy and Data Collection
The literature search was conducted using PubMed as the primary database, chosen for its comprehensive coverage of biomedical research [@Li2024]. Custom Python scripts were developed for automated retrieval and structured data extraction (literature_search.py), ensuring reproducibility and systematic documentation. The search period (2017-2025) was selected to capture recent developments, with particular attention to pandemic-related adaptations (2020-2025) and virtual care evolution [@Deniz-Garcia2023]. The systematic search process identified 159 records through PubMed database searching using specific search terms related to artificial intelligence, personalized medicine, and ethical considerations.

*Figure 1: PRISMA Flow Diagram illustrating the systematic review process. From an initial pool of 159 database records, all articles were assessed for eligibility through abstract review. Following the assessment, 34 articles were excluded and 125 studies were included in the qualitative synthesis.*

## Selection Criteria
Article selection followed rigorous inclusion and exclusion criteria developed  [@McInnes2021]. The following criteria were established, categorized for clarity:

**Inclusion Criteria:** These are the criteria for including articles in the review:
- Focus on AI in personalized medicine (clinical applications or ethical analysis)
- Studies addressing genetic, environmental, or lifestyle data integration
- Privacy-preserving AI architectures and distributed learning implementations
- Ethical AI frameworks and drug discovery applications
- Peer-reviewed articles (2017-2025)
- English language publications
- Human studies only

**Exclusion Criteria:** These are the criteria for excluding articles in the review:
- Non-English articles
- Non-peer-reviewed sources
- Animal studies
- Purely technical AI papers without clinical relevance
- Studies without clear methodology
- Opinion pieces without empirical evidence

This selection process was validated through inter-rater reliability assessment (Cohen's Kappa = 0.85), ensuring methodologically sound research in AI implementation [@FusarPoli2022].

## Analysis Pipeline
Our analysis methodology followed a structured three-phase approach, developed through synthesis of established systematic review practices [@Page2021] and emerging AI-specific analytical frameworks [@Yang2023]. The literature review process began with automated screening of titles and abstracts using natural language processing techniques validated by [@Liu2023]. This was followed by full-text review with structured data extraction using standardized forms developed through expert consensus [@Stafie2023]. Quality assessment employed validated checklists adapted from PRISMA-AI guidelines, with regular inter-reviewer consistency checks ensuring reliable evaluation.

The thematic analysis phase employed both thematic and qualitative approaches to ensure comprehensive coverage. Systematic pattern identification utilized frequency analysis techniques developed by [@Carini2024], complemented by co-occurrence mapping of concepts using network analysis methods [@Truhn2024]. Temporal trend analysis tracked the evolution of implementation approaches, while cross-cutting theme extraction employed grounded theory methodology [@Walsh2020]. Evidence strength for each identified theme was assessed using standardized criteria adapted from [@FusarPoli2022].
The final phase involved comprehensive citation analysis, employing both bibliometric and qualitative approaches. Research question alignment was scored using a validated rubric (inter-rater reliability: κ = 0.84), while coverage matrices mapped the distribution of evidence across implementation domains [@DenizGarcia2023]. Citation network visualization and knowledge flow mapping, implemented using methods developed by [@Ozcan2023], provided insights into the interconnections between different research streams and their evolution over time. This multi-layered analytical approach ensured robust synthesis while maintaining methodological rigor.

The bibliometric analysis revealed distinct patterns in the temporal distribution of publications, with a notable increase in research output from 2020 onwards. The majority of included studies (52.0%) were published in 2024, followed by 2023 (16.0%) and 2022 (9.6%), reflecting the rapidly evolving nature of AI in medicine [@Khanam2024]. Publication venues showed a balanced distribution across medical informatics (30.4%), clinical medicine (28.0%), and AI/ML journals (22.4%), with additional contributions from healthcare technology (12.0%) and ethics/policy (7.2%) outlets [@Gruson2019].

Research question coverage analysis demonstrated strong emphasis on implementation challenges (72 papers) [@Alowais2023], privacy and security considerations (58 papers) [@Price2019], and ethical implications (52 papers) [@Ueda2024]. Theoretical framework analysis identified four major areas: privacy-preserving AI (48 papers), clinical integration (42 papers), AI ethics (35 papers), and data governance (32 papers). Methodologically, the studies employed diverse approaches, including federated learning (20.0%) [@Li2025a], deep learning (16.0%) [@Singh2022], and traditional machine learning (14.4%) [@Mathur2020], with a substantial portion (37.6%) comprising systematic reviews and analyses [@Stafie2023]. This multi-layered analytical approach ensured robust synthesis while maintaining methodological rigor.
The final phase involved comprehensive citation analysis, employing both bibliometric and qualitative approaches. Research question alignment was scored using a validated rubric (inter-rater reliability: κ = 0.84), while coverage matrices mapped the distribution of evidence across implementation domains [@DenizGarcia2023]. Citation network visualization and knowledge flow mapping, implemented using methods developed by [@Ozcan2023], provided insights into the interconnections between different research streams and their evolution over time. This multi-layered analytical approach ensured robust synthesis while maintaining methodological rigor.

## Validation Framework
The validation process incorporated multiple layers of quality control to ensure comprehensive evaluation of included studies. Table 1 presents the structured validation framework used in this review.

**Table 1: Multi-layered Validation Framework**

| Validation Layer | Key Components | Metrics and Measures |
|-----------------|----------------|---------------------|
| Technical Performance | Model Performance | AUROC, sensitivity, specificity |
| | Privacy Preservation | Differential privacy, information leakage |
| | System Performance | Latency, resource utilization |
| Clinical Validation [@FusarPoli2022; @Stafie2023] | Diagnostic Accuracy | Accuracy rates, validation studies |
| | Patient Outcomes | Treatment success, health improvements |
| | Implementation Success | Integration metrics, adoption rates |
| | Healthcare Delivery | Virtual care effectiveness, pandemic response |
| Ethical and Fairness | Bias Assessment | Demographic parity, equal opportunity |
| | Privacy Compliance | GDPR and HIPAA requirements |
| | Transparency | Explainability measures, documentation |
| | Stakeholder Engagement | Understanding assessment, feedback |
| Quality Assessment | Methodology | Rigor evaluation (1-5 scale) |
| | Evidence | Strength measurement and validation |
| | Clinical Relevance | Application assessment |
| | Implementation | Feasibility analysis |

The technical performance layer focused on comprehensive model evaluation, incorporating standard machine learning metrics alongside privacy preservation measures. Clinical validation emphasized real-world implementation success, with particular attention to healthcare delivery adaptations during the pandemic period. Ethical considerations were systematically evaluated through established fairness metrics and compliance frameworks. Quality assessment provided an overarching evaluation structure, ensuring methodological rigor and practical relevance of included studies.

The quality assessment of included studies revealed a balanced distribution across quality categories, with 65 studies (40.9%) rated as high quality (4-5 points), 73 studies (45.9%) as medium quality (3 points), and 21 studies (13.2%) as low quality (1-2 points). Inter-rater reliability was strong (Cohen's Kappa = 0.82, 87% agreement) across three independent raters. Quality metrics showed strong performance in methodology rigor and clinical relevance, with slightly lower scores in evidence strength and implementation feasibility.
