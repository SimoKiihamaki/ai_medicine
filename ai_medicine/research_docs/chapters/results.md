# Results

## Temporal Distribution Overview
The analysis of 125 articles revealed a clear evolution in AI implementation approaches across three distinct phases, reflecting the dynamic progression of the field [@Carini2024]. 

**Early Phase (2017-2019): Foundational Methods.** This initial period, representing 3.2% of the analyzed papers, was characterized by exploratory studies focused on establishing foundational privacy-preserving methods [@Price2019]. Key research during this phase laid the groundwork for subsequent advancements in federated learning and data security [@Gruson2019; @Jaremko2019; @Price2019].

**Mid Phase (2020-2022): Pandemic-Driven Acceleration.** The mid phase showed significant acceleration, accounting for 19.2% of papers. This surge coincided with the rapid adoption of virtual care technologies driven by global healthcare challenges [@Deniz-Garcia2023]. Research during this period focused on adapting AI implementations to address emerging needs in remote healthcare delivery and virtual patient care [@Stafie2023; @Deniz-Garcia2023; @Khanam2024], with studies exploring workflow integration in virtual settings and initial ethical considerations for virtual AI applications [@Nebeker2019; @Fusar-Poli2022].

**Recent Phase (2023-2025): Hybrid Healthcare Optimization.** The most substantial development occurred in the recent phase (2023-2025), comprising 77.6% of papers, with over half from 2024 alone. This phase is characterized by mature approaches to optimizing hybrid healthcare delivery systems. Studies focused on refining AI integration for seamless hybrid models, enhancing data security in interconnected systems, and establishing comprehensive ethical frameworks for diverse AI applications. Recent contributions demonstrate sophisticated integration strategies and emerging trends in privacy-preserving implementations [@Khanam2024; @Petkovic2024b; @Almansour2024; @Bhange2025; @Li2025a; @Feng2024; @Kumar2024; @Miller2024; @Nashwan2024; @Reza2024; @Momtazmanesh2022; @Toit2023; @Visco2023; @Avci2024]. This temporal distribution underscores the field's rapid maturation and adaptation to evolving healthcare needs, consistent with broader trends in digital health innovations [@Yang2023].

## Research Question Findings

Our systematic review addressed five key research questions through qualitative synthesis. The main findings across each research question, organized by domain and supported by key references are summarized in the following tables.

**Table 1: Research Question Findings Summary**

