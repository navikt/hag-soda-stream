# hag-bigquery-soda
Koden er forket fra [flex-bigquery-soda](https://github.com/navikt/flex-bigquery-soda), og er tilpasset for team helsearbeidsgiver.

Bygger på [nada-soda](https://github.com/navikt/nada-soda) og er tungt inspirert av, og har stålet mye fra, [helse-styringsinfo-kvalitetssjekk](https://github.com/navikt/helse-styringsinfo-kvalitetssjekk).

[Naisjob](https://doc.nais.io/naisjob/) for periodisk kjøring av [Soda](https://www.soda.io/)-sjekker på BigQuery-tabeller. Varsler på Slack-kanalen `#flex-dev` ved avvik.

## Utvikling

I mappen [local/](local/) ligger det filer som kan brukes til å kjøre Soda-sjekker fra lokal maskin. Sjekkene som ligger her er ikke de samme som kjøres av naisjobben, og er i all hovedsak ment for kjøring av tester i forbindelse med utvikling.


Før første gang testene kjøres lokalt må poetry konfigureres:

```sh
# Sett python versjon:
poetry env use 3.12
cd local/
poetry install
```

Testene kan deretter kjøres med:

```sh
make run-soda-checks
```

## Aksjoner

Hvis noen av sjekkene som verifiser at det er streamet data til BigQuery feiler kan status på Datastreams sjekkes med:

```cmd
# Sett helsearbeidsgiver-dev som prosjekt:
gcloud config set project helsearbeidsgiver-dev-6d06

# List datastreams:
gcloud datastream streams list --location=europe-north1 | tr -s ' ' | cut -d ' '  -f1,2
```

## Avhengigheter

- [Homebrew](https://brew.sh/)

## Ressurser

- [List of SodaCL metrics and checks](https://docs.soda.io/soda-cl/metrics-and-checks.html#list-of-sodacl-metrics-and-checks)
