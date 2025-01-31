# PRISMA Flow Diagram for AI in Medicine Systematic Review

```mermaid
flowchart TD
    id1[Records identified through<br>database searching<br>n = 159] --> id3[Total records identified<br>n = 159]
    id3 --> id4[Records after duplicates removed<br>n = 159]
    id4 --> id5[Records screened<br>n = 159]
    id5 --> id7[Full-text articles assessed for eligibility<br>n = 159]
    id7 --> id8[Full-text articles excluded<br>n = 34]
    id7 --> id9[Studies included in<br>qualitative analysis<br>n = 125]
    id9 --> id10[Studies included<br>n = 125]

    classDef box fill:#f9f,stroke:#333,stroke-width:2px;
    class id1,id3,id4,id5,id7,id8,id9,id10 box;
```

## Diagram Notes

1. **Identification**
   - Records identified via PubMed database search: 159
   - Total records identified: 159

2. **Screening**
   - Total records: 159
   - All records were assessed for eligibility

3. **Eligibility**
   - Full-text articles assessed: 159
   - Articles excluded: 34

4. **Included**
   - Studies included in qualitative analysis: 125
   - Studies included: 125

## References
- PRISMA guidelines [@Page2021]