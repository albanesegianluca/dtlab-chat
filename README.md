# DTLAB-CHAT
[WEEK 3] Laboratorio per le lezioni degli studenti del Cisco DTLAB 2021 sui capitoli 5-6 del corso DEVASC.

## Descrizione
Utilizzando il web framework Flask, i file realizzano un semplice servizio REST con storage in memoria
di una web chat. Sono realizzate le seguenti funzionalità:
- signup e signin con email e password degli utenti;
- gli utenti possono inviare messaggi agli altri utenti identificati per email;
Documentazione del framework Flask: https://flask.palletsprojects.com/en/1.1.x/

## ESERCIZIO 1 (25 minuti)
In questo esercizio, lavoreremo sul modulo user aggiungendo la funzionalità di login.

### ESERCIZIO 1.1
In questa prima parte, configuriamo l'ambiente di sviluppo. In particolare:
* creare virtualenv;
* installare le dipendenze da requirements.txt;
* testare che il codice funzioni con Postman;

### ESERCIZIO 1.2
Creare una route '/login' che consenta agli utenti di effettuare il login con la funzione Login del modulo user.

#### HINT: si tratta di una funzione simile a quella di creazione degli utenti già presente

### ESERCIZIO 1.2
Testare le funzionalità create con Postman;

## ESERCIZIO 2 (35 minuti)
In questo esercizio, implementeremo le due funzioni fondamentali di messaggistica: invio e ricezione dei messaggi. Creeremo un modulo "message.py" che in seguito importeremo nel file server.py.

### ESERCIZIO 2.1
Creare un modulo 'message.py' con una funzione 'SaveMessage' che memorizza un messaggio.
In particolare, un messaggio deve contenere:
- mittente: id dell'utente che ha inviato il messaggio;
- destinatario: id dell'utente a cui è destinato il messaggio;
- contenuto: testo del messaggio;

#### DISCUSS: altre informazioni che possono servire. Ad esempio:
- se volessi in futuro dare la possibilità di modificare/eliminare/inoltrare un messaggio inviato, cosa mi converrebbe aggiungere?
- se volessi mostrare i messaggi di una conversazione con quale ordine li mostrerei, cosa mi converrebbe aggiungere?

#### DISCUSS: come gestiamo l'enumerazione Result? Nel codice iniziale era parte del modulo "user.py", ma adesso anche il modulo "message.py" la usa. Come facciamo a risolvere?

### ESERCIZIO 2.2
Creare una route POST "/inbox" che consenta agli utenti di inviare i messaggi ad un altro utente.

### ESERCIZIO 2.3
Creare una funzione GetMessage che consente ad un utente di ricevere tutti i messaggi diretti a lui e aggiungerla in una route GET "/inbox";
Un utente per inviare un messaggio: scrive il corpo e lo manda ad un email.
Come faccio a capire chi sta inviando la richiesta? Mi serve il suo ID per inserirlo nel campo mittente...

#### HINT: utilizzare la documentazione per capire come accedere alla variabile <id_utente>
#### DISCUSS: ma quindi tutti quelli che hanno l'ID di un utente possono leggere i suoi messaggi?

### ESERCIZIO 2.4
Testare la funzionalità creata con Postman.

## ESERCIZIO 3 (25 minuti)
In questo esercizio, ci occupiamo di creare la funzione "Elimina account". Per questioni di sicurezza, ogni utente può eliminare SOLO il proprio account. Per fare ciò, dobbiamo inviare una richiesta autenticata: ovvero inserire nell'header un campo Authorization che contenga le informazioni che ci assicurano che chi sta facendo la richiesta è autorizzato.

### ESERCIZIO 3.1
Aggiungere la route:
- DELETE /user/<id_utente>: l'utente invia email e password per cancellare il suo account:  

#### HINT 1: utilizzare la documentazione per capire come accedere all'header della richiesta ed estrarre le credenziali dalla richiesta;

Esempio
- DELETE /user/123 -> cancella utente con ID 123;

Per inviare una richiesta con autenticazione, bisogna utilizzare un "authorization header". Come abbiamo visto, gli header aggiungono ulteriori informazioni sul come trattare la richiesta; sottoforma di coppie chiave valore. Ad esempio:

**Content-Type: application/json**: indica di interpretare il contentuto del corpo della richiesta come JSON.

Utilizzando un Authorization header possiamo inviare informazioni per identificare l'utente nel sistema. Come visto in precedenza, ci sono diversi tipi di autorizzazione. Proviamo ad utilizzare la basic auth: inviamo username e password separati da ":" in base64;

Lato server, bisogna validare la richiesta verificando prima che le credenziali siano corrette e poi eseguire l'operazione. Se la convalida non va a buon fine, è buona norma ritornare "401 - Unauthorized". 

### ESERCIZIO 3.2 
Testare la funzionalità creata con Postman.

## ESERCIZIO 4 (20 minuti)
In questo esercizio, ci occupiamo di installare l'applicazione utilizzando Docker.

### ESERCIZIO 4.1
Innanzitutto dobbiamo decidere quale immagine utilizzare. Ci serve un'immagine di Python 3. Scegliamola da https://hub.docker.com

Se cerchiamo python e andiamo nella sezione tag, troviamo tantissime immagini Python, ognuna con versione e dimensione diversa. Proviamo a scegliere la versione 3.9.2 con dimensione minore. Questo sarà il punto di partenza del Dockerfile.

### ESERCIZIO 4.2
* Creiamo il Dockerfile e inseriamo come statement FROM il nome dell'immagine di scelta;
* Scegliamo una cartella dove mettere il nostro codice con lo statement WORKDIR;
* Copiamo i file del codice e installiamo le dipendenze con pip usando lo statement RUN;
* Terminiamo il file con lo statement CMD che eseguirà l'applicazione;

#### DISCUSS: se la creazione dell'immagine fallisse, dovremmo riscaricare tutte le dipendenze con l'esecuzione del comando RUN pip install ecc. Come possiamo fare per risparmiarci l'installazione delle dipendenze se modifichiamo il codice?

#### HINT: potrebbe tornare utile la feature UnionFS su cui si basano le immagini Docker;

### ESERCIZIO 4.3
Creiamo l'immagine con il comando docker build e un container con Docker Run

#### WARNING: non dimentichiamo di pubblicare la porta per raggiungere il container dall'esterno.

### ESERCIZIO 4.4 
Testiamo l'applicazione da Postman.

##  ESERCIZIO 5 (20 minuti)
In questo esercizio, creeremo una pipeline CI/CD utilizzando Jenkins.

### ESERCIZIO 5.1
In maniera del tutto analoga al laboratorio presente su netacad.com, creiamo una propria repository del codice su Github, configurare un job su Jenkins che ad ogni push esegue un rebuild dell'immagine Docker.

## EXTRA
Salvare su file gli utenti e i messaggi per avere uno storage anche non volatile.

#### WARNING: la creazione di un Docker container abilita la creazione di un layer in scrittura temporeano. Quando fermiamo un Docker Container perdiamo i file creati su di esso. Per rendere persistenti i progressi fatti da un Docker container, deve essere utilizzato un Docker Volume che esula dagli obiettivi del corso!


