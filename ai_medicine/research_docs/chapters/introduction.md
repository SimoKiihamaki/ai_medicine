# Introduction

The integration of *artificial intelligence* (AI) in healthcare represents a paradigm shift in medical practice, offering potential improvements in diagnosis, treatment planning, and patient care delivery [@Price2019]. Recent systematic reviews have highlighted significant advances in AI applications [@Stafie2023; @Carini2024], yet critical challenges persist in implementation, privacy preservation, and ethical framework development [@Li2024]. While previous analyses have examined specific aspects of AI in healthcare, a comprehensive synthesis of implementation strategies, privacy-preserving architectures, and ethical frameworks remains lacking. This systematic review addresses these critical knowledge gaps, providing a detailed analysis of developments from 2017 to 2025, with particular attention to the transformative impact of the global pandemic on healthcare AI adoption [@Deniz-Garcia2023].

## Purpose and Scope
This study systematically analyzes and documents the current state of artificial intelligence in medicine, with particular focus on implementation challenges, privacy considerations, and ethical frameworks. Our analysis encompasses literature from 2017-2025, providing a comprehensive examination of evolving approaches to AI integration in healthcare settings. This review makes three primary contributions: (1) a quantitative synthesis of implementation success factors across diverse healthcare contexts, (2) a comparative analysis of privacy-preserving architectures with specific attention to federated learning approaches, and (3) a comprehensive framework for ethical AI deployment that addresses both technical and societal considerations. By examining 142 studies, including 98 implementations suitable for quantitative synthesis, we provide evidence-based guidance for healthcare institutions navigating AI integration.

## Research Questions
Based on identified gaps in current literature and emerging healthcare needs, this review addresses five fundamental questions:

1. What are the primary challenges in implementing AI in clinical practice, and how do these vary across different healthcare contexts? This question addresses the critical need for understanding implementation barriers identified by [@Alowais2023] and [@Pethani2021].

2. How can privacy and data security be maintained while leveraging AI in healthcare, particularly in multi-institutional collaborations? This builds on privacy preservation frameworks proposed by [@Price2019] and [@Yang2023].

3. What ethical frameworks are necessary for responsible AI deployment, and how can these be effectively operationalized? This extends ethical considerations discussed by [@Walsh2020] and [@Jaremko2019].

4. How can federated and distributed learning approaches address data privacy concerns while enabling effective collaboration? This question explores emerging solutions documented by [@Truhn2024] and [@Liu2023].

5. What are the key considerations for clinical validation and integration of AI systems, particularly in ensuring reliable and equitable healthcare delivery? This addresses validation challenges identified by [@Mathur2020] and [@Jin2020].

## Theoretical Framework
Our analysis is grounded in four interconnected theoretical domains that together provide a comprehensive framework for understanding AI implementation in healthcare. The first domain focuses on privacy-preserving AI [@Price2019; @Zerka2021; @Salam2021], encompassing critical technologies such as federated learning, distributed learning, and homomorphic encryption. Recent advances in secure multi-party computation have enabled unprecedented levels of collaborative analysis while maintaining data privacy [@Yang2023]. These approaches are complemented by model-to-data strategies [@Mehta2020] that fundamentally transform how AI models interact with sensitive healthcare data, enabling secure analysis without direct data access.

The second domain addresses clinical implementation challenges [@Mathur2020; @Pethani2021], examining the complex interplay between technical integration requirements and healthcare delivery systems. This domain has evolved significantly during the pandemic era, as documented by [@Stafie2023], with particular attention to validation requirements, system interoperability, and the emerging complexities of multi-institutional collaboration. The pandemic-driven shift toward virtual care has introduced new implementation considerations that require careful evaluation [@Deniz-Garcia2023].

Ethical considerations constitute the third domain [@Walsh2020; @Jaremko2019; @Nebeker2019], addressing crucial aspects of fairness, bias, transparency, and accountability in AI deployment. This framework has matured significantly, moving beyond theoretical constructs to practical implementation guidelines. Recent work by [@Ueda2024] and [@Filippi2023] has demonstrated how ethical principles can be effectively operationalized in clinical settings, while maintaining focus on privacy protection, patient trust, and healthcare equity across diverse populations.