| Research Question             | Domain                | Key Findings                                          | Supporting Evidence                                                                                                |
| :-------------------------- | :-------------------- | :---------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| RQ1: Clinical Implementation | Workflow Integration    | System adaptation and infrastructure requirements     | [@Alowais2023; @DenizGarcia2023; @Stafie2023; @Ozcan2023]                                                                       |
|                             |                       | Staff training and resource allocation                | [@Stafie2023; @Alowais2023; @Ozcan2023]                                                                                      |
|                             |                       | Need for robust data standardization efforts          | [@Ozcan2023; @Kitamura2022a]                                                                                       |
|                             | Domain-Specific       | Specialty-specific workflow modifications             | [@Ozcan2023; @Pethani2021; @Kitamura2022a; @Kitamura2022]                                                                         |
|                             |                       | Tailored implementation approaches for radiology, dentistry | [@Kitamura2022a; @Pethani2021; @Ozcan2023; @Irmici2024; @Parillo2024; @Singh2024]                                             |
| RQ2: Privacy & Security      | Technical Solutions   | Federated learning and secure aggregation             | [@Truhn2024; @Yang2023; @Li2025a; @Ali2023; @Guo2024; @Zerka2021; @Salam2021; @Hossen2023; @Pan2024c; @Liu2023c]                                       |
|                             |                       | Encryption and model-to-data approaches               | [@Liu2023b; @Mehta2020; @Guo2024; @Price2019]                                                                                 |
|                             |                       | Blockchain for enhanced data security                 | [@Ali2023; @Chen2024; @Eliwa2024]                                                                                                       |
|                             | Governance            | Data protection and collaboration frameworks          | [@Price2019; @Deist2017; @Koetzier2024; @Monah2022; @Calvino2024; @Silva2018]                                                                |
|                             |                       | Security infrastructure design and dynamic access control | [@Silva2018; @Price2019; @Truhn2024; @Yang2023; @DenizGarcia2023]                                                                            |
| RQ3: Ethical Frameworks      | Clinical Ethics       | Practice guidelines and patient care                  | [@Ueda2024; @Filippi2023; @Marques2024; @FusarPoli2022]                                                                          |
|                             |                       | Implementation ethics and fairness                    | [@FusarPoli2022; @Ueda2024; @Filippi2023; @Marques2024; @Aldhafeeri2024]                                                                       |
|                             |                       | Bias detection and mitigation strategies              | [@Wang2023; @Ueda2024; @Filippi2023; @Stanley2025; @Verma2025b]                                                                            |
|                             | Research Ethics       | Study design and data usage protocols                 | [@Sui2023; @Nebeker2019; @Monah2022; @Iqbal2022]                                                                            |
|                             |                       | Participant protection frameworks and consent protocols | [@Monah2022; @Nebeker2019; @FusarPoli2022; @Jaremko2019; @Ennis-O'Connor2024c]                                                                       |
| RQ4: Federated Learning      | Clinical Applications | Multi-center collaboration frameworks                 | [@Yang2021; @Li2025a; @Ali2023; @Truhn2024; @Deist2017; @Kitamura2022]                                                                       |
|                             |                       | Disease-specific implementations for oncology, neurology | [@Jaladanki2021; @Kitamura2022a; @Bhange2025; @Vitt2024; @Singh2024; @Alhajahjeh2024; @Tripathi2024b; @Kale2024; @Rajput2025; @Qureshi2022b]          |
|                             |                       | Cross-border initiatives and data sharing frameworks  | [@Kitamura2022a; @Calvino2024; @Ali2023; @Price2019; @Zerka2021; @Salam2021; @Corpas2024b]                                                            |
|                             | Technical Innovations   | Privacy preservation and optimization                 | [@Zerka2021; @Salam2021; @Li2025a; @Ali2023; @Guo2024; @Pan2023; @Hossen2023; @Solar2024c; @Solar2024b; @Wu2024c]                            |
|                             |                       | Model aggregation strategies and performance improvements | [@Salam2021;  @Pan2023; @Gao2023c; @Zeng2024c; @Wu2024c; @Malik2023; @Zhou2024c; @Solar2024c]                                                        |
| RQ5: Clinical Validation     | Methodologies         | Disease-specific protocols and frameworks             | [@Mathur2020; @Jin2020; @Gallone2022; @Cheungpasitporn2024b; @Gurmessa2024b; @Okpete2024; @Wang2024a; @Avci2024; @Surendran2024; @Patcas2022]            |
|                             |                       | Outcome measures and standards for diagnostic accuracy, treatment optimization | [@Gallone2022; @Jin2020; @Mathur2020; @Miller2024; @Qureshi2022b; @Irmici2024; @Parillo2024; @Visco2023; @Yammouri2024; @Ng2024]                             |
|                             | Integration           | Implementation roadmaps and protocols                 | [@Dow2022; @Momtazmanesh2022; @Toit2023; @Mascarenhas2023; @Alhur2024; @Rao2024; @Ennis-O'Connor2024c]                                                                       |
|                             |                       | Performance metrics and optimization for workflow integration, staff adoption | [@Toit2023; @Momtazmanesh2022; @Stafie2023; @Alowais2023; @Ozcan2023; @Pethani2021; @Nashwan2024; @Georgakopoulou2024; @Lindholz2025; @Umesh2024]                             |

The findings reveal significant progress across all research questions, with particularly strong advances in privacy-preserving implementations and ethical framework development. Clinical implementation challenges showed consistent patterns across different medical specialties, while federated learning applications demonstrated successful adaptation to various healthcare contexts. Validation methodologies evolved to address both technical performance and clinical utility, with increasing emphasis on real-world implementation success.

## Geographic Distribution Analysis
The systematic analysis of research contributions revealed distinct regional patterns in AI implementation approaches and priorities. 

**Table 2: Geographic Distribution of Studies**

| Region               | Percentage of Studies | Key Focus Areas                                  | Representative Strengths                                  |
| :------------------- | :-------------------- | :------------------------------------------------- | :-------------------------------------------------------- |
| North America        | 33.6%                 | Clinical Implementation, Regulatory Frameworks     | Healthcare system integration, Regulatory leadership       |
| Europe               | 30.4%                 | Privacy Preservation, Ethical Frameworks           | Data protection research, Cross-border collaboration       |
| Asia                 | 25.6%                 | Technical Innovation, Implementation Strategies    | Novel AI architectures, Pragmatic integration approaches    |
| International Collaborations | 8.0%                 | Global Standards, Cross-border Data Sharing        | Multi-center federated learning, Validation studies        |
| Other Regions        | 2.4%                 | Healthcare Equity, Regional Adaptation           | Context-specific solutions, Adaptable AI implementations |


North America emerged as the leading contributor, accounting for 33.6% of studies, with particular strength in clinical implementation research [@Alowais2023; @DenizGarcia2023; @Stafie2023]. The region demonstrated robust leadership in developing regulatory frameworks and showed significant emphasis on healthcare system integration, reflecting its well-established healthcare infrastructure and regulatory environment [@Price2019; @Ueda2024].

European contributions, comprising 30.4% of studies, showed distinctive focus areas aligned with the region's regulatory landscape [@Ueda2024; @Filippi2023; @Petkovic2024b]. European researchers demonstrated particular prominence in privacy preservation research and ethical framework development, likely influenced by stringent data protection regulations [@Price2019; @Monah2022]. The region also showed strong leadership in facilitating cross-border collaboration, leveraging its integrated research networks and harmonized regulatory frameworks [@Calvino2024; @Deist2017].

Asian institutions, contributing 25.6% of studies, made significant advances in technical innovation, particularly in developing novel AI architectures and federated learning applications [@Yang2021; @Li2025a; @Ali2023]. The region demonstrated growing emphasis on implementation strategies, reflecting the rapid digitalization of healthcare systems across Asian countries [@Khanam2024; @Nashwan2024; @Reza2024]. This technical focus was complemented by pragmatic approaches to healthcare AI integration [@Umesh2024; @Patcas2022].

International collaborations, representing 8.0% of studies, played a crucial role in advancing global standards for AI implementation [@Yang2023; @Calvino2024]. These collaborative efforts primarily focused on developing multi-center federated learning initiatives and establishing robust cross-border data sharing frameworks [@Truhn2024; @Ali2023; @Deist2017]. Such collaborations proved particularly valuable in conducting comprehensive validation studies across diverse healthcare contexts [@FusarPoli2022; @Gallone2022].

The remaining 2.4% of contributions from other regions provided valuable insights into diverse implementation contexts and regional adaptation strategies [@Arizón2023; @Ng2024]. These studies particularly emphasized healthcare equity considerations, offering important perspectives on AI implementation in resource-varied settings and highlighting the need for adaptable solutions that can address diverse healthcare needs across different socioeconomic contexts [@Okpete2024; @Alhajahjeh2024].

## Cross-Cutting Themes
The analysis revealed complex interconnections between implementation, privacy, ethics, and validation domains (Figures 2a-2d). Our citation analysis identified key cross-cutting themes, as detailed in Table 3.

**Table 3: Key Cross-Cutting Themes**

| Theme                  | Papers | Key Concepts                                  |
| :--------------------- | :----- | :-------------------------------------------- |
| Data Privacy           | 48     | Patient confidentiality, Federated Learning, Homomorphic Encryption, Secure Multi-party Computation, Data Governance Frameworks                            |
| Clinical Integration   | 42     | Implementation frameworks, Workflow Adaptation, System Interoperability, Clinical Validation, Healthcare Provider Training         |
| AI Ethics              | 35     | Bias mitigation, Transparency, Accountability, Fairness Metrics, Ethical Guidelines, Patient Trust and Consent                     |
| Technical Innovation   | 32     | Distributed learning, Privacy-preserving methods, Model Architecture Advances, Security Protocol Development, Virtual Care Platforms |
| Regulatory Compliance | 25     | Legal frameworks, GDPR, HIPAA, Data Governance Standards, Cross-border Data Sharing Regulations                  |
| Crisis Preparedness    | 15     | Pandemic Response Protocols, Emergency Scaling Mechanisms, Virtual Surge Capacity, Remote Healthcare Delivery Systems              |


Recent work by [@Marques2024] and [@Petkovic2024b] has demonstrated how these themes intersect in practice, particularly in addressing fairness and transparency requirements.

The privacy-preserving AI domain showed significant development, with 48 papers focusing on patient data protection. This included substantial contributions in federated learning (25 papers) [@Li2025a; @Ali2023], distributed learning (10 papers) [@Deist2017], homomorphic encryption (7 papers) [@Guo2024], and secure multi-party computation (6 papers) [@Truhn2024]. Clinical implementation research (42 papers) addressed integration challenges (15 papers) [@Mascarenhas2023], validation requirements (12 papers) [@Bhange2025], and system interoperability (8 papers) [@Alhur2024].

Ethical considerations (35 papers) encompassed fairness and bias (12 papers) [@Ueda2024], transparency (9 papers) [@Marques2024], accountability (8 papers) [@Iqbal2022], and privacy protection (6 papers) [@Monah2022]. The evolution of themes shows a clear shift from purely technical implementation concerns in the pre-pandemic era to a more balanced approach incorporating virtual care integration and hybrid solutions in recent years, as evidenced by recent implementations [@Nashwan2024; @Reza2024].

*Figures 2a-2d: Thematic analysis diagrams illustrating the interconnections in AI medicine implementation across different dimensions.*

The analysis of cross-cutting themes revealed several key developments across interconnected domains. International collaboration accounted for 8.0% of total studies. This growth was supported by Truhn et al.'s [@Truhn2024] establishment of sophisticated federated learning networks and Ali et al.'s [@Ali2023] development of standardized data exchange protocols, facilitating secure multi-institutional research.

Technical innovation demonstrated substantial progress across multiple fronts. Yang et al. [@Yang2021] advanced privacy-preserving technologies, while Gao et al. [@Gao2023c] made significant contributions to distributed learning optimization. DenizGarcia et al. [@DenizGarcia2023] enhanced security through multi-layer protection systems. The methodological landscape showed diverse approaches, with Review/Analysis studies leading at 37.6%, followed by Federated Learning (20.0%), Deep Learning (16.0%), Traditional ML (14.4%), and Hybrid Approaches (12.0%).

Healthcare integration efforts focused on comprehensive system transformation. Alowais et al. [@Alowais2023] developed sophisticated system interoperability solutions, while DenizGarcia et al. [@DenizGarcia2023] established effective workflow optimization strategies. Stafie et al. [@Stafie2023] contributed crucial healthcare provider adaptation frameworks that facilitated smooth transitions to AI-enhanced clinical workflows.

The pandemic era catalyzed rapid adaptations in healthcare delivery systems. Deniz-Garcia et al. [@DenizGarcia2023] documented widespread virtual care platform adoption, while Fusar-Poli et al. [@FusarPoli2022] developed robust crisis management protocols. Ozcan et al. [@Ozcan2023] analyzed comprehensive digital transformation initiatives that fundamentally reshaped healthcare delivery models.

Ethical framework implementation remained central to successful AI integration. Price et al. [@Price2019] established foundational patient data protection mechanisms, while Ueda et al. [@Ueda2024] developed comprehensive healthcare equity assurance measures. Filippi et al. [@Filippi2023] advanced transparency and accountability systems that enhanced trust in AI-enabled healthcare delivery, ensuring responsible technology deployment.