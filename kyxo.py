import spacy


EN_MODEL = ('en_core_web_md');
FR_MODEL = ('fr_core_news_md');
EN_ALPHA = "0123456789abcdefghijklmnopqrstuvwxyz-'";
FR_ALPHA = "0123456789abcdefghijklmnopqrstuvwxyz-éù'èçàîêâïôüûë";
EXTRACT_PATTERN = None;
SBT_AVR  = 1.5;
NLP      = None;
MTC      = None;
ALP      = None;

NAME    = 'KYXO'
BOLD    = '\033[01m';
BLACK   = '\033[30m';
FGC     = BOLD + BLACK ;
BGC     = '\033[47m';
RESET   = '\033[0m';


def _printf(message, **kwargs):
    print("{fg}{bg}{module} {reset} {message}".format(
        fg=FGC,
        bg=BGC,
        module=NAME,
        reset=RESET,
        message=message,
    ), **kwargs);


def default_pattern():
    wpat = {
        'IS_PUNCT': False, 
        'IS_SPACE': False,
        'IS_STOP':  False,
        'POS':      {'NOT_IN': [
            'SPACE',
            'VERB',
            'ADJ',
            'ADV',
            'AUX',
        ]},
    };
    wspat = wpat.copy();
    wspat.update({'OP': '+'});
    adppat = {'POS': 'ADP'};
    adjpat = {'POS': 'ADJ', 'OP': '?'};
    detpat = {'POS': 'DET', 'OP': '?'};

    pattern1 = [wpat, adppat, detpat, wpat];
    pattern2 = [wspat];
    pattern0 = [wpat];
    return [pattern1, pattern2, pattern0];


def init(model=FR_MODEL, alpha=FR_ALPHA):
    global NLP;
    global MTC;
    global ALP;
    global EXTRACT_PATTERN;
    
    try:
        _printf("NLP loading ...", end=' ');
        NLP = spacy.load(model);
        print("OK");

        _printf("MTC loading ...", end=' ');
        MTC = spacy.matcher.Matcher(NLP.vocab);
        print("OK");

        EXTRACT_PATTERN = default_pattern();
        ALP             = alpha;
        return NLP, MTC, EXTRACT_PATTERN;
    except Exception as e:
        _printf("ERROR ==> {}".format(e.args[0]));


def _tokok(token, alpha):
    if len(token.text) > 1:
        for c in token.text:
            if c != ' ' and c.lower() not in alpha:
                return False;
        return True;


def _reg_counts(elem, dict_):
    # Function which update the counts
    if elem in dict_: dict_[elem] += 1;
    else:             dict_[elem]  = 1;
    return dict_;


def get_keywords(text, ratio=SBT_AVR):
    global NLP;
    global MTC;
    global ALP
    global EN_ALPHA;
    global FR_ALPHA;
    global EXTRACT_PATTERN;

    try:
        if not text: return {};
        MTC.add('mmat_01', EXTRACT_PATTERN);
        doc     = NLP(text);
        matches = MTC(doc);
        counts  = {};
        # for token in tokens: print(token, token.pos_);

        # I count the token lemma
        for match_id, start, end in matches:
            span = doc[start:end];
            kws  = '';
            if _tokok(span, ALP):
                if len(span) > 1: kws = span.text;
                else:
                    dock = NLP(span.text);
                    kws  = dock[0].lemma_;

                # for token in span: print("{} \t {}".format(token.text, token.pos_));
                counts = _reg_counts(kws.lower(), counts);

        # I sorte the dict before to continue
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True));
        coun   = list(counts.values());
        if len(coun) == 0: 
            return {};

        min_ = coun[-1];
        max_ = coun[0];
        stdd = max_ - min_;     # print(stdd);
        avr  = stdd / ratio;  # print(avr);

        keywords = {};
        for token, count in counts.items():
            if count >= avr:
                keywords[token] = count;
            else:
                break;

        _printf(keywords);
        return keywords;
    except Exception as e:
        _printf("ERROR ==> {}".format(e.args[0]));
        return {};