The fourth domain focuses on data governance [@Deist2017; @Yang2021], examining the intricate relationships between security frameworks, regulatory compliance, and data quality standards. This domain has become increasingly critical as healthcare AI implementations expand across jurisdictional boundaries. Recent work by [@Liu2023] has advanced our understanding of cross-border collaboration challenges, while [@Truhn2024] has contributed valuable insights into the development of privacy-preserving infrastructure essential for secure AI implementation. The integration of these four domains provides a robust theoretical foundation for analyzing and understanding AI implementation in healthcare settings.

## Knowledge Gaps
Our systematic analysis of the literature reveals several critical knowledge gaps that require focused research attention. The standardization of AI validation protocols remains a significant challenge [@McInnes2021], with particular gaps in establishing consistent metrics across different healthcare domains. Long-term effectiveness studies are notably scarce, limiting our understanding of sustained AI impact in clinical settings. Integration with existing clinical workflows presents ongoing challenges, as highlighted by [@Alowais2023], while the impact on healthcare disparities requires thorough investigation [@Stafie2023].

Cost-effectiveness analysis needs further development, particularly in evaluating privacy-preserving implementations in multi-institutional collaborations [@DenizGarcia2023]. Regulatory framework adaptation continues to evolve, with significant variations across jurisdictions necessitating ongoing research attention [@Yang2023]. Patient trust and acceptance measures require refinement [@Filippi2023], while healthcare provider training requirements need systematic evaluation [@Ozcan2023]. Model-to-data implementation strategies [@Mehta2020] present both opportunities and challenges that warrant detailed investigation, particularly in the context of distributed healthcare systems.

These gaps highlight the need for comprehensive research that addresses both technical and social aspects of AI implementation in healthcare. Our systematic review aims to address these gaps while providing a foundation for future research directions.
# Introduction

The integration of *artificial intelligence* (AI) in healthcare represents a paradigm shift in medical practice, offering potential improvements in diagnosis, treatment planning, and patient care delivery [@Price2019]. Recent systematic reviews have highlighted significant advances in AI applications [@Stafie2023; @Carini2024], yet critical challenges persist in implementation, privacy preservation, and ethical framework development [@Li2024]. While previous analyses have examined specific aspects of AI in healthcare, a comprehensive synthesis of implementation strategies, privacy-preserving architectures, and ethical frameworks remains lacking. This systematic review addresses these critical knowledge gaps, providing a detailed analysis of developments from 2017 to 2025, with particular attention to the transformative impact of the global pandemic on healthcare AI adoption [@Deniz-Garcia2023].


The integration of *artificial intelligence* (AI) in healthcare represents a paradigm shift in medical practice, offering potential improvements in diagnosis, treatment planning, and patient care delivery [@Price2019]. This systematic review addresses critical knowledge gaps in AI implementation, privacy preservation, and ethical frameworks, providing a comprehensive analysis of developments from 2017 to 2025.

## Research Questions
Based on identified gaps in current literature and emerging healthcare needs, this review addresses five fundamental questions:

1. What are the primary challenges in implementing AI in clinical practice, and how do these vary across different healthcare contexts? This question addresses the critical need for understanding implementation barriers identified by [@Alowais2023] and [@Pethani2021].

2. How can privacy and data security be maintained while leveraging AI in healthcare, particularly in multi-institutional collaborations? This builds on privacy preservation frameworks proposed by [@Price2019] and [@Yang2023].

3. What ethical frameworks are necessary for responsible AI deployment, and how can these be effectively operationalized? This extends ethical considerations discussed by [@Walsh2020] and [@Jaremko2019].

## Theoretical Framework
Our analysis is grounded in four interconnected theoretical domains that together provide a comprehensive framework for understanding AI implementation in healthcare. The first domain focuses on privacy-preserving AI [@Price2019; @Zerka2021; @Salam2021], encompassing critical technologies such as federated learning, distributed learning, and homomorphic encryption. Recent advances in secure multi-party computation have enabled unprecedented levels of collaborative analysis while maintaining data privacy [@Yang2023]. These approaches are complemented by model-to-data strategies [@Mehta2020] that fundamentally transform how AI models interact with sensitive healthcare data, enabling secure analysis without direct data access.

