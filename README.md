# p-afin_stats_teaser

## data

Bemerkungen:

- Whitespaces in Dateinamen
- Wahrscheinlich aus Excel exportiert -> exotisches Encoding. Es gibt einen UTF-8-CSV-Export in Excel.
- Datentypen werden geraten
- https://github.com/openZH/ogd-handbook/blob/main/publikationsleitlinien.md
- https://github.com/openZH/ogd-handbook/blob/main/publikationsleitlinien/xls-zu-csv-konvertieren.md
- Immer gleiche Werte sollten "Aufzähltypen" sein.
- Header wird beim Export trotz FORCE_QUOTE nicht gequoted. Müsste man schauen wegen iox-reader.
- Tsüri empfiehlt "long" (so wie ichs verstehe): https://github.com/openZH/ogd-handbook/blob/main/publikationsleitlinien/warum_tidy_data.md https://r4ds.hadley.nz/data-tidy.html
- Eventuell https://motherduck.com/blog/from-data-lake-to-lakehouse-duckdb-portable-catalog/ für duckdb-Katalog mit allen Parquet-Dateien geviewed. Dann kann man immer die gleiche DuckDB in evidence verwenden.



```
./duckdb ch.so.mfk.fahrzeugbestand.duckdb

CREATE TABLE mfk_fahrzeugbestand AS
    SELECT * FROM '/Users/stefan/sources/p-afin_stats_teaser/data/ch.so.mfk.fahrzeugbestand_1990-2024.parquet';
```




```
npx degit evidence-dev/template my-project
cd my-project
npm install
npm run sources
npm run dev
```