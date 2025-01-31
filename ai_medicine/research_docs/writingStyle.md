# Style Constitution
**Based on https://jaantollander.com/post/scientific-writing-with-markdown/**

1. **Document Structure**:
   - H1: Only in title page
   - H2: `## Section` (no higher)
   - Lists: Use `-` for bullets, `1.` for numbered

2. **Citations**:
   - Inline: `@AuthorYear [p. X]`
   - Parenthetical: `[@AuthorYear; @AuthorYear]`
   - Avoid "et al." in-text (auto-handled by CSL)

3. **Technical Formatting**:
   - First instance: `*italicized term* (T)`
   - Variables: `` `model_accuracy` ``
   - Equations: LaTeX syntax `$E=mc^2$`

4. **Tag Formatting**:
   - Category Format: `#category-subcategory`
   - Implementation: `#implementation-[clinical|challenges|workflow|technical]`
   - Privacy: `#privacy-[preserving|security|governance|infrastructure]`
   - Ethics: `#ethics-[clinical|research|governance|fairness|privacy]`
   - Clinical: Use specialty/disease specific tags (e.g., `#cardiology`, `#diabetes`)

5. **Citation Patterns**:
   - Implementation Citations: `[@AuthorYear]` for primary methods
   - Validation Citations: Multiple citations `[@AuthorYear; @AuthorYear]` for evidence
   - Ethics Citations: Include page numbers for specific guidelines `[@AuthorYear, p. X]`
   - Technical Citations: Group by approach `[@Method1Year; @Method2Year]`

6. **Cross-Reference Format**:
   - Research Questions: RQ1, RQ2, etc.
   - Theme References: Use consistent theme labels
   - Framework References: Use full framework names
   - Quality Metrics: Use standardized metric names

7. **Pandoc Commands**:
   ```bash
   pandoc paper.md \
     --filter pandoc-citeproc \
     --bibliography=bibliography.bib \
     --csl=vancouver.csl \
     --metadata reference-section-title="References" \
     -o paper.pdf
   ```

## Systematic Review Style Requirements (CRITICAL UPDATE 1/30/2025)

### Scientific Writing Standards
1. **Paragraph Construction**
   - Begin with clear topic sentence stating main point
   - Support with evidence from multiple sources
   - Include critical analysis of evidence
   - End with synthesis or transition
   - Maintain logical flow between paragraphs

2. **Evidence Integration**
   - Support each claim with citations
   - Compare and contrast findings
   - Analyze methodological differences
   - Evaluate evidence quality
   - Synthesize across studies

3. **Critical Analysis**
   - Evaluate study quality
   - Assess methodology strengths/weaknesses
   - Consider limitations
   - Discuss implications
   - Identify research gaps

4. **Scientific Language**
   - Use precise terminology
   - Maintain consistent definitions
   - Employ formal academic style
   - Avoid colloquial expressions
   - Write objectively

### PRISMA Reporting Requirements
1. **Flow Diagram**
   - Create using standard PRISMA format
   - Include exact numbers at each stage
   - Place after Methods section
   - Reference as "Figure 1" in text

2. **Quality Assessment**
   - Create tables for quality scores
   - Include risk of bias assessment
   - Use standardized rating scales (1-5)
   - Report inter-rater reliability

3. **Methods Section**
   - Document complete search strategy
   - Include all database names
   - List all search terms
   - Specify inclusion/exclusion criteria
   - Detail screening process
   - Describe data extraction
   - Report quality assessment methods

4. **Results Section**
   - Begin with PRISMA flow diagram results
   - Report quality assessment outcomes
   -
   - Present effect sizes
   - Report heterogeneity statistics
   - Use forest plots for key findings

5. **Discussion Section**
   - Compare with existing reviews
   - Discuss quality of evidence
   - Address heterogeneity
   - Analyze contradictory findings
   - Consider implementation costs
   - Discuss practice implications