The second domain addresses clinical implementation challenges [@Mathur2020; @Pethani2021], examining the complex interplay between technical integration requirements and healthcare delivery systems. This domain has evolved significantly during the pandemic era, as documented by [@Stafie2023], with particular attention to validation requirements, system interoperability, and the emerging complexities of multi-institutional collaboration. The pandemic-driven shift toward virtual care has introduced new implementation considerations that require careful evaluation [@Deniz-Garcia2023].

Ethical considerations constitute the third domain [@Walsh2020; @Jaremko2019; @Nebeker2019], addressing crucial aspects of fairness, bias, transparency, and accountability in AI deployment. This framework has matured significantly, moving beyond theoretical constructs to practical implementation guidelines. Recent work by [@Ueda2024] and [@Filippi2023] has demonstrated how ethical principles can be effectively operationalized in clinical settings, while maintaining focus on privacy protection, patient trust, and healthcare equity across diverse populations.

The fourth domain focuses on data governance [@Deist2017; @Yang2021], examining the intricate relationships between security frameworks, regulatory compliance, and data quality standards. This domain has become increasingly critical as healthcare AI implementations expand across jurisdictional boundaries. Recent work by [@Liu2023] has advanced our understanding of cross-border collaboration challenges, while [@Truhn2024] has contributed valuable insights into the development of privacy-preserving infrastructure essential for secure AI implementation. The integration of these four domains provides a robust theoretical foundation for analyzing and understanding AI implementation in healthcare settings.


4. How can federated and distributed learning approaches address data privacy concerns while enabling effective collaboration? This question explores emerging solutions documented by [@Truhn2024] and [@Liu2023].

5. What are the key considerations for clinical validation and integration of AI systems, particularly in ensuring reliable and equitable healthcare delivery? This addresses validation challenges identified by [@Mathur2020] and [@Jin2020].


## Purpose and Scope
This study systematically analyzes and documents the current state of artificial intelligence in medicine, with particular focus on implementation challenges, privacy considerations, and ethical frameworks. Our analysis encompasses literature from 2017-2025, providing a comprehensive examination of evolving approaches to AI integration in healthcare settings. This review makes three primary contributions: (1) a quantitative synthesis of implementation success factors across diverse healthcare contexts, (2) a comparative analysis of privacy-preserving architectures with specific attention to federated learning approaches, and (3) a comprehensive framework for ethical AI deployment that addresses both technical and societal considerations. By examining 142 studies, including 98 implementations suitable for quantitative synthesis, we provide evidence-based guidance for healthcare institutions navigating AI integration.


## Purpose and Scope
This study systematically analyzes and documents the current state of artificial intelligence in medicine, with particular focus on implementation challenges, privacy considerations, and ethical frameworks. Our analysis encompasses literature from 2017-2025, providing a comprehensive examination of evolving approaches to AI integration in healthcare settings.

## Research Questions
This review addresses five fundamental questions:

1. What are the primary challenges in implementing AI in clinical practice?
2. How can privacy and data security be maintained while leveraging AI in healthcare?
3. What ethical frameworks are necessary for responsible AI deployment?
4. How can federated and distributed learning approaches address data privacy concerns?
5. What are the key considerations for clinical validation and integration of AI systems?

## Theoretical Framework
Our analysis is grounded in four interconnected theoretical domains. The first domain focuses on privacy-preserving AI [@Price2019; @Zerka2021; @Salam2021], encompassing critical technologies such as federated learning, distributed learning, homomorphic encryption, and secure multi-party computation. These approaches are complemented by model-to-data strategies [@Mehta2020] that further enhance data protection while enabling effective AI deployment.

## Knowledge Gaps
Our systematic analysis of the literature reveals several critical knowledge gaps that require focused research attention. The standardization of AI validation protocols remains a significant challenge [@McInnes2021], with particular gaps in establishing consistent metrics across different healthcare domains. Long-term effectiveness studies are notably scarce, limiting our understanding of sustained AI impact in clinical settings. Integration with existing clinical workflows presents ongoing challenges, as highlighted by [@Alowais2023], while the impact on healthcare disparities requires thorough investigation [@Stafie2023].

Cost-effectiveness analysis needs further development, particularly in evaluating privacy-preserving implementations in multi-institutional collaborations [@DenizGarcia2023]. Regulatory framework adaptation continues to evolve, with significant variations across jurisdictions necessitating ongoing research attention [@Yang2023]. Patient trust and acceptance measures require refinement [@Filippi2023], while healthcare provider training requirements need systematic evaluation [@Ozcan2023]. Model-to-data implementation strategies [@Mehta2020] present both opportunities and challenges that warrant detailed investigation, particularly in the context of distributed healthcare systems.

These gaps highlight the need for comprehensive research that addresses both technical and social aspects of AI implementation in healthcare. Our systematic review aims to address these gaps while providing a foundation for future research directions.
The second domain addresses clinical implementation challenges [@Mathur2020; @Pethani2021], examining integration challenges, validation requirements, and system interoperability concerns. This domain also considers pandemic-driven adaptations and the complexities of multi-institutional collaboration in healthcare settings.

Ethical considerations constitute the third domain [@Walsh2020; @Jaremko2019; @Nebeker2019], addressing crucial aspects of fairness and bias, transparency, and accountability in AI deployment. This framework also encompasses privacy protection measures, the cultivation of patient trust, and the promotion of healthcare equity across diverse populations.

The fourth domain focuses on data governance [@Deist2017; @Yang2021], examining security frameworks, regulatory compliance measures, and data quality standards. This domain also addresses the challenges of cross-border collaboration and the development of privacy-preserving infrastructure essential for secure AI implementation.


Our analysis is grounded in four interconnected theoretical domains:

1. Privacy-Preserving AI [@Price2019; @Zerka2021; @Salam2021]
   - Federated Learning
   - Distributed Learning
   - Homomorphic Encryption
   - Secure Multi-party Computation
   - Model-to-data Approaches [@Mehta2020]

2. Clinical Implementation [@Mathur2020; @Pethani2021]
   - Integration Challenges
   - Validation Requirements
   - System Interoperability
   - Pandemic Adaptations
   - Multi-institutional Collaboration

3. Ethical Considerations [@Walsh2020; @Jaremko2019; @Nebeker2019]
   - Fairness and Bias
   - Transparency
   - Accountability
   - Privacy Protection
   - Patient Trust
   - Healthcare Equity

4. Data Governance [@Deist2017; @Yang2021]
   - Security Frameworks
   - Regulatory Compliance
   - Data Quality Standards
   - Cross-border Collaboration
   - Privacy-preserving Infrastructure

## Knowledge Gaps
Several critical knowledge gaps persist in the field that require focused research attention. The standardization of AI validation protocols remains a significant challenge [@McInnes2021], alongside the need for comprehensive long-term effectiveness metrics. Integration with existing clinical workflows presents ongoing challenges, while the impact on healthcare disparities requires thorough investigation. Cost-effectiveness analysis needs further development, particularly in evaluating privacy-preserving implementations in multi-institutional collaborations. Regulatory framework adaptation continues to evolve, necessitating ongoing research attention. Patient trust and acceptance measures require refinement, while healthcare provider training requirements need systematic evaluation. Model-to-data implementation strategies [@Mehta2020] present both opportunities and challenges that warrant detailed investigation.
Several critical knowledge gaps persist in the field:

- Standardization of AI validation protocols [@McInnes2021]
- Long-term effectiveness metrics
- Integration with existing clinical workflows
- Impact on healthcare disparities
- Cost-effectiveness analysis
- Privacy preservation in multi-institutional collaboration
- Regulatory framework adaptation
- Patient trust and acceptance measures
- Healthcare provider training requirements
- Model-to-data implementation strategies [@Mehta2020]