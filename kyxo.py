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


def get_keywords(text):
    global NLP;
    global MTC;
    global ALP
    global EN_ALPHA;
    global FR_ALPHA;
    global EXTRACT_PATTERN;

    try:
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
            return [];

        min_ = coun[-1];
        max_ = coun[0];
        stdd = max_ - min_;     # print(stdd);
        avr  = stdd / SBT_AVR;  # print(avr);

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
        return [];


if __name__ == '__main__':
    eg = """
Un réseau de télévision est un réseau de télécommunications destiné à la distribution de programmes télévisés. Cependant, le terme désigne désormais un groupement d'affiliés régionaux autour d'une chaîne de télévision centrale, offrant une programmation à plusieurs stations de télévision locales.

Jusqu'au milieu des années 1980, la programmation télévisée de la plupart des pays du monde a été dominée par un petit nombre de réseaux de diffusion. Bon nombre des premiers réseaux de télévision (comme la BBC, NBC ou CBS) se sont développés à partir de réseaux de radio existants. 
"""
    init(FR_MODEL, FR_ALPHA);
    ks = get_keywords(eg);
    # for k in ks: print(k);

    