if __name__ == '__main__':
    eg = """


L'intelligence artificielle (IA) est un processus d'imitation de l'intelligence humaine qui repose sur la création et l'application d'algorithmes exécutés dans un environnement informatique dynamique. Son but est de permettre à des ordinateurs de penser et d'agir comme des êtres humains.

Pour y parvenir, trois composants sont nécessaires :

    Des systèmes informatiques
    Des données avec des systèmes de gestion
    Des algorithmes d'IA avancés (code)

Pour se rapprocher le plus possible du comportement humain, l'intelligence artificielle a besoin d'une quantité de données et d'une capacité de traitement élevées.
Quelles sont les origines de l'intelligence artificielle ?

Depuis au moins le premier siècle avant notre ère, l'Homme s'est penché sur la création de machines capables d'imiter le raisonnement humain. Le terme « intelligence artificielle » a été créé plus récemment, en 1955 par John McCarthy. En 1956, John McCarthy et ses collaborateurs ont organisé une conférence intitulée « Dartmouth Summer Research Project on Artificial Intelligence » qui a donné naissance au machine learning, au deep learning, aux analyses prédictives et, depuis peu, aux analyses prescriptives. Un nouveau domaine d'étude est également apparu : la science des données.
Pourquoi l'intelligence artificielle est-elle importante ?

De nos jours, êtres humains et machines génèrent des données plus vite qu'il n'est humainement possible de les absorber et de les interpréter pour prendre des décisions complexes. L'intelligence artificielle est la base de tout apprentissage par un ordinateur et représente l'avenir des processus décisionnels complexes. Par exemple, la plupart des êtres humains peuvent apprendre à ne pas perdre à une simple partie de morpion, alors qu'il existe 255 168 actions possibles, dont 46 080 mènent à un match nul. En revanche, les champions du jeu de dames sont plus rares, étant donné qu'il existe plus de 500 x 1018 (500 trillions) de coups possibles. Les ordinateurs sont capables de calculer ces combinaisons et les meilleures permutations possibles très efficacement, afin de prendre la bonne décision. L'IA (avec son évolution logique, le machine learning) et le deep learning représentent l'avenir de la prise de décisions.
Utilisations de l'intelligence artificielle

L'IA est présente dans notre quotidien. Elle est par exemple utilisée par les services de détection des fraudes des établissements financiers, pour la prévision des intentions d'achat et dans les interactions avec les services clients en ligne. Voici quelques exemples : 

    Détection des fraudes. Dans le secteur de la finance, l'intelligence artificielle est utilisée de deux manières. Les applications qui notent les demandes de crédit utilisent l'IA pour évaluer la solvabilité des consommateurs. Des moteurs d'IA plus avancés sont chargés de surveiller et de détecter en temps réel les paiements frauduleux réalisés par carte bancaire.
    Service client virtuel (SCV). Les centres d'appel utilisent un SCV pour prédire les demandes de leurs clients et y répondre sans intervention humaine. La reconnaissance vocale et un simulateur de dialogue humain constituent le premier point d'interaction avec le service client. Les demandes plus complexes requièrent quant à elles une intervention humaine.
    Lorsqu'un internaute ouvre une fenêtre de dialogue sur une page web (chatbot), son interlocuteur est souvent un ordinateur exécutant une forme d'IA spécialisée. Si le chatbot ne parvient pas à interpréter la question ou à résoudre le problème, un agent humain prend le relais. Ces échecs d'interprétation sont envoyés au système de machine learning afin d'améliorer les futures interactions de l'application d'IA.

NetApp et l'intelligence artificielle

En tant que référence en matière de gestion de données dans le cloud hybride, NetApp comprend l'importance de l'accès aux données, de leur gestion et de leur contrôle. NetApp® Data Fabric fournit un environnement de gestion unifiée des données qui couvre les terminaux, les data centers et plusieurs clouds hyperscale. Il permet aux entreprises, quelle que soit leur taille, d'accélérer les applications stratégiques, d'améliorer la visibilité sur les données, d'en optimiser la protection et d'améliorer l'agilité fonctionnelle.

Les solutions d'IA de NetApp reposent sur des composants de base clés : 

    Le logiciel ONTAP® permet d'exploiter l'IA et le deep learning localement et dans le cloud hybride.
    Les systèmes FAS 100 % Flash accélèrent les workloads d'IA et de deep learning, tout en éliminant les goulots d'étranglement qui affectent les performances.
    Le logiciel ONTAP Select permet de collecter les données efficacement à la périphérie à l'aide de terminaux IoT et de points d'agrégation.
    Cloud Volumes peut être utilisé pour créer rapidement des prototypes pour de nouveaux projets. Il permet de recevoir et d'envoyer des données d'IA depuis et vers le cloud.

NetApp a également commencé à intégrer l'analytique Big Data et l'intelligence artificielle dans ses propres produits et services, notamment avec Active IQ®, qui utilise des milliards de points de données, l'analyse prédictive et un moteur puissant de machine learning afin de proposer des recommandations proactives de support client pour les environnements IT complexes. Active IQ est une application de cloud hybride conçue à l'aide des mêmes produits et technologies NetApp que nos clients utilisent pour créer leurs solutions d'IA dans plusieurs domaines.

"""
    init(FR_MODEL, FR_ALPHA);
    ks = get_keywords(eg);
    # for k in ks: print(k);

    
