---
title: Fahrzeugbestand
---

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

```sql fahrzeugbestand_grouped_by_year
SELECT 
	jahr,
	sum(anzahl) AS total
FROM 
	mfk_fahrzeugbestand.fahrzeugbestand
GROUP BY
	jahr
```

<BarChart
    title='Gesamter Fahrzeugbestand' 
    data={fahrzeugbestand_grouped_by_year}
    x=jahr
    y=total
    yAxisTitle="Anzahl Fahrzeuge"
    markers=true
    xFmt='###0'
    yMin=218000
/>

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam

```sql fahrzeugbestand_grouped_by_year_bezirk
SELECT 
	jahr,
	bezirk,
	sum(anzahl) AS total
FROM 
	mfk_fahrzeugbestand.fahrzeugbestand
GROUP BY
	jahr,
	bezirk
ORDER BY 
	jahr,
	bezirk
```

<BarChart
    title='Fahrzeugbestand pro Bezirk' 
    data={fahrzeugbestand_grouped_by_year_bezirk}
    x=jahr
    y=total
    series=bezirk
    yAxisTitle="Anzahl Fahrzeuge"
    markers=true
    xFmt='###0'
/>

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam

```sql fahrzeugbestand_typ
SELECT 
	typ
FROM 
	mfk_fahrzeugbestand.fahrzeugbestand
GROUP BY
	1
ORDER BY 
	typ
```

<Dropdown 
  data={fahrzeugbestand_typ} 
  name=typen
  value=typ
  title="Wählen Sie einen Typ"
  noDefault=true
/>


```sql fahrzeugbestand_grouped_by_year_bezirk_typ
SELECT 
	jahr,
	bezirk,
	typ,
	sum(anzahl) AS total
FROM 
	mfk_fahrzeugbestand.fahrzeugbestand
WHERE 
	typ = '${inputs.typen.value}'
GROUP BY
	jahr,
	bezirk,
	typ
ORDER BY 
	jahr,
	bezirk,
	typ
```

<LineChart
    title='Fahrzeugbestand pro Bezirk und Typ' 
    data={fahrzeugbestand_grouped_by_year_bezirk_typ}
    x=jahr
    y=total
    series=bezirk
    yAxisTitle="Anzahl Fahrzeuge"
    markers=true
    xFmt='###0'
/>

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam

```sql fahrzeugbestand_grouped_by_year_bezirk_2024
SELECT 
	jahr,
	bezirk,
	sum(anzahl) AS total
FROM 
	mfk_fahrzeugbestand.fahrzeugbestand
WHERE 
	jahr = '2024'
GROUP BY
	jahr,
	bezirk
ORDER BY 
	jahr,
	bezirk
```

<AreaMap 
    data={fahrzeugbestand_grouped_by_year_bezirk_2024} 
    areaCol=bezirk
    geoJsonUrl='/agi_bezirksgrenzen_generalisiert.geojson'
    geoId=bezirksname
    value=total
    legend=false
    showTooltip=false
    title='Fahrzeugbestand 2024'
    attribution='Kanton Solothurn'
/>


<Details title='How to edit this page'>

  This page can be found in your project at `/pages/index.md`. Make a change to the markdown file and save it to see the change take effect in your browser.
</Details>

## What's Next?
- [Connect your data sources](settings)
- Edit/add markdown files in the `pages` folder
- Deploy your project with [Evidence Cloud](https://evidence.dev/cloud)

## Get Support
- Message us on [Slack](https://slack.evidence.dev/)
- Read the [Docs](https://docs.evidence.dev/)
- Open an issue on [Github](https://github.com/evidence-dev/evidence)
