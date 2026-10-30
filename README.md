# hag-soda-stream 
Koden er hentet fra [flex-bigquery-soda](https://github.com/navikt/flex-bigquery-soda), og er tilpasset for team helsearbeidsgiver.

[Naisjob](https://doc.nais.io/naisjob/) for periodisk kjøring av [Soda](https://www.soda.io/)-sjekker på BigQuery-tabeller. Varsler på Slack-kanalen `#helse-arbeidsgiver-alerts-dev` for dev-miljø ved avvik.

## Utvikling

I mappen [local/](local/) ligger det filer som kan brukes til å kjøre Soda-sjekker fra lokal maskin. Sjekkene som ligger her er ikke de samme som kjøres av naisjobben, og er i all hovedsak ment for kjøring av tester i forbindelse med utvikling.


Sjekkene bruker Soda v4 Data Contracts. Naisjobben kjører NADA sitt
`nada-soda-contracts`-image, som rapporterer resultater og varsler via NADA Soda.
Hver tabell har en egen kontrakt med krav om `row_count` lik null.

Før første gang testene kjøres lokalt må poetry konfigureres:

```sh
cd local/
poetry env use 3.12
poetry install
```

Testene kan deretter kjøres med:

```sh
make run-soda-checks
```

Kontraktene ligger i `local/soda-checks/`, og datakilden i
`local/soda-config/config.yaml`. Lokalt brukes Application Default Credentials
mot dev-prosjektet. Nais-kontraktene ligger i `nais/soda-checks.yaml`, med
prosjekt-ID fra miljøets variabelfil.

## Aksjoner

Hvis noen av sjekkene som verifiser at det er streamet data til BigQuery feiler kan status på Datastreams sjekkes med:

```cmd

# Sett helsearbeidsgiver-dev som prosjekt:
gcloud config set project <prosjekt-id>

# List datastreams:
gcloud datastream streams list --location=europe-north1 | tr -s ' ' | cut -d ' '  -f1,2
```

## Avhengigheter

- [Homebrew](https://brew.sh/)

## Ressurser

- [Soda Data Contracts](https://docs.soda.io/reference/contract-language-reference)
- [NADA Soda](https://github.com/navikt/nada-soda)
