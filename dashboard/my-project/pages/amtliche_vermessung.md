---
title: Amtliche Vermessung
---

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

```sql personal
UNPIVOT 
(
SELECT 
    *
FROM 
    agi_amtliche_vermessung.personal
)
ON COLUMNS(* EXCLUDE (jahr))
INTO
    NAME kategorie
    VALUE anzahl
```

<BarChart
    title='Personal in der amtlichen Vermessung' 
    data={personal}
    x=jahr
    y=anzahl
    series=kategorie
    yAxisTitle="Personen"
    markers=true
    xFmt='###0'
/>

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam

```sql umsatz
SELECT 
    *
FROM 
    agi_amtliche_vermessung.umsatz
```

<LineChart
    title='Anzahl Grenzmutationen' 
    data={umsatz}
    x=jahr
    y=anzahl_grenzmutationen
    yAxisTitle="Mutationen"
    markers=true
    xFmt='###0'
/>

<LineChart
    title='Anzahl Gebäudemutationen' 
    data={umsatz}
    x=jahr
    y=anzahl_gebaeudemutationen
    yAxisTitle="Mutationen"
    markers=true
    xFmt='###0'
/>

<LineChart
    title='Umsatz' 
    data={umsatz}
    x=jahr
    y=umsatz_in_chf
    yAxisTitle="CHF"
    markers=true
    xFmt='###0'
/>