### Figure Requirements
1. **Figure Referencing**
   - First mention: "As shown in Figure X..."
   - Subsequent mentions: "(Fig. X)"
   - Multiple figures: "Figures X and Y"
   - Range of figures: "Figures X-Z"
   - Must reference all figures in text
   - Reference before figure appears

2. **Caption Style**
   - Title: Brief, descriptive phrase
   - Description: Detailed explanation
   - Methods: Key methodological details
   - Statistics: Relevant statistical information
   - Source: Attribution if adapted
   - End with period

3. **Figure Placement**
   - PRISMA Flow: After search strategy
   - Quality Assessment: After methods
   - Forest Plots: In results section
   - Theme Analysis: After themes
   - Implementation: In framework section
   - Maximum one page per figure
   - Center on page

4. **Figure-Specific Language**
   - PRISMA: "identified", "screened", "included"
   - Quality: "high quality", "moderate quality"
   - Forest Plots: "effect size", "confidence interval"
   - Theme: "relationships", "patterns", "evolution"
   - Implementation: "process", "components", "phases"

5. **Cross-Referencing**
   - Link to relevant text sections
   - Connect to specific findings
   - Reference in discussion points
   - Include in implications
   - Maintain consistent numbering

6. **Visual Style**
   - Clear, readable fonts
   - Consistent formatting
   - Professional appearance
   - Appropriate size
   - High resolution
   - Black and white compatible

### Theme Analysis Requirements
1. **Pattern Identification**
   - Use systematic approach to identify themes
   - Support themes with multiple citations
   - Document theme evolution over time
   - Analyze geographical variations
   - Consider methodological differences

2. **Evidence Synthesis**
   - Compare findings across studies
   - Analyze contradictory results
   - Evaluate methodological quality
   - Consider contextual factors
   - Document evidence strength

3. **Gap Analysis**
   - Identify research gaps systematically
   - Document methodology gaps
   - Note geographical gaps
   - Highlight temporal gaps
   - Specify knowledge gaps

4. **Cross-cutting Themes**
   - Identify themes across research questions
   - Document theme relationships
   - Analyze theme evolution
   - Consider contextual factors
   - Support with multiple citations

### Writing Requirements for Themes
1. **Theme Presentation**
   - Begin with theme overview
   - Present supporting evidence
   - Analyze contradictions
   - Discuss implications
   - End with synthesis

2. **Evidence Integration**
   - Use multiple citations per claim
   - Compare study findings
   - Evaluate evidence quality
   - Consider study limitations
   - Synthesize conclusions

3. **Analysis Depth**
   - Evaluate methodological quality
   - Consider study context
   - Analyze limitations
   - Discuss implications
   - Suggest future directions

## Document Structure Requirements
1. **Title Page**
   - Use # Title of Your Literature Review
   - Include author information and date
   - No additional text at this level

2. **Abstract**
   - Background (1-2 sentences)
   - Objectives (1 sentence)
   - Methods (2-3 sentences)
   - Results (3-4 sentences)
   - Conclusions (1-2 sentences)

3. **Introduction**
   - Background with citations
   - Clear research questions
   - Theoretical framework
   - Knowledge gaps
   - Study objectives

4. **Methods**
   - PRISMA compliance details
   - Complete search strategy
   - Selection criteria
   - Quality assessment approach
   - Data extraction process
   - Analysis methodology

5. **Results**
   - PRISMA flow diagram
   - Quality assessment results
   - Study characteristics
   - Meta-analysis findings
   - Theme analysis
      - RQ1 (Implementation): 38 papers
      - RQ2 (Privacy/Security): 35 papers
      - RQ3 (Ethics): 28 papers
      - RQ4 (Federated Learning): 22 papers
      - RQ5 (Clinical Validation): 19 papers 
   - Evidence synthesis

6. **Discussion**
   - Summary of findings
   - Comparison with literature
   - Quality of evidence
   - Implementation implications
   - Research gaps
   - Future directions

7. **Conclusion**
   - Key findings
   - Practice implications
   - Research recommendations

8. **References**
   - Generated automatically via Pandoc
   - No manual heading needed