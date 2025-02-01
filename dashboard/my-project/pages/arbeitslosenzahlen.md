---
title: Arbeitslosenzahlen
---

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

```sql stellensuchende
SELECT 
	*
FROM 
	awa_arbeitslosenzahlen_stellensuchende.arbeitslosenzahlen_stellensuchende
```

```sql years
SELECT 
	jahr
FROM 
	awa_arbeitslosenzahlen_stellensuchende.arbeitslosenzahlen_stellensuchende
GROUP BY 
  1
```

<Dropdown 
  data={years} 
  name=jahre
  value=jahr
  title="Wählen Sie ein Jahr aus"
/>


```sql stellensuchende_diff_last_year
SELECT 
	a.jahr,
	a.total AS atotal,
	b.total AS btotal,
	CASE 
		WHEN b.total IS NOT NULL THEN ((a.total - b.total) * 1.0 / b.total)
		ELSE NULL
	END AS adiff
FROM 
(
	SELECT 
		jahr,
		sum(anzahl) AS total
	FROM 
	  awa_arbeitslosenzahlen_stellensuchende.arbeitslosenzahlen_stellensuchende
	WHERE 
		jahr = '${inputs.jahre.value}'
		AND 
		(kategorie = 'Stellensuchende Männer' OR kategorie = 'Stellensuchende Frauen')
	GROUP BY
		jahr
) AS a
JOIN 
(
	SELECT 
		jahr,
		sum(anzahl) AS total
	FROM 
	  awa_arbeitslosenzahlen_stellensuchende.arbeitslosenzahlen_stellensuchende
	WHERE 
		jahr = ( cast('${inputs.jahre.value}' AS int) - 1 )
		AND 
		(kategorie = 'Stellensuchende Männer' OR kategorie = 'Stellensuchende Frauen')
	GROUP BY
		jahr

) AS b
ON 1=1
```

<BigValue 
  data={stellensuchende_diff_last_year}
  title="Stellensuchende Total" 
  value=atotal
  fmt='###0'
  comparison=adiff
  comparisonFmt=pct1
  comparisonTitle="vs. Vorjahr"
/>


```sql stellensuchende_male_female
SELECT 
	jahr,
	kategorie,
	anzahl
FROM 
	awa_arbeitslosenzahlen_stellensuchende.arbeitslosenzahlen_stellensuchende
WHERE 
	jahr = '${inputs.jahre.value}'
	AND 
	(kategorie = 'Stellensuchende Männer' OR kategorie = 'Stellensuchende Frauen')
```

```sql pie_data
select kategorie as name, anzahl as value
from ${stellensuchende_male_female}
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam

<ECharts title='fubar' config={
    {
        title: {
          text: 'Stellensuchende Männer vs Frauen'
        },
        tooltip: {
            formatter: '{b}: {c} ({d}%)'
        },
        series: [
        {
          type: 'pie',
          data: [...pie_data],
          color: ['#00b04f', '#ffbf00', 'ff0000']
        }
      ]
      }
    }
/>

