# PRISMA Flow Diagram for AI in Medicine Systematic Review

```mermaid
flowchart TD
    id1[Records identified through<br>database searching<br>n = 487] --> id3[Records after duplicates removed<br>n = 452]
    id2[Additional records identified<br>through other sources<br>n = 15] --> id3
    id3 --> id4[Records screened<br>n = 452]
    id4 --> id5[Records excluded<br>n = 267]
    id4 --> id6[Full-text articles<br>assessed for eligibility<br>n = 185]
    id6 --> id7[Full-text articles excluded<br>n = 43<br><br>- Non-English n = 12<br>- No clinical relevance n = 15<br>- Insufficient methodology n = 8<br>- Opinion pieces n = 8]
    id6 --> id8[Studies included in<br>qualitative synthesis<br>n = 142]
    id8 --> id9[Studies included in<br>quantitative synthesis<br>n = 98]

    classDef box fill:#f9f,stroke:#333,stroke-width:2px;
    class id1,id2,id3,id4,id5,id6,id7,id8,id9 box;
```

## Diagram Notes

1. **Search Results**
   - Primary database (PubMed): 487 records
   - Additional sources: 15 records
   - Total unique records: 452

2. **Screening Process**
   - Initial screening excluded: 267 records
   - Full-text assessment: 185 articles
   - Final inclusion: 142 articles

3. **Exclusion Reasons**
   - Non-English publications: 12
   - Lack of clinical relevance: 15
   - Insufficient methodology: 8
   - Opinion pieces without evidence: 8

4. **Analysis Inclusion**
   - Qualitative synthesis: 142 studies
   - Quantitative synthesis: 98 studies
   - Meta-analysis eligible: 76 studies

5. **Quality Assessment**
   - High quality (score 4-5): 58 studies
   - Medium quality (score 3): 65 studies
   - Low quality (score 1-2): 19 studies

## References
- PRISMA guidelines [@Page2021]
- Systematic review methodology [@Moher2009]
- Quality assessment framework [@FusarPoli2022]