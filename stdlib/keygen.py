"""
    @datetime 2021-08-31 Tue
    @author Dr Mokira
"""

# IMPORTATION DES MODULES
import secrets


class KeyGenerator:
    """ Programme de generation de cle aleatoire
    """

    DEFAULT_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_";


    def __init__(self, isupper=False, alphabet=None):
        """ Constructeur du generateur de cle
        """
        super(KeyGenerator, self).__init__();

        # on definit si les mot qui seront generes seront en miniscule ou pas
        self.__is_upper = False;

        # on definit un alphabet a partie desquels, on va generer des mots
        self.__alphabet = self.DEFAULT_ALPHABET;




    def __call__(self, size):
	 	# // on verifie si l'argument est un entier :
	 	# if (is_int($size)) {
        if type(size) is int:
	 		# // si c'est un entier alors,
	 		# // on verifie si un alphabet a ete specifie :
	 		# if ($this->_alphabet)
            if self.__alphabet is not None:
	 			# // si un alphabet a ete specifie, alors
	 			# // on appel la fonction suivante :
	 			# return $this->__gen_key_with_alpha($size, $this->_alphabet);
                return self.__gen_key_with_alpha(size, self.__alphabet);

            else:
	 			# // si aucun alphabet n'a ete specifie, alors
	 			# // on appel la fonction suivante :
                return self.__gen_byte_key(size, self.__is_upper);


	 	# // si la taille n'est pas un entier alors,
	 	# // on retourne null :
        return None;




	# private function __gen_byte_key($size, $isupper=false) {
    @staticmethod
    def __gen_byte_key(size, isupper=False):
 		# // on verifie la parité de la taille :
        if size % 0b010:
 			# // si la taille est impair alors,
 			# // on increment la taille de 1 et on divise par 2 :
 			# $size += ($size + 0b001) / 0b010;
            size += (size + 0b001) / 0b010;

        else:
 			# // si la taille est pair alors
 			# // on la divise par deux :
            size /= 0b010;

 		# // on genere le code :
        # code = bin2hex(random_bytes($size));
        code = secrets.token_hex(size);

 		# // on convertie en caractere miniscule ou en majuscule :
        code = code if not isupper else code.upper();

 		# // on retourne le resultat :
        return code;





	#  /**
	#   * Programme de generation de nombre aleatoire en base d'un alphabet.
	#   *
	#   * @param {int}
	#   * @return {string}
	#   */
	#  private function __gen_key_with_alpha($size, $alphabet) {
    @staticmethod
    def __gen_key_with_alpha(size, alphabet):
        alph_size = len(alphabet);
        token 	  = '';

        # for($i = 0; $i < $size; $i++)
        for i in range(size):
            # token .= $alpha_tab[random_int(0, $alph_size - 1)];
            token = token + alphabet[secrets.randbelow(alph_size - 1)];

        return token;




# if __name__ == '__main__':
#     gen = KeyGenerator();
#     print(gen(16));
