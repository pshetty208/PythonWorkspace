{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "60cfd85a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['ONCE', 'there', 'was', 'a', 'gentleman', 'who', 'married,', 'for', 'his', 'second', 'wife,', 'the', 'proudest', 'and', 'most', 'haughty', 'woman', 'that', 'was', 'ever', 'seen.', 'She', 'had,', 'by', 'a', 'former', 'husband,', 'two', 'daughters', 'of', 'her', 'own', 'humor,', 'who', 'were,', 'indeed,', 'exactly', 'like', 'her', 'in', 'all', 'things.', 'He', 'had', 'likewise,', 'by', 'another', 'wife,', 'a', 'young', 'daughter,', 'but', 'of', 'unparalleled', 'goodness', 'and', 'sweetness', 'of', 'temper,', 'which', 'she', 'took', 'from', 'her', 'mother,', 'who', 'was', 'the', 'best', 'creature', 'in', 'the', 'world.', 'No', 'sooner', 'were', 'the', 'ceremonies', 'of', 'the', 'wedding', 'over', 'but', 'the', 'mother-in-law', 'began', 'to', 'show', 'herself', 'in', 'her', 'true', 'colors.', 'She', 'could', 'not', 'bear', 'the', 'good', 'qualities', 'of', 'this', 'pretty', 'girl,', 'and', 'the', 'less', 'because', 'they', 'made', 'her', 'own', 'daughters', 'appear', 'the', 'more', 'odious.', 'She', 'employed', 'her', 'in', 'the', 'meanest', 'work', 'of', 'the', 'house:', 'she', 'scoured', 'the', 'dishes,', 'tables,', 'etc.,', 'and', 'scrubbed', \"madam's\", 'chamber,', 'and', 'those', 'of', 'misses,', 'her', 'daughters;', 'she', 'lay', 'up', 'in', 'a', 'sorry', 'garret,', 'upon', 'a', 'wretched', 'straw', 'bed,', 'while', 'her', 'sisters', 'lay', 'in', 'fine', 'rooms,', 'with', 'floors', 'all', 'inlaid,', 'upon', 'beds', 'of', 'the', 'very', 'newest', 'fashion,', 'and', 'where', 'they', 'had', 'looking-glasses', 'so', 'large', 'that', 'they', 'might', 'see', 'themselves', 'at', 'their', 'full', 'length', 'from', 'head', 'to', 'foot.', 'The', 'poor', 'girl', 'bore', 'all', 'patiently,', 'and', 'dared', 'not', 'tell', 'her', 'father,', 'who', 'would', 'have', 'rattled', 'her', 'off;', 'for', 'his', 'wife', 'governed', 'him', 'entirely.', 'When', 'she', 'had', 'done', 'her', 'work,', 'she', 'used', 'to', 'go', 'into', 'the', 'chimney-corner,', 'and', 'sit', 'down', 'among', 'cinders', 'and', 'ashes,', 'which', 'made', 'her', 'commonly', 'be', 'called', 'Cinderwench;', 'but', 'the', 'youngest,', 'who', 'was', 'not', 'so', 'rude', 'and', 'uncivil', 'as', 'the', 'eldest,', 'called', 'her', 'Cinderella.', 'However,', 'Cinderella,', 'notwithstanding', 'her', 'mean', 'apparel,', 'was', 'a', 'hundred', 'times', 'handsomer', 'than', 'her', 'sisters,', 'though', 'they', 'were', 'always', 'dressed', 'very', 'richly.', 'It', 'happened', 'that', 'the', \"King's\", 'son', 'gave', 'a', 'ball,', 'and', 'invited', 'all', 'persons', 'of', 'fashion', 'to', 'it.', 'Our', 'young', 'misses', 'were', 'also', 'invited,', 'for', 'they', 'cut', 'a', 'very', 'grand', 'figure', 'among', 'the', 'quality.', 'They', 'were', 'mightily', 'delighted', 'at', 'this', 'invitation,', 'and', 'wonderfully', 'busy', 'in', 'choosing', 'out', 'such', 'gowns,', 'petticoats,', 'and', 'head-clothes', 'as', 'might', 'become', 'them.', 'This', 'was', 'a', 'new', 'trouble', 'to', 'Cinderella;', 'for', 'it', 'was', 'she', 'who', 'ironed', 'her', \"sisters'\", 'linen,', 'and', 'plaited', 'their', 'ruffles;', 'they', 'talked', 'all', 'day', 'long', 'of', 'nothing', 'but', 'how', 'they', 'should', 'be', 'dressed.', '\"For', 'my', 'part,\"', 'said', 'the', 'eldest,', '\"I', 'will', 'wear', 'my', 'red', 'velvet', 'suit', 'with', 'French', 'trimming.\"', '\"And', 'I,\"', 'said', 'the', 'youngest,', '\"shall', 'have', 'my', 'usual', 'petticoat;', 'but', 'then,', 'to', 'make', 'amends', 'for', 'that,', 'I', 'will', 'put', 'on', 'my', 'gold-flowered', 'manteau,', 'and', 'my', 'diamond', 'stomacher,', 'which', 'is', 'far', 'from', 'being', 'the', 'most', 'ordinary', 'one', 'in', 'the', 'world.\"', 'They', 'sent', 'for', 'the', 'best', 'tire-woman', 'they', 'could', 'get', 'to', 'make', 'up', 'their', 'head-dresses', 'and', 'adjust', 'their', 'double', 'pinners,', 'and', 'they', 'had', 'their', 'red', 'brushes', 'and', 'patches', 'from', 'Mademoiselle', 'de', 'la', 'Poche.', 'Cinderella', 'was', 'likewise', 'called', 'up', 'to', 'them', 'to', 'be', 'consulted', 'in', 'all', 'these', 'matters,', 'for', 'she', 'had', 'excellent', 'notions,', 'and', 'advised', 'them', 'always', 'for', 'the', 'best,', 'nay,', 'and', 'offered', 'her', 'services', 'to', 'dress', 'their', 'heads,', 'which', 'they', 'were', 'very', 'willing', 'she', 'should', 'do.', 'As', 'she', 'was', 'doing', 'this,', 'they', 'said', 'to', 'her:', '\"Cinderella,', 'would', 'you', 'not', 'be', 'glad', 'to', 'go', 'to', 'the', 'ball?\"', '\"Alas!\"', 'said', 'she,', '\"you', 'only', 'jeer', 'me;', 'it', 'is', 'not', 'for', 'such', 'as', 'I', 'am', 'to', 'go', 'thither.\"', '\"Thou', 'art', 'in', 'the', 'right', 'of', 'it,\"', 'replied', 'they;', '\"it', 'would', 'make', 'the', 'people', 'laugh', 'to', 'see', 'a', 'Cinderwench', 'at', 'a', 'ball.\"', 'Anyone', 'but', 'Cinderella', 'would', 'have', 'dressed', 'their', 'heads', 'awry,', 'but', 'she', 'was', 'very', 'good,', 'and', 'dressed', 'them', 'perfectly', 'well', 'They', 'were', 'almost', 'two', 'days', 'without', 'eating,', 'so', 'much', 'were', 'they', 'transported', 'with', 'joy.', 'They', 'broke', 'above', 'a', 'dozen', 'laces', 'in', 'trying', 'to', 'be', 'laced', 'up', 'close,', 'that', 'they', 'might', 'have', 'a', 'fine', 'slender', 'shape,', 'and', 'they', 'were', 'continually', 'at', 'their', 'looking-glass.', 'At', 'last', 'the', 'happy', 'day', 'came;', 'they', 'went', 'to', 'Court,', 'and', 'Cinderella', 'followed', 'them', 'with', 'her', 'eyes', 'as', 'long', 'as', 'she', 'could,', 'and', 'when', 'she', 'had', 'lost', 'sight', 'of', 'them,', 'she', 'fell', 'a-crying.', 'Her', 'godmother,', 'who', 'saw', 'her', 'all', 'in', 'tears,', 'asked', 'her', 'what', 'was', 'the', 'matter.', '\"I', 'wish', 'I', 'could--I', 'wish', 'I', 'could--\";', 'she', 'was', 'not', 'able', 'to', 'speak', 'the', 'rest,', 'being', 'interrupted', 'by', 'her', 'tears', 'and', 'sobbing.', 'This', 'godmother', 'of', 'hers,', 'who', 'was', 'a', 'fairy,', 'said', 'to', 'her,', '\"Thou', 'wishest', 'thou', 'couldst', 'go', 'to', 'the', 'ball;', 'is', 'it', 'not', 'so?\"', '\"Y--es,\"', 'cried', 'Cinderella,', 'with', 'a', 'great', 'sigh.', '\"Well,\"', 'said', 'her', 'godmother,', '\"be', 'but', 'a', 'good', 'girl,', 'and', 'I', 'will', 'contrive', 'that', 'thou', 'shalt', 'go.\"', 'Then', 'she', 'took', 'her', 'into', 'her', 'chamber,', 'and', 'said', 'to', 'her,', '\"Run', 'into', 'the', 'garden,', 'and', 'bring', 'me', 'a', 'pumpkin.\"', 'Cinderella', 'went', 'immediately', 'to', 'gather', 'the', 'finest', 'she', 'could', 'get,', 'and', 'brought', 'it', 'to', 'her', 'godmother,', 'not', 'being', 'able', 'to', 'imagine', 'how', 'this', 'pumpkin', 'could', 'make', 'her', 'go', 'to', 'the', 'ball.', 'Her', 'godmother', 'scooped', 'out', 'all', 'the', 'inside', 'of', 'it,', 'having', 'left', 'nothing', 'but', 'the', 'rind;', 'which', 'done,', 'she', 'struck', 'it', 'with', 'her', 'wand,', 'and', 'the', 'pumpkin', 'was', 'instantly', 'turned', 'into', 'a', 'fine', 'coach,', 'gilded', 'all', 'over', 'with', 'gold.', 'She', 'then', 'went', 'to', 'look', 'into', 'her', 'mouse-trap,', 'where', 'she', 'found', 'six', 'mice,', 'all', 'alive,', 'and', 'ordered', 'Cinderella', 'to', 'lift', 'up', 'a', 'little', 'the', 'trapdoor,', 'when,', 'giving', 'each', 'mouse,', 'as', 'it', 'went', 'out,', 'a', 'little', 'tap', 'with', 'her', 'wand,', 'the', 'mouse', 'was', 'that', 'moment', 'turned', 'into', 'a', 'fine', 'horse,', 'which', 'altogether', 'made', 'a', 'very', 'fine', 'set', 'of', 'six', 'horses', 'of', 'a', 'beautiful', 'mouse-colored', 'dapple-gray.', 'Being', 'at', 'a', 'loss', 'for', 'a', 'coachman,', '\"I', 'will', 'go', 'and', 'see,\"', 'says', 'Cinderella,', '\"if', 'there', 'is', 'never', 'a', 'rat', 'in', 'the', 'rat-trap--we', 'may', 'make', 'a', 'coachman', 'of', 'him.\"', '\"Thou', 'art', 'in', 'the', 'right,\"', 'replied', 'her', 'godmother;', '\"go', 'and', 'look.\"', 'Cinderella', 'brought', 'the', 'trap', 'to', 'her,', 'and', 'in', 'it', 'there', 'were', 'three', 'huge', 'rats.', 'The', 'fairy', 'made', 'choice', 'of', 'one', 'of', 'the', 'three', 'which', 'had', 'the', 'largest', 'beard,', 'and,', 'having', 'touched', 'him', 'with', 'her', 'wand,', 'he', 'was', 'turned', 'into', 'a', 'fat,', 'jolly', 'coach-', 'man,', 'who', 'had', 'the', 'smartest', 'whiskers', 'eyes', 'ever', 'beheld.', 'After', 'that,', 'she', 'said', 'to', 'her:', '\"Go', 'again', 'into', 'the', 'garden,', 'and', 'you', 'will', 'find', 'six', 'lizards', 'behind', 'the', 'watering-pot,', 'bring', 'them', 'to', 'me.\"', 'She', 'had', 'no', 'sooner', 'done', 'so', 'but', 'her', 'godmother', 'turned', 'them', 'into', 'six', 'footmen,', 'who', 'skipped', 'up', 'immediately', 'behind', 'the', 'coach,', 'with', 'their', 'liveries', 'all', 'bedaubed', 'with', 'gold', 'and', 'silver,', 'and', 'clung', 'as', 'close', 'behind', 'each', 'other', 'as', 'if', 'they', 'had', 'done', 'nothing', 'else', 'their', 'whole', 'lives.', 'The', 'Fairy', 'then', 'said', 'to', 'Cinderella:', '\"Well,', 'you', 'see', 'here', 'an', 'equipage', 'fit', 'to', 'go', 'to', 'the', 'ball', 'with;', 'are', 'you', 'not', 'pleased', 'with', 'it?\"', '\"Oh!', 'yes,\"', 'cried', 'she;', '\"but', 'must', 'I', 'go', 'thither', 'as', 'I', 'am,', 'in', 'these', 'nasty', 'rags?\"', 'Her', 'godmother', 'only', 'just', 'touched', 'her', 'with', 'her', 'wand,', 'and,', 'at', 'the', 'same', 'instant,', 'her', 'clothes', 'were', 'turned', 'into', 'cloth', 'of', 'gold', 'and', 'silver,', 'all', 'beset', 'with', 'jewels.', 'This', 'done,', 'she', 'gave', 'her', 'a', 'pair', 'of', 'glass', 'slippers,', 'the', 'prettiest', 'in', 'the', 'whole', 'world.', 'Being', 'thus', 'decked', 'out,', 'she', 'got', 'up', 'into', 'her', 'coach;', 'but', 'her', 'godmother,', 'above', 'all', 'things,', 'commanded', 'her', 'not', 'to', 'stay', 'till', 'after', 'midnight,', 'telling', 'her,', 'at', 'the', 'same', 'time,', 'that', 'if', 'she', 'stayed', 'one', 'moment', 'longer,', 'the', 'coach', 'would', 'be', 'a', 'pumpkin', 'again,', 'her', 'horses', 'mice,', 'her', 'coachman', 'a', 'rat,', 'her', 'footmen', 'lizards,', 'and', 'her', 'clothes', 'become', 'just', 'as', 'they', 'were', 'before.', 'She', 'promised', 'her', 'godmother', 'she', 'would', 'not', 'fail', 'of', 'leaving', 'the', 'ball', 'before', 'midnight;', 'and', 'then', 'away', 'she', 'drives,', 'scarce', 'able', 'to', 'contain', 'herself', 'for', 'joy.', 'The', \"King's\", 'son', 'who', 'was', 'told', 'that', 'a', 'great', 'princess,', 'whom', 'nobody', 'knew,', 'was', 'come,', 'ran', 'out', 'to', 'receive', 'her;', 'he', 'gave', 'her', 'his', 'hand', 'as', 'she', 'alighted', 'out', 'of', 'the', 'coach,', 'and', 'led', 'her', 'into', 'the', 'ball,', 'among', 'all', 'the', 'company.', 'There', 'was', 'immediately', 'a', 'profound', 'silence,', 'they', 'left', 'off', 'dancing,', 'and', 'the', 'violins', 'ceased', 'to', 'play,', 'so', 'attentive', 'was', 'everyone', 'to', 'contemplate', 'the', 'singular', 'beauties', 'of', 'the', 'unknown', 'new-comer.', 'Nothing', 'was', 'then', 'heard', 'but', 'a', 'confused', 'noise', 'of:', '\"Ha!', 'how', 'handsome', 'she', 'is!', 'Ha!', 'how', 'handsome', 'she', 'is!\"', 'The', 'King', 'himself,', 'old', 'as', 'he', 'was,', 'could', 'not', 'help', 'watching', 'her,', 'and', 'telling', 'the', 'Queen', 'softly', 'that', 'it', 'was', 'a', 'long', 'time', 'since', 'he', 'had', 'seen', 'so', 'beautiful', 'and', 'lovely', 'a', 'creature.', 'All', 'the', 'ladies', 'were', 'busied', 'in', 'considering', 'her', 'clothes', 'and', 'headdress,', 'that', 'they', 'might', 'have', 'some', 'made', 'next', 'day', 'after', 'the', 'same', 'pattern,', 'provided', 'they', 'could', 'meet', 'with', 'such', 'fine', 'material', 'and', 'as', 'able', 'hands', 'to', 'make', 'them.', 'The', \"King's\", 'son', 'conducted', 'her', 'to', 'the', 'most', 'honorable', 'seat,', 'and', 'afterward', 'took', 'her', 'out', 'to', 'dance', 'with', 'him;', 'she', 'danced', 'so', 'very', 'gracefully', 'that', 'they', 'all', 'more', 'and', 'more', 'admired', 'her.', 'A', 'fine', 'collation', 'was', 'served', 'up,', 'whereof', 'the', 'young', 'prince', 'ate', 'not', 'a', 'morsel,', 'so', 'intently', 'was', 'he', 'busied', 'in', 'gazing', 'on', 'her.', 'She', 'went', 'and', 'sat', 'down', 'by', 'her', 'sisters,', 'showing', 'them', 'a', 'thousand', 'civilities,', 'giving', 'them', 'part', 'of', 'the', 'oranges', 'and', 'citrons', 'which', 'the', 'Prince', 'had', 'presented', 'her', 'with,', 'which', 'very', 'much', 'surprised', 'them,', 'for', 'they', 'did', 'not', 'know', 'her.', 'While', 'Cinderella', 'was', 'thus', 'amusing', 'her', 'sisters,', 'she', 'heard', 'the', 'clock', 'strike', 'eleven', 'and', 'three-quarters,', 'whereupon', 'she', 'immediately', 'made', 'a', 'courtesy', 'to', 'the', 'company', 'and', 'hasted', 'away', 'as', 'fast', 'as', 'she', 'could.', 'When', 'she', 'got', 'home', 'she', 'ran', 'to', 'seek', 'out', 'her', 'godmother,', 'and,', 'after', 'having', 'thanked', 'her,', 'she', 'said', 'she', 'could', 'not', 'but', 'heartily', 'wish', 'she', 'might', 'go', 'next', 'day', 'to', 'the', 'ball,', 'because', 'the', \"King's\", 'son', 'had', 'desired', 'her.', 'As', 'she', 'was', 'eagerly', 'telling', 'her', 'godmother', 'whatever', 'had', 'passed', 'at', 'the', 'ball,', 'her', 'two', 'sisters', 'knocked', 'at', 'the', 'door,', 'which', 'Cinderella', 'ran', 'and', 'opened.', '\"How', 'long', 'you', 'have', 'stayed!\"', 'cried', 'she,', 'gaping,', 'rubbing', 'her', 'eyes', 'and', 'stretching', 'herself', 'as', 'if', 'she', 'had', 'been', 'just', 'waked', 'out', 'of', 'her', 'sleep;', 'she', 'had', 'not,', 'however,', 'any', 'manner', 'of', 'inclination', 'to', 'sleep', 'since', 'they', 'went', 'from', 'home.', '\"If', 'thou', 'hadst', 'been', 'at', 'the', 'ball,\"', 'said', 'one', 'of', 'her', 'sisters,', '\"thou', 'wouldst', 'not', 'have', 'been', 'tired', 'with', 'it.', 'There', 'came', 'thither', 'the', 'finest', 'princess,', 'the', 'most', 'beautiful', 'ever', 'was', 'seen', 'with', 'mortal', 'eyes;', 'she', 'showed', 'us', 'a', 'thousand', 'civilities,', 'and', 'gave', 'us', 'oranges', 'and', 'citrons.\"', 'Cinderella', 'seemed', 'very', 'indifferent', 'in', 'the', 'matter;', 'indeed,', 'she', 'asked', 'them', 'the', 'name', 'of', 'that', 'princess;', 'but', 'they', 'told', 'her', 'they', 'did', 'not', 'know', 'it,', 'and', 'that', 'the', \"King's\", 'son', 'was', 'very', 'uneasy', 'on', 'her', 'account', 'and', 'would', 'give', 'all', 'the', 'world', 'to', 'know', 'who', 'she', 'was.', 'At', 'this', 'Cinderella,', 'smiling,', 'replied:', '\"She', 'must,', 'then,', 'be', 'very', 'beautiful', 'indeed;', 'how', 'happy', 'you', 'have', 'been!', 'Could', 'not', 'I', 'see', 'her?', 'Ah!', 'dear', 'Miss', 'Charlotte,', 'do', 'lend', 'me', 'your', 'yellow', 'suit', 'of', 'clothes', 'which', 'you', 'wear', 'every', 'day.\"', '\"Ay,', 'to', 'be', 'sure!\"', 'cried', 'Miss', 'Charlotte;', '\"lend', 'my', 'clothes', 'to', 'such', 'a', 'dirty', 'Cinderwench', 'as', 'thou', 'art!', 'I', 'should', 'be', 'a', 'fool.\"', 'Cinderella,', 'indeed,', 'expected', 'well', 'such', 'answer,', 'and', 'was', 'very', 'glad', 'of', 'the', 'refusal;', 'for', 'she', 'would', 'have', 'been', 'sadly', 'put', 'to', 'it', 'if', 'her', 'sister', 'had', 'lent', 'her', 'what', 'she', 'asked', 'for', 'jestingly.', 'The', 'next', 'day', 'the', 'two', 'sisters', 'were', 'at', 'the', 'ball,', 'and', 'so', 'was', 'Cinderella,', 'but', 'dressed', 'more', 'magnificently', 'than', 'before.', 'The', \"King's\", 'son', 'was', 'always', 'by', 'her,', 'and', 'never', 'ceased', 'his', 'compliments', 'and', 'kind', 'speeches', 'to', 'her;', 'to', 'whom', 'all', 'this', 'was', 'so', 'far', 'from', 'being', 'tiresome', 'that', 'she', 'quite', 'forgot', 'what', 'her', 'godmother', 'had', 'recommended', 'to', 'her;', 'so', 'that', 'she,', 'at', 'last,', 'counted', 'the', 'clock', 'striking', 'twelve', 'when', 'she', 'took', 'it', 'to', 'be', 'no', 'more', 'than', 'eleven;', 'she', 'then', 'rose', 'up', 'and', 'fled,', 'as', 'nimble', 'as', 'a', 'deer.', 'The', 'Prince', 'followed,', 'but', 'could', 'not', 'overtake', 'her.', 'She', 'left', 'behind', 'one', 'of', 'her', 'glass', 'slippers,', 'which', 'the', 'Prince', 'took', 'up', 'most', 'carefully.', 'She', 'got', 'home', 'but', 'quite', 'out', 'of', 'breath,', 'and', 'in', 'her', 'nasty', 'old', 'clothes,', 'having', 'nothing', 'left', 'her', 'of', 'all', 'her', 'finery', 'but', 'one', 'of', 'the', 'little', 'slippers,', 'fellow', 'to', 'that', 'she', 'dropped.', 'The', 'guards', 'at', 'the', 'palace', 'gate', 'were', 'asked:', 'If', 'they', 'had', 'not', 'seen', 'a', 'princess', 'go', 'out.', 'Who', 'said:', 'They', 'had', 'seen', 'nobody', 'go', 'out', 'but', 'a', 'young', 'girl,', 'very', 'meanly', 'dressed,', 'and', 'who', 'had', 'more', 'the', 'air', 'of', 'a', 'poor', 'country', 'wench', 'than', 'a', 'gentlewoman.', 'When', 'the', 'two', 'sisters', 'returned', 'from', 'the', 'ball', 'Cinderella', 'asked', 'them:', 'If', 'they', 'had', 'been', 'well', 'diverted,', 'and', 'if', 'the', 'fine', 'lady', 'had', 'been', 'there.', 'They', 'told', 'her:', 'Yes,', 'but', 'that', 'she', 'hurried', 'away', 'immediately', 'when', 'it', 'struck', 'twelve,', 'and', 'with', 'so', 'much', 'haste', 'that', 'she', 'dropped', 'one', 'of', 'her', 'little', 'glass', 'slippers,', 'the', 'prettiest', 'in', 'the', 'world,', 'which', 'the', \"King's\", 'son', 'had', 'taken', 'up;', 'that', 'he', 'had', 'done', 'nothing', 'but', 'look', 'at', 'her', 'all', 'the', 'time', 'at', 'the', 'ball,', 'and', 'that', 'most', 'certainly', 'he', 'was', 'very', 'much', 'in', 'love', 'with', 'the', 'beautiful', 'person', 'who', 'owned', 'the', 'glass', 'slipper.', 'What', 'they', 'said', 'was', 'very', 'true;', 'for', 'a', 'few', 'days', 'after', 'the', \"King's\", 'son', 'caused', 'it', 'to', 'be', 'proclaimed,', 'by', 'sound', 'of', 'trumpet,', 'that', 'he', 'would', 'marry', 'her', 'whose', 'foot', 'the', 'slipper', 'would', 'just', 'fit.', 'They', 'whom', 'he', 'employed', 'began', 'to', 'try', 'it', 'upon', 'the', 'princesses,', 'then', 'the', 'duchesses', 'and', 'all', 'the', 'Court,', 'but', 'in', 'vain;', 'it', 'was', 'brought', 'to', 'the', 'two', 'sisters,', 'who', 'did', 'all', 'they', 'possibly', 'could', 'to', 'thrust', 'their', 'foot', 'into', 'the', 'slipper,', 'but', 'they', 'could', 'not', 'effect', 'it.', 'Cinderella,', 'who', 'saw', 'all', 'this,', 'and', 'knew', 'her', 'slipper,', 'said', 'to', 'them,', 'laughing:', '\"Let', 'me', 'see', 'if', 'it', 'will', 'not', 'fit', 'me.\"', 'Her', 'sisters', 'burst', 'out', 'a-laughing,', 'and', 'began', 'to', 'banter', 'her.', 'The', 'gentleman', 'who', 'was', 'sent', 'to', 'try', 'the', 'slipper', 'looked', 'earnestly', 'at', 'Cinderella,', 'and,', 'finding', 'her', 'very', 'handsome,', 'said:', 'It', 'was', 'but', 'just', 'that', 'she', 'should', 'try,', 'and', 'that', 'he', 'had', 'orders', 'to', 'let', 'everyone', 'make', 'trial.', 'He', 'obliged', 'Cinderella', 'to', 'sit', 'down,', 'and,', 'putting', 'the', 'slipper', 'to', 'her', 'foot,', 'he', 'found', 'it', 'went', 'on', 'very', 'easily,', 'and', 'fitted', 'her', 'as', 'if', 'it', 'had', 'been', 'made', 'of', 'wax.', 'The', 'astonishment', 'her', 'two', 'sisters', 'were', 'in', 'was', 'excessively', 'great,', 'but', 'still', 'abundantly', 'greater', 'when', 'Cinderella', 'pulled', 'out', 'of', 'her', 'pocket', 'the', 'other', 'slipper,', 'and', 'put', 'it', 'on', 'her', 'foot.', 'Thereupon,', 'in', 'came', 'her', 'godmother,', 'who,', 'having', 'touched', 'with', 'her', 'wand', \"Cinderella's\", 'clothes,', 'made', 'them', 'richer', 'and', 'more', 'magnificent', 'than', 'any', 'of', 'those', 'she', 'had', 'before.', 'And', 'now', 'her', 'two', 'sisters', 'found', 'her', 'to', 'be', 'that', 'fine,', 'beautiful', 'lady', 'whom', 'they', 'had', 'seen', 'at', 'the', 'ball.', 'They', 'threw', 'themselves', 'at', 'her', 'feet', 'to', 'beg', 'pardon', 'for', 'all', 'the', 'ill-', 'treatment', 'they', 'had', 'made', 'her', 'undergo.', 'Cinderella', 'took', 'them', 'up,', 'and,', 'as', 'she', 'embraced', 'them,', 'cried:', 'That', 'she', 'forgave', 'them', 'with', 'all', 'her', 'heart,', 'and', 'desired', 'them', 'always', 'to', 'love', 'her.', 'She', 'was', 'conducted', 'to', 'the', 'young', 'prince,', 'dressed', 'as', 'she', 'was;', 'he', 'thought', 'her', 'more', 'charming', 'than', 'ever,', 'and,', 'a', 'few', 'days', 'after,', 'married', 'her.', 'Cinderella,', 'who', 'was', 'no', 'less', 'good', 'than', 'beautiful,', 'gave', 'her', 'two', 'sisters', 'lodgings', 'in', 'the', 'palace.'], ['Once', 'upon', 'a', 'time', 'there', 'lived', 'a', 'poor', 'widow', 'and', 'her', 'son', 'Jack.', 'One', 'day,', 'Jack’s', 'mother', 'told', 'him', 'to', 'sell', 'their', 'only', 'cow.', 'Jack', 'went', 'to', 'the', 'market', 'and', 'on', 'the', 'way', 'he', 'met', 'a', 'man', 'who', 'wanted', 'to', 'buy', 'his', 'cow.', 'Jack', 'asked,', '“What', 'will', 'you', 'give', 'me', 'in', 'return', 'for', 'my', 'cow?”', 'The', 'man', 'answered,', '“I', 'will', 'give', 'you', 'five', 'magic', 'beans!”', 'Jack', 'took', 'the', 'magic', 'beans', 'and', 'gave', 'the', 'man', 'the', 'cow.', 'But', 'when', 'he', 'reached', 'home,', 'Jack’s', 'mother', 'was', 'very', 'angry.', 'She', 'said,', '“You', 'fool!', 'He', 'took', 'away', 'your', 'cow', 'and', 'gave', 'you', 'some', 'beans!”', 'She', 'threw', 'the', 'beans', 'out', 'of', 'the', 'window.', 'Jack', 'was', 'very', 'sad', 'and', 'went', 'to', 'sleep', 'without', 'dinner.', 'The', 'next', 'day,', 'when', 'Jack', 'woke', 'up', 'in', 'the', 'morning', 'and', 'looked', 'out', 'of', 'the', 'window,', 'he', 'saw', 'that', 'a', 'huge', 'beanstalk', 'had', 'grown', 'from', 'his', 'magic', 'beans!', 'He', 'climbed', 'up', 'the', 'beanstalk', 'and', 'reached', 'a', 'kingdom', 'in', 'the', 'sky.', 'There', 'lived', 'a', 'giant', 'and', 'his', 'wife.', 'Jack', 'went', 'inside', 'the', 'house', 'and', 'found', 'the', 'giant’s', 'wife', 'in', 'the', 'kitchen.', 'Jack', 'said,', '“Could', 'you', 'please', 'give', 'me', 'something', 'to', 'eat?', 'I', 'am', 'so', 'hungry!”', 'The', 'kind', 'wife', 'gave', 'him', 'bread', 'and', 'some', 'milk.', 'While', 'he', 'was', 'eating,', 'the', 'giant', 'came', 'home.', 'The', 'giant', 'was', 'very', 'big', 'and', 'looked', 'very', 'fearsome.', 'Jack', 'was', 'terrified', 'and', 'went', 'and', 'hid', 'inside.', 'The', 'giant', 'cried,', '“Fee-fi-fo-fum,', 'I', 'smell', 'the', 'blood', 'of', 'an', 'Englishman.', 'Be', 'he', 'alive,', 'or', 'be', 'he', 'dead,', 'I’ll', 'grind', 'his', 'bones', 'to', 'make', 'my', 'bread!”', 'The', 'wife', 'said,', '“There', 'is', 'no', 'boy', 'in', 'here!”', 'So,', 'the', 'giant', 'ate', 'his', 'food', 'and', 'then', 'went', 'to', 'his', 'room.', 'He', 'took', 'out', 'his', 'sacks', 'of', 'gold', 'coins,', 'counted', 'them', 'and', 'kept', 'them', 'aside.', 'Then', 'he', 'went', 'to', 'sleep.', 'In', 'the', 'night,', 'Jack', 'crept', 'out', 'of', 'his', 'hiding', 'place,', 'took', 'one', 'sack', 'of', 'gold', 'coins', 'and', 'climbed', 'down', 'the', 'beanstalk.', 'At', 'home,', 'he', 'gave', 'the', 'coins', 'to', 'his', 'mother.', 'His', 'mother', 'was', 'very', 'happy', 'and', 'they', 'lived', 'well', 'for', 'sometime.', 'Jack', 'and', 'the', 'Beanstalk', 'Fee', 'Fi', 'Fo', 'Fum!Climbed', 'the', 'beanstalk', 'and', 'went', 'to', 'the', 'giant’s', 'house', 'again.', 'Once', 'again,', 'Jack', 'asked', 'the', 'giant’s', 'wife', 'for', 'food,', 'but', 'while', 'he', 'was', 'eating', 'the', 'giant', 'returned.', 'Jack', 'leapt', 'up', 'in', 'fright', 'and', 'went', 'and', 'hid', 'under', 'the', 'bed.', 'The', 'giant', 'cried,', '“Fee-fifo-fum,', 'I', 'smell', 'the', 'blood', 'of', 'an', 'Englishman.', 'Be', 'he', 'alive,', 'or', 'be', 'he', 'dead,', 'I’ll', 'grind', 'his', 'bones', 'to', 'make', 'my', 'bread!”', 'The', 'wife', 'said,', '“There', 'is', 'no', 'boy', 'in', 'here!”', 'The', 'giant', 'ate', 'his', 'food', 'and', 'went', 'to', 'his', 'room.', 'There,', 'he', 'took', 'out', 'a', 'hen.', 'He', 'shouted,', '“Lay!”', 'and', 'the', 'hen', 'laid', 'a', 'golden', 'egg.', 'When', 'the', 'giant', 'fell', 'asleep,', 'Jack', 'took', 'the', 'hen', 'and', 'climbed', 'down', 'the', 'beanstalk.', 'Jack’s', 'mother', 'was', 'very', 'happy', 'with', 'him.', 'After', 'some', 'days,', 'Jack', 'once', 'again', 'climbed', 'the', 'beanstalk', 'and', 'went', 'to', 'the', 'giant’s', 'castle.', 'For', 'the', 'third', 'time,', 'Jack', 'met', 'the', 'giant’s', 'wife', 'and', 'asked', 'for', 'some', 'food.', 'Once', 'again,', 'the', 'giant’s', 'wife', 'gave', 'him', 'bread', 'and', 'milk.', 'But', 'while', 'Jack', 'was', 'eating,', 'the', 'giant', 'came', 'home.', '“Fee-fi-fo-fum,', 'I', 'smell', 'the', 'blood', 'of', 'an', 'Englishman.', 'Be', 'he', 'alive,', 'or', 'be', 'he', 'dead,', 'I’ll', 'grind', 'his', 'bones', 'to', 'make', 'my', 'bread!”', 'cried', 'the', 'giant.', '“Don’t', 'be', 'silly!', 'There', 'is', 'no', 'boy', 'in', 'here!”', 'said', 'his', 'wife.', 'The', 'giant', 'had', 'a', 'magical', 'harp', 'that', 'could', 'play', 'beautiful', 'songs.', 'While', 'the', 'giant', 'slept,', 'Jack', 'took', 'the', 'harp', 'and', 'was', 'about', 'to', 'leave.', 'Suddenly,', 'the', 'magic', 'harp', 'cried,', '“Help', 'master!', 'A', 'boy', 'is', 'stealing', 'me!”', 'The', 'giant', 'woke', 'up', 'and', 'saw', 'Jack', 'with', 'the', 'harp.', 'Furious,', 'he', 'ran', 'after', 'Jack.', 'But', 'Jack', 'was', 'too', 'fast', 'for', 'him.', 'He', 'ran', 'down', 'the', 'beanstalk', 'and', 'reached', 'home.', 'The', 'giant', 'followed', 'him', 'down.', 'Jack', 'quickly', 'ran', 'inside', 'his', 'house', 'and', 'fetched', 'an', 'axe.', 'He', 'began', 'to', 'chop', 'the', 'beanstalk.', 'The', 'giant', 'fell', 'and', 'died.', 'Jack', 'and', 'his', 'mother', 'were', 'now', 'very', 'rich', 'and', 'they', 'lived', 'happily', 'ever', 'after.'], ['Long,', 'long', 'ago,', 'there', 'lived', 'an', 'old', 'farmer', 'and', 'his', 'wife', 'who', 'had', 'made', 'their', 'home', 'in', 'the', 'mountains,', 'far', 'from', 'any', 'town.', 'Their', 'only', 'neighbor', 'was', 'a', 'bad', 'and', 'malicious', 'badger.', 'This', 'badger', 'used', 'to', 'come', 'out', 'every', 'night', 'and', 'run', 'across', 'to', 'the', \"farmer's\", 'field', 'and', 'spoil', 'the', 'vegetables', 'and', 'the', 'rice', 'which', 'the', 'farmer', 'spent', 'his', 'time', 'in', 'carefully', 'cultivating.', 'The', 'badger', 'at', 'last', 'grew', 'so', 'ruthless', 'in', 'his', 'mischievous', 'work,', 'and', 'did', 'so', 'much', 'harm', 'everywhere', 'on', 'the', 'farm,', 'that', 'the', 'good-natured', 'farmer', 'could', 'not', 'stand', 'it', 'any', 'longer,', 'and', 'determined', 'to', 'put', 'a', 'stop', 'to', 'it.', 'So', 'he', 'lay', 'in', 'wait', 'day', 'after', 'day', 'and', 'night', 'after', 'night,', 'with', 'a', 'big', 'club,', 'hoping', 'to', 'catch', 'the', 'badger,', 'but', 'all', 'in', 'vain.', 'Then', 'he', 'laid', 'traps', 'for', 'the', 'wicked', 'animal.', 'The', \"farmer's\", 'trouble', 'and', 'patience', 'was', 'rewarded,', 'for', 'one', 'fine', 'day', 'on', 'going', 'his', 'rounds', 'he', 'found', 'the', 'badger', 'caught', 'in', 'a', 'hole', 'he', 'had', 'dug', 'for', 'that', 'purpose.', 'The', 'farmer', 'was', 'delighted', 'at', 'having', 'caught', 'his', 'enemy,', 'and', 'carried', 'him', 'home', 'securely', 'bound', 'with', 'rope.', 'When', 'he', 'reached', 'the', 'house', 'the', 'farmer', 'said', 'to', 'his', 'wife:', '\"I', 'have', 'at', 'last', 'caught', 'the', 'bad', 'badger.', 'You', 'must', 'keep', 'an', 'eye', 'on', 'him', 'while', 'I', 'am', 'out', 'at', 'work', 'and', 'not', 'let', 'him', 'escape,', 'because', 'I', 'want', 'to', 'make', 'him', 'into', 'soup', 'to-night.\"', 'Saying', 'this,', 'he', 'hung', 'the', 'badger', 'up', 'to', 'the', 'rafters', 'of', 'his', 'storehouse', 'and', 'went', 'out', 'to', 'his', 'work', 'in', 'the', 'fields.', 'The', 'badger', 'was', 'in', 'great', 'distress,', 'for', 'he', 'did', 'not', 'at', 'all', 'like', 'the', 'idea', 'of', 'being', 'made', 'into', 'soup', 'that', 'night,', 'and', 'he', 'thought', 'and', 'thought', 'for', 'a', 'long', 'time,', 'trying', 'to', 'hit', 'upon', 'some', 'plan', 'by', 'which', 'he', 'might', 'escape.', 'It', 'was', 'hard', 'to', 'think', 'clearly', 'in', 'his', 'uncomfortable', 'position,', 'for', 'he', 'had', 'been', 'hung', 'upside', 'down.', 'Very', 'near', 'him,', 'at', 'the', 'entrance', 'to', 'the', 'storehouse,', 'looking', 'out', 'towards', 'the', 'green', 'fields', 'and', 'the', 'trees', 'and', 'the', 'pleasant', 'sunshine,', 'stood', 'the', \"farmer's\", 'old', 'wife', 'pounding', 'barley.', 'She', 'looked', 'tired', 'and', 'old.', 'Her', 'face', 'was', 'seamed', 'with', 'many', 'wrinkles,', 'and', 'was', 'as', 'brown', 'as', 'leather,', 'and', 'every', 'now', 'and', 'then', 'she', 'stopped', 'to', 'wipe', 'the', 'perspiration', 'which', 'rolled', 'down', 'her', 'face.', '\"Dear', 'lady,\"', 'said', 'the', 'wily', 'badger,', '\"you', 'must', 'be', 'very', 'weary', 'doing', 'such', 'heavy', 'work', 'in', 'your', 'old', 'age.', \"Won't\", 'you', 'let', 'me', 'do', 'that', 'for', 'you?', 'My', 'arms', 'are', 'very', 'strong,', 'and', 'I', 'could', 'relieve', 'you', 'for', 'a', 'little', 'while!\"', '\"Thank', 'you', 'for', 'your', 'kindness,\"', 'said', 'the', 'old', 'woman,', '\"but', 'I', 'cannot', 'let', 'you', 'do', 'this', 'work', 'for', 'me', 'because', 'I', 'must', 'not', 'untie', 'you,', 'for', 'you', 'might', 'escape', 'if', 'I', 'did,', 'and', 'my', 'husband', 'would', 'be', 'very', 'angry', 'if', 'he', 'came', 'home', 'and', 'found', 'you', 'gone.\"', 'Now,', 'the', 'badger', 'is', 'one', 'of', 'the', 'most', 'cunning', 'of', 'animals,', 'and', 'he', 'said', 'again', 'in', 'a', 'very', 'sad,', 'gentle,', 'voice:', '\"You', 'are', 'very', 'unkind.', 'You', 'might', 'untie', 'me,', 'for', 'I', 'promise', 'not', 'to', 'try', 'to', 'escape.', 'If', 'you', 'are', 'afraid', 'of', 'your', 'husband,', 'I', 'will', 'let', 'you', 'bind', 'me', 'again', 'before', 'his', 'return', 'when', 'I', 'have', 'finished', 'pounding', 'the', 'barley.', 'I', 'am', 'so', 'tired', 'and', 'sore', 'tied', 'up', 'like', 'this.', 'If', 'you', 'would', 'only', 'let', 'me', 'down', 'for', 'a', 'few', 'minutes', 'I', 'would', 'indeed', 'be', 'thankful!\"', 'The', 'old', 'woman', 'had', 'a', 'good', 'and', 'simple', 'nature,', 'and', 'could', 'not', 'think', 'badly', 'of', 'any', 'one.', 'Much', 'less', 'did', 'she', 'think', 'that', 'the', 'badger', 'was', 'only', 'deceiving', 'her', 'in', 'order', 'to', 'get', 'away.', 'She', 'felt', 'sorry,', 'too,', 'for', 'the', 'animal', 'as', 'she', 'turned', 'to', 'look', 'at', 'him.', 'He', 'looked', 'in', 'such', 'a', 'sad', 'plight', 'hanging', 'downwards', 'from', 'the', 'ceiling', 'by', 'his', 'legs,', 'which', 'were', 'all', 'tied', 'together', 'so', 'tightly', 'that', 'the', 'rope', 'and', 'the', 'knots', 'were', 'cutting', 'into', 'the', 'skin.', 'So', 'in', 'the', 'kindness', 'of', 'her', 'heart,', 'and', 'believing', 'the', \"creature's\", 'promise', 'that', 'he', 'would', 'not', 'run', 'away,', 'she', 'untied', 'the', 'cord', 'and', 'let', 'him', 'down.', 'The', 'old', 'woman', 'then', 'gave', 'him', 'the', 'wooden', 'pestle', 'and', 'told', 'him', 'to', 'do', 'the', 'work', 'for', 'a', 'short', 'time', 'while', 'she', 'rested.', 'He', 'took', 'the', 'pestle,', 'but', 'instead', 'of', 'doing', 'the', 'work', 'as', 'he', 'was', 'told,', 'the', 'badger', 'at', 'once', 'sprang', 'upon', 'the', 'old', 'woman', 'and', 'knocked', 'her', 'down', 'with', 'the', 'heavy', 'piece', 'of', 'wood.', 'He', 'then', 'killed', 'her', 'and', 'cut', 'her', 'up', 'and', 'made', 'soup', 'of', 'her,', 'and', 'waited', 'for', 'the', 'return', 'of', 'the', 'old', 'farmer.', 'The', 'old', 'man', 'worked', 'hard', 'in', 'his', 'fields', 'all', 'day,', 'and', 'as', 'he', 'worked', 'he', 'thought', 'with', 'pleasure', 'that', 'no', 'more', 'now', 'would', 'his', 'labor', 'be', 'spoiled', 'by', 'the', 'destructive', 'badger.', 'Towards', 'sunset', 'he', 'left', 'his', 'work', 'and', 'turned', 'to', 'go', 'home.', 'He', 'was', 'very', 'tired,', 'but', 'the', 'thought', 'of', 'the', 'nice', 'supper', 'of', 'hot', 'badger', 'soup', 'awaiting', 'his', 'return', 'cheered', 'him.', 'The', 'thought', 'that', 'the', 'badger', 'might', 'get', 'free', 'and', 'take', 'revenge', 'on', 'the', 'poor', 'old', 'woman', 'never', 'once', 'came', 'into', 'his', 'mind.', 'The', 'badger', 'meanwhile', 'assumed', 'the', 'old', \"woman's\", 'form,', 'and', 'as', 'soon', 'as', 'he', 'saw', 'the', 'old', 'farmer', 'approaching', 'came', 'out', 'to', 'greet', 'him', 'on', 'the', 'veranda', 'of', 'the', 'little', 'house,', 'saying:', '\"So', 'you', 'have', 'come', 'back', 'at', 'last.', 'I', 'have', 'made', 'the', 'badger', 'soup', 'and', 'have', 'been', 'waiting', 'for', 'you', 'for', 'a', 'long', 'time.\"', 'The', 'old', 'farmer', 'quickly', 'took', 'off', 'his', 'straw', 'sandals', 'and', 'sat', 'down', 'before', 'his', 'tiny', 'dinner-tray.', 'The', 'innocent', 'man', 'never', 'even', 'dreamed', 'that', 'it', 'was', 'not', 'his', 'wife', 'but', 'the', 'badger', 'who', 'was', 'waiting', 'upon', 'him,', 'and', 'asked', 'at', 'once', 'for', 'the', 'soup.', 'Then', 'the', 'badger', 'suddenly', 'transformed', 'himself', 'back', 'to', 'his', 'natural', 'form', 'and', 'cried', 'out:', '\"You', 'wife-eating', 'old', 'man!', 'Look', 'out', 'for', 'the', 'bones', 'in', 'the', 'kitchen!\"', 'Laughing', 'loudly', 'and', 'derisively', 'he', 'escaped', 'out', 'of', 'the', 'house', 'and', 'ran', 'away', 'to', 'his', 'den', 'in', 'the', 'hills.', 'The', 'old', 'man', 'was', 'left', 'behind', 'alone.', 'He', 'could', 'hardly', 'believe', 'what', 'he', 'had', 'seen', 'and', 'heard.', 'Then', 'when', 'he', 'understood', 'the', 'whole', 'truth', 'he', 'was', 'so', 'scared', 'and', 'horrified', 'that', 'he', 'fainted', 'right', 'away.', 'After', 'a', 'while', 'he', 'came', 'round', 'and', 'burst', 'into', 'tears.', 'He', 'cried', 'loudly', 'and', 'bitterly.', 'He', 'rocked', 'himself', 'to', 'and', 'fro', 'in', 'his', 'hopeless', 'grief.', 'It', 'seemed', 'too', 'terrible', 'to', 'be', 'real', 'that', 'his', 'faithful', 'old', 'wife', 'had', 'been', 'killed', 'and', 'cooked', 'by', 'the', 'badger', 'while', 'he', 'was', 'working', 'quietly', 'in', 'the', 'fields,', 'knowing', 'nothing', 'of', 'what', 'was', 'going', 'on', 'at', 'home,', 'and', 'congratulating', 'himself', 'on', 'having', 'once', 'for', 'all', 'got', 'rid', 'of', 'the', 'wicked', 'animal', 'who', 'had', 'so', 'often', 'spoiled', 'his', 'fields.', 'And', 'oh!', 'the', 'horrible', 'thought;', 'he', 'had', 'very', 'nearly', 'drunk', 'the', 'soup', 'which', 'the', 'creature', 'had', 'made', 'of', 'his', 'poor', 'old', 'woman.', '\"Oh', 'dear,', 'oh', 'dear,', 'oh', 'dear!\"', 'he', 'wailed', 'aloud.', 'Now,', 'not', 'far', 'away', 'there', 'lived', 'in', 'the', 'same', 'mountain', 'a', 'kind,', 'good-natured', 'old', 'rabbit.', 'He', 'heard', 'the', 'old', 'man', 'crying', 'and', 'sobbing', 'and', 'at', 'once', 'set', 'out', 'to', 'see', 'what', 'was', 'the', 'matter,', 'and', 'if', 'there', 'was', 'anything', 'he', 'could', 'do', 'to', 'help', 'his', 'neighbor.', 'The', 'old', 'man', 'told', 'him', 'all', 'that', 'had', 'happened.', 'When', 'the', 'rabbit', 'heard', 'the', 'story', 'he', 'was', 'very', 'angry', 'at', 'the', 'wicked', 'and', 'deceitful', 'badger,', 'and', 'told', 'the', 'old', 'man', 'to', 'leave', 'everything', 'to', 'him', 'and', 'he', 'would', 'avenge', 'his', \"wife's\", 'death.', 'The', 'farmer', 'was', 'at', 'last', 'comforted,', 'and,', 'wiping', 'away', 'his', 'tears,', 'thanked', 'the', 'rabbit', 'for', 'his', 'goodness', 'in', 'coming', 'to', 'him', 'in', 'his', 'distress.', 'The', 'rabbit,', 'seeing', 'that', 'the', 'farmer', 'was', 'growing', 'calmer,', 'went', 'back', 'to', 'his', 'home', 'to', 'lay', 'his', 'plans', 'for', 'the', 'punishment', 'of', 'the', 'badger.', 'The', 'next', 'day', 'the', 'weather', 'was', 'fine,', 'and', 'the', 'rabbit', 'went', 'out', 'to', 'find', 'the', 'badger.', 'He', 'was', 'not', 'to', 'be', 'seen', 'in', 'the', 'woods', 'or', 'on', 'the', 'hillside', 'or', 'in', 'the', 'fields', 'anywhere,', 'so', 'the', 'rabbit', 'went', 'to', 'his', 'den', 'and', 'found', 'the', 'badger', 'hiding', 'there,', 'for', 'the', 'animal', 'had', 'been', 'afraid', 'to', 'show', 'himself', 'ever', 'since', 'he', 'had', 'escaped', 'from', 'the', \"farmer's\", 'house,', 'for', 'fear', 'of', 'the', 'old', \"man's\", 'wrath.', 'The', 'rabbit', 'called', 'out:', '\"Why', 'are', 'you', 'not', 'out', 'on', 'such', 'a', 'beautiful', 'day?', 'Come', 'out', 'with', 'me,', 'and', 'we', 'will', 'go', 'and', 'cut', 'grass', 'on', 'the', 'hills', 'together.\"', 'The', 'badger,', 'never', 'doubting', 'but', 'that', 'the', 'rabbit', 'was', 'his', 'friend,', 'willingly', 'consented', 'to', 'go', 'out', 'with', 'him,', 'only', 'too', 'glad', 'to', 'get', 'away', 'from', 'the', 'neighborhood', 'of', 'the', 'farmer', 'and', 'the', 'fear', 'of', 'meeting', 'him.', 'The', 'rabbit', 'led', 'the', 'way', 'miles', 'away', 'from', 'their', 'homes,', 'out', 'on', 'the', 'hills', 'where', 'the', 'grass', 'grew', 'tall', 'and', 'thick', 'and', 'sweet.', 'They', 'both', 'set', 'to', 'work', 'to', 'cut', 'down', 'as', 'much', 'as', 'they', 'could', 'carry', 'home,', 'to', 'store', 'it', 'up', 'for', 'their', \"winter's\", 'food.', 'When', 'they', 'had', 'each', 'cut', 'down', 'all', 'they', 'wanted', 'they', 'tied', 'it', 'in', 'bundles', 'and', 'then', 'started', 'homewards,', 'each', 'carrying', 'his', 'bundle', 'of', 'grass', 'on', 'his', 'back.', 'This', 'time', 'the', 'rabbit', 'made', 'the', 'badger', 'go', 'first.', 'When', 'they', 'had', 'gone', 'a', 'little', 'way', 'the', 'rabbit', 'took', 'out', 'a', 'flint', 'and', 'steel,', 'and,', 'striking', 'it', 'over', 'the', \"badger's\", 'back', 'as', 'he', 'stepped', 'along', 'in', 'front,', 'set', 'his', 'bundle', 'of', 'grass', 'on', 'fire.', 'The', 'badger', 'heard', 'the', 'flint', 'striking,', 'and', 'asked:', '\"What', 'is', 'that', 'noise.', \"'Crack,\", 'crack\\'?\"', '\"Oh,', 'that', 'is', 'nothing.\"', 'replied', 'the', 'rabbit;', '\"I', 'only', 'said', \"'Crack,\", \"crack'\", 'because', 'this', 'mountain', 'is', 'called', 'Crackling', 'Mountain.\"', 'The', 'fire', 'soon', 'spread', 'in', 'the', 'bundle', 'of', 'dry', 'grass', 'on', 'the', \"badger's\", 'back.', 'The', 'badger,', 'hearing', 'the', 'crackle', 'of', 'the', 'burning', 'grass,', 'asked,', '\"What', 'is', 'that?\"', '\"Now', 'we', 'have', 'come', 'to', 'the', \"'Burning\", 'Mountain,\\'\"', 'answered', 'the', 'rabbit.', 'By', 'this', 'time', 'the', 'bundle', 'was', 'nearly', 'burned', 'out', 'and', 'all', 'the', 'hair', 'had', 'been', 'burned', 'off', 'the', \"badger's\", 'back.', 'He', 'now', 'knew', 'what', 'had', 'happened', 'by', 'the', 'smell', 'of', 'the', 'smoke', 'of', 'the', 'burning', 'grass.', 'Screaming', 'with', 'pain', 'the', 'badger', 'ran', 'as', 'fast', 'as', 'he', 'could', 'to', 'his', 'hole.', 'The', 'rabbit', 'followed', 'and', 'found', 'him', 'lying', 'on', 'his', 'bed', 'groaning', 'with', 'pain.', '\"What', 'an', 'unlucky', 'fellow', 'you', 'are!\"', 'said', 'the', 'rabbit.', '\"I', \"can't\", 'imagine', 'how', 'this', 'happened!', 'I', 'will', 'bring', 'you', 'some', 'medicine', 'which', 'will', 'heal', 'your', 'back', 'quickly!\"', 'The', 'rabbit', 'went', 'away', 'glad', 'and', 'smiling', 'to', 'think', 'that', 'the', 'punishment', 'upon', 'the', 'badger', 'had', 'already', 'begun.', 'He', 'hoped', 'that', 'the', 'badger', 'would', 'die', 'of', 'his', 'burns,', 'for', 'he', 'felt', 'that', 'nothing', 'could', 'be', 'too', 'bad', 'for', 'the', 'animal,', 'who', 'was', 'guilty', 'of', 'murdering', 'a', 'poor', 'helpless', 'old', 'woman', 'who', 'had', 'trusted', 'him.', 'He', 'went', 'home', 'and', 'made', 'an', 'ointment', 'by', 'mixing', 'some', 'sauce', 'and', 'red', 'pepper', 'together.', 'He', 'carried', 'this', 'to', 'the', 'badger,', 'but', 'before', 'putting', 'it', 'on', 'he', 'told', 'him', 'that', 'it', 'would', 'cause', 'him', 'great', 'pain,', 'but', 'that', 'he', 'must', 'bear', 'it', 'patiently,', 'because', 'it', 'was', 'a', 'very', 'wonderful', 'medicine', 'for', 'burns', 'and', 'scalds', 'and', 'such', 'wounds.', 'The', 'badger', 'thanked', 'him', 'and', 'begged', 'him', 'to', 'apply', 'it', 'at', 'once.', 'But', 'no', 'language', 'can', 'describe', 'the', 'agony', 'of', 'the', 'badger', 'as', 'soon', 'as', 'the', 'red', 'pepper', 'had', 'been', 'pasted', 'all', 'over', 'his', 'sore', 'back.', 'He', 'rolled', 'over', 'and', 'over', 'and', 'howled', 'loudly.', 'The', 'rabbit,', 'looking', 'on,', 'felt', 'that', 'the', \"farmer's\", 'wife', 'was', 'beginning', 'to', 'be', 'avenged.', 'The', 'badger', 'was', 'in', 'bed', 'for', 'about', 'a', 'month;', 'but', 'at', 'last,', 'in', 'spite', 'of', 'the', 'red', 'pepper', 'application,', 'his', 'burns', 'healed', 'and', 'he', 'got', 'well.', 'When', 'the', 'rabbit', 'saw', 'that', 'the', 'badger', 'was', 'getting', 'well,', 'he', 'thought', 'of', 'another', 'plan', 'by', 'which', 'he', 'could', 'compass', 'the', \"creature's\", 'death.', 'So', 'he', 'went', 'one', 'day', 'to', 'pay', 'the', 'badger', 'a', 'visit', 'and', 'to', 'congratulate', 'him', 'on', 'his', 'recovery.', 'During', 'the', 'conversation', 'the', 'rabbit', 'mentioned', 'that', 'he', 'was', 'going', 'fishing,', 'and', 'described', 'how', 'pleasant', 'fishing', 'was', 'when', 'the', 'weather', 'was', 'fine', 'and', 'the', 'sea', 'smooth.', 'The', 'badger', 'listened', 'with', 'pleasure', 'to', 'the', \"rabbit's\", 'account', 'of', 'the', 'way', 'he', 'passed', 'his', 'time', 'now,', 'and', 'forgot', 'all', 'his', 'pains', 'and', 'his', \"month's\", 'illness,', 'and', 'thought', 'what', 'fun', 'it', 'would', 'be', 'if', 'he', 'could', 'go', 'fishing', 'too;', 'so', 'he', 'asked', 'the', 'rabbit', 'if', 'he', 'would', 'take', 'him', 'the', 'next', 'time', 'he', 'went', 'out', 'to', 'fish.', 'This', 'was', 'just', 'what', 'the', 'rabbit', 'wanted,', 'so', 'he', 'agreed.', 'Then', 'he', 'went', 'home', 'and', 'built', 'two', 'boats,', 'one', 'of', 'wood', 'and', 'the', 'other', 'of', 'clay.', 'At', 'last', 'they', 'were', 'both', 'finished,', 'and', 'as', 'the', 'rabbit', 'stood', 'and', 'looked', 'at', 'his', 'work', 'he', 'felt', 'that', 'all', 'his', 'trouble', 'would', 'be', 'well', 'rewarded', 'if', 'his', 'plan', 'succeeded,', 'and', 'he', 'could', 'manage', 'to', 'kill', 'the', 'wicked', 'badger', 'now.', 'The', 'day', 'came', 'when', 'the', 'rabbit', 'had', 'arranged', 'to', 'take', 'the', 'badger', 'fishing.', 'He', 'kept', 'the', 'wooden', 'boat', 'himself', 'and', 'gave', 'the', 'badger', 'the', 'clay', 'boat.', 'The', 'badger,', 'who', 'knew', 'nothing', 'about', 'boats,', 'was', 'delighted', 'with', 'his', 'new', 'boat', 'and', 'thought', 'how', 'kind', 'it', 'was', 'of', 'the', 'rabbit', 'to', 'give', 'it', 'to', 'him.', 'They', 'both', 'got', 'into', 'their', 'boats', 'and', 'set', 'out.', 'After', 'going', 'some', 'distance', 'from', 'the', 'shore', 'the', 'rabbit', 'proposed', 'that', 'they', 'should', 'try', 'their', 'boats', 'and', 'see', 'which', 'one', 'could', 'go', 'the', 'quickest.', 'The', 'badger', 'fell', 'in', 'with', 'the', 'proposal,', 'and', 'they', 'both', 'set', 'to', 'work', 'to', 'row', 'as', 'fast', 'as', 'they', 'could', 'for', 'some', 'time.', 'In', 'the', 'middle', 'of', 'the', 'race', 'the', 'badger', 'found', 'his', 'boat', 'going', 'to', 'pieces,', 'for', 'the', 'water', 'now', 'began', 'to', 'soften', 'the', 'clay.', 'He', 'cried', 'out', 'in', 'great', 'fear', 'to', 'the', 'rabbit', 'to', 'help', 'him.', 'But', 'the', 'rabbit', 'answered', 'that', 'he', 'was', 'avenging', 'the', 'old', \"woman's\", 'murder,', 'and', 'that', 'this', 'had', 'been', 'his', 'intention', 'all', 'along,', 'and', 'that', 'he', 'was', 'happy', 'to', 'think', 'that', 'the', 'badger', 'had', 'at', 'last', 'met', 'his', 'deserts', 'for', 'all', 'his', 'evil', 'crimes,', 'and', 'was', 'to', 'drown', 'with', 'no', 'one', 'to', 'help', 'him.', 'Then', 'he', 'raised', 'his', 'oar', 'and', 'struck', 'at', 'the', 'badger', 'with', 'all', 'his', 'strength', 'till', 'he', 'fell', 'with', 'the', 'sinking', 'clay', 'boat', 'and', 'was', 'seen', 'no', 'more.', 'Thus', 'at', 'last', 'he', 'kept', 'his', 'promise', 'to', 'the', 'old', 'farmer.', 'The', 'rabbit', 'now', 'turned', 'and', 'rowed', 'shorewards,', 'and', 'having', 'landed', 'and', 'pulled', 'his', 'boat', 'upon', 'the', 'beach,', 'hurried', 'back', 'to', 'tell', 'the', 'old', 'farmer', 'everything,', 'and', 'how', 'the', 'badger,', 'his', 'enemy,', 'had', 'been', 'killed.', 'The', 'old', 'farmer', 'thanked', 'him', 'with', 'tears', 'in', 'his', 'eyes.', 'He', 'said', 'that', 'till', 'now', 'he', 'could', 'never', 'sleep', 'at', 'night', 'or', 'be', 'at', 'peace', 'in', 'the', 'daytime,', 'thinking', 'of', 'how', 'his', \"wife's\", 'death', 'was', 'unavenged,', 'but', 'from', 'this', 'time', 'he', 'would', 'be', 'able', 'to', 'sleep', 'and', 'eat', 'as', 'of', 'old.', 'He', 'begged', 'the', 'rabbit', 'to', 'stay', 'with', 'him', 'and', 'share', 'his', 'home,', 'so', 'from', 'this', 'day', 'the', 'rabbit', 'went', 'to', 'stay', 'with', 'the', 'old', 'farmer', 'and', 'they', 'both', 'lived', 'together', 'as', 'good', 'friends', 'to', 'the', 'end', 'of', 'their', 'days.'], ['ONCE', 'upon', 'a', 'time', 'there', 'was', 'a', 'prince', 'who', 'wanted', 'to', 'marry', 'a', 'princess;', 'but', 'she', 'would', 'have', 'to', 'be', 'a', 'real', 'princess.', 'He', 'travelled', 'all', 'over', 'the', 'world', 'to', 'find', 'one,', 'but', 'nowhere', 'could', 'he', 'get', 'what', 'he', 'wanted.', 'There', 'were', 'princesses', 'enough,', 'but', 'it', 'was', 'difficult', 'to', 'find', 'out', 'whether', 'they', 'were', 'real', 'ones.', 'There', 'was', 'always', 'something', 'about', 'them', 'that', 'was', 'not', 'as', 'it', 'should', 'be.', 'So', 'he', 'came', 'home', 'again', 'and', 'was', 'sad,', 'for', 'he', 'would', 'have', 'liked', 'very', 'much', 'to', 'have', 'a', 'real', 'princess.', 'One', 'evening', 'a', 'terrible', 'storm', 'came', 'on;', 'there', 'was', 'thunder', 'and', 'lightning,', 'and', 'the', 'rain', 'poured', 'down', 'in', 'torrents.', 'Suddenly', 'a', 'knocking', 'was', 'heard', 'at', 'the', 'city', 'gate,', 'and', 'the', 'old', 'king', 'went', 'to', 'open', 'it.', 'It', 'was', 'a', 'princess', 'standing', 'out', 'there', 'in', 'front', 'of', 'the', 'gate.', 'But,', 'good', 'gracious!', 'what', 'a', 'sight', 'the', 'rain', 'and', 'the', 'wind', 'had', 'made', 'her', 'look.', 'The', 'water', 'ran', 'down', 'from', 'her', 'hair', 'and', 'clothes;', 'it', 'ran', 'down', 'into', 'the', 'toes', 'of', 'her', 'shoes', 'and', 'out', 'again', 'at', 'the', 'heels.', 'And', 'yet', 'she', 'said', 'that', 'she', 'was', 'a', 'real', 'princess.', 'Well,', \"we'll\", 'soon', 'find', 'that', 'out,', 'thought', 'the', 'old', 'queen.', 'But', 'she', 'said', 'nothing,', 'went', 'into', 'the', 'bed-room,', 'took', 'all', 'the', 'bedding', 'off', 'the', 'bedstead,', 'and', 'laid', 'a', 'pea', 'on', 'the', 'bottom;', 'then', 'she', 'took', 'twenty', 'mattresses', 'and', 'laid', 'them', 'on', 'the', 'pea,', 'and', 'then', 'twenty', 'eider-down', 'beds', 'on', 'top', 'of', 'the', 'mattresses.', 'On', 'this', 'the', 'princess', 'had', 'to', 'lie', 'all', 'night.', 'In', 'the', 'morning', 'she', 'was', 'asked', 'how', 'she', 'had', 'slept.', 'Oh,', 'very', 'badly!', 'said', 'she.', 'I', 'have', 'scarcely', 'closed', 'my', 'eyes', 'all', 'night.', 'Heaven', 'only', 'knows', 'what', 'was', 'in', 'the', 'bed,', 'but', 'I', 'was', 'lying', 'on', 'something', 'hard,', 'so', 'that', 'I', 'am', 'black', 'and', 'blue', 'all', 'over', 'my', 'body.', 'Its', 'horrible!', 'Now', 'they', 'knew', 'that', 'she', 'was', 'a', 'real', 'princess', 'because', 'she', 'had', 'felt', 'the', 'pea', 'right', 'through', 'the', 'twenty', 'mattresses', 'and', 'the', 'twenty', 'eider-down', 'beds.', 'Nobody', 'but', 'a', 'real', 'princess', 'could', 'be', 'as', 'sensitive', 'as', 'that.', 'So', 'the', 'prince', 'took', 'her', 'for', 'his', 'wife,', 'for', 'now', 'he', 'knew', 'that', 'he', 'had', 'a', 'real', 'princess;', 'and', 'the', 'pea', 'was', 'put', 'in', 'the', 'museum,', 'where', 'it', 'may', 'still', 'be', 'seen,', 'if', 'no', 'one', 'has', 'stolen', 'it.', 'There,', 'that', 'is', 'a', 'true', 'story.']]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "huge_list = []\n",
    "huge_list2 = []\n",
    "huge_list3 = []\n",
    "huge_list4 = []\n",
    "\n",
    "\n",
    "with open(\"C:/Users/Prajna Shetty/PythonWorkspace/cinderella.txt\", \"r\") as f:\n",
    "    huge_list = f.read().split()\n",
    "    \n",
    "with open(\"C:/Users/Prajna Shetty/PythonWorkspace/thefarmerandthebadger.txt\", \"r\") as h:\n",
    "    huge_list3 = h.read().split()\n",
    "    \n",
    "with open(\"C:/Users/Prajna Shetty/PythonWorkspace/theprincessandthepea.txt\", \"r\") as i:\n",
    "    huge_list4 = i.read().split()\n",
    "    \n",
    "with open(\"C:/Users/Prajna Shetty/PythonWorkspace/jackandthebeanstalk.txt\", encoding=\"utf8\") as g:\n",
    "    huge_list2 = g.read().split()\n",
    "    \n",
    "listA = [huge_list,huge_list2,huge_list3,huge_list4]\n",
    "\n",
    "print(listA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "b6d9783a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(huge_list.count(\"asked\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27301e9c",
   "metadata": {},
   "source": [
    "Write a python program that generates a Boolean incidence Matrix for term-document (Don’t forget to sort them alphabetically)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8a3f292d",
   "metadata": {},
   "outputs": [],
   "source": [
    "cinderella = open('cinderella.txt', 'r',encoding='utf-8').read().lower()\n",
    "jackandthebeanstalk= open(\"jackandthebeanstalk.txt\",'r',encoding='utf-8').read().lower()\n",
    "thefarmerandthebadger=open(\"thefarmerandthebadger.txt\",'r',encoding='utf-8').read().lower()\n",
    "theprincessandthepea=open(\"theprincessandthepea.txt\",'r',encoding='utf-8').read().lower()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a7f1dc79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['able', 'about', 'above', 'abundantly', 'account', 'across', 'adjust', 'admired', 'advised', 'afraid', 'after', 'afterward', 'again', 'age', 'ago', 'agony', 'agreed', 'air', 'alas', 'alighted', 'alive', 'all', 'almost', 'alone', 'along', 'aloud', 'already', 'also', 'altogether', 'always', 'amends', 'among', 'amusing', 'and', 'angry', 'animal', 'animals', 'another', 'answer', 'answered', 'any', 'anyone', 'anything', 'anywhere', 'apparel', 'appear', 'apply', 'are', 'arms', 'arranged', 'art', 'ashes', 'aside', 'asked', 'asleep', 'assumed', 'ate', 'attentive', 'avenge', 'avenged', 'avenging', 'awaiting', 'away', 'awry', 'axe', 'back', 'bad', 'badger', 'badly', 'ball', 'banter', 'barley', 'beach', 'beans', 'beanstalk', 'bear', 'beard', 'beauties', 'beautiful', 'because', 'become', 'bed', 'bedaubed', 'bedding', 'beds', 'bedstead', 'been', 'before', 'beg', 'began', 'begged', 'beginning', 'begun', 'beheld', 'behind', 'being', 'believe', 'believing', 'beset', 'best', 'big', 'bind', 'bitterly', 'black', 'blood', 'blue', 'boat', 'boats', 'body', 'bones', 'bore', 'both', 'bottom', 'bound', 'boy', 'bread', 'breath', 'bring', 'broke', 'brought', 'brown', 'brushes', 'built', 'bundle', 'bundles', 'burned', 'burning', 'burns', 'burst', 'busied', 'busy', 'but', 'buy', 'called', 'calmer', 'came', 'can', 'cannot', 'carefully', 'carried', 'carry', 'carrying', 'castle', 'catch', 'caught', 'cause', 'caused', 'ceased', 'ceiling', 'ceremonies', 'certainly', 'chamber', 'charlotte', 'charming', 'cheered', 'chimney', 'choice', 'choosing', 'chop', 'cinderella', 'cinders', 'citrons', 'city', 'civilities', 'clay', 'clearly', 'climbed', 'clock', 'close', 'closed', 'cloth', 'clothes', 'club', 'clung', 'coach', 'coachman', 'coins', 'collation', 'colored', 'colors', 'come', 'comer', 'comforted', 'coming', 'commanded', 'commonly', 'company', 'compass', 'conducted', 'confused', 'consented', 'consulted', 'contain', 'contrive', 'cooked', 'cord', 'corner', 'could', 'couldst', 'counted', 'country', 'court', 'courtesy', 'cow', 'crack', 'crackle', 'crackling', 'creature', 'crept', 'cried', 'crimes', 'crying', 'cunning', 'cut', 'cutting', 'dance', 'danced', 'dancing', 'dapple', 'dared', 'daughter', 'daughters', 'day', 'days', 'daytime', 'dead', 'dear', 'death', 'deceitful', 'deceiving', 'decked', 'deer', 'delighted', 'den', 'derisively', 'describe', 'described', 'deserts', 'desired', 'determined', 'diamond', 'did', 'die', 'died', 'difficult', 'dinner', 'dirty', 'dishes', 'distance', 'distress', 'diverted', 'doing', 'don', 'done', 'door', 'double', 'doubting', 'down', 'downwards', 'dozen', 'dreamed', 'dress', 'dressed', 'dresses', 'drives', 'dropped', 'drown', 'drunk', 'dry', 'duchesses', 'dug', 'during', 'each', 'eagerly', 'earnestly', 'easily', 'eat', 'eating', 'effect', 'egg', 'eider', 'eldest', 'eleven', 'else', 'embraced', 'employed', 'end', 'enemy', 'englishman', 'enough', 'entirely', 'entrance', 'equipage', 'escape', 'escaped', 'etc', 'even', 'evening', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'evil', 'exactly', 'excellent', 'expected', 'eye', 'eyes', 'face', 'fail', 'fainted', 'fairy', 'faithful', 'far', 'farm', 'farmer', 'fashion', 'fast', 'fat', 'father', 'fear', 'fearsome', 'fee', 'feet', 'fell', 'fellow', 'felt', 'fetched', 'few', 'field', 'fields', 'fifo', 'figure', 'find', 'finding', 'fine', 'finery', 'finest', 'finished', 'fire', 'first', 'fish', 'fishing', 'fit', 'fitted', 'five', 'fled', 'flint', 'floors', 'flowered', 'followed', 'food', 'fool', 'foot', 'footmen', 'for', 'forgave', 'forgot', 'form', 'former', 'found', 'free', 'french', 'friend', 'friends', 'fright', 'fro', 'from', 'front', 'full', 'fum', 'fun', 'furious', 'gaping', 'garden', 'garret', 'gate', 'gather', 'gave', 'gazing', 'gentle', 'gentleman', 'get', 'getting', 'giant', 'gilded', 'girl', 'give', 'giving', 'glad', 'glass', 'glasses', 'godmother', 'going', 'gold', 'golden', 'gone', 'good', 'goodness', 'got', 'governed', 'gowns', 'gracefully', 'gracious', 'grand', 'grass', 'gray', 'great', 'greater', 'green', 'greet', 'grew', 'grief', 'grind', 'groaning', 'growing', 'grown', 'guards', 'guilty', 'had', 'hadst', 'hair', 'hand', 'hands', 'handsome', 'handsomer', 'hanging', 'happened', 'happily', 'happy', 'hard', 'hardly', 'harm', 'harp', 'has', 'haste', 'hasted', 'haughty', 'have', 'having', 'head', 'headdress', 'heads', 'heal', 'healed', 'heard', 'hearing', 'heart', 'heartily', 'heaven', 'heavy', 'heels', 'help', 'helpless', 'hen', 'her', 'here', 'hers', 'herself', 'hid', 'hiding', 'hills', 'hillside', 'him', 'himself', 'his', 'hit', 'hole', 'home', 'homes', 'homewards', 'honorable', 'hoped', 'hopeless', 'hoping', 'horrible', 'horrified', 'horse', 'horses', 'hot', 'house', 'how', 'however', 'howled', 'huge', 'humor', 'hundred', 'hung', 'hungry', 'hurried', 'husband', 'idea', 'ill', 'illness', 'imagine', 'indeed', 'inlaid', 'innocent', 'inside', 'instant', 'instantly', 'instead', 'intention', 'intently', 'into', 'invitation', 'invited', 'ironed', 'its', 'jack', 'jeer', 'jestingly', 'jewels', 'jolly', 'joy', 'just', 'keep', 'kept', 'kill', 'killed', 'kind', 'kindness', 'king', 'kingdom', 'kitchen', 'knew', 'knocked', 'knocking', 'knots', 'know', 'knowing', 'knows', 'labor', 'laced', 'laces', 'ladies', 'lady', 'laid', 'landed', 'language', 'large', 'largest', 'last', 'laugh', 'laughing', 'law', 'lay', 'leapt', 'leather', 'leave', 'leaving', 'led', 'left', 'legs', 'lend', 'length', 'lent', 'less', 'let', 'lie', 'lift', 'lightning', 'like', 'liked', 'likewise', 'linen', 'listened', 'little', 'lived', 'liveries', 'lives', 'lizards', 'lodgings', 'long', 'longer', 'look', 'looked', 'looking', 'loss', 'lost', 'loudly', 'love', 'lovely', 'lying', 'madam', 'made', 'magic', 'magical', 'make', 'malicious', 'man', 'manage', 'manner', 'manteau', 'many', 'market', 'married', 'marry', 'master', 'material', 'matter', 'matters', 'mattresses', 'may', 'mean', 'meanest', 'meanly', 'meanwhile', 'medicine', 'meet', 'meeting', 'mentioned', 'met', 'mice', 'middle', 'midnight', 'might', 'mightily', 'miles', 'milk', 'mind', 'minutes', 'miss', 'misses', 'mixing', 'moment', 'month', 'more', 'morning', 'morsel', 'mortal', 'most', 'mother', 'mountain', 'mountains', 'mouse', 'much', 'murder', 'murdering', 'museum', 'must', 'name', 'nasty', 'natural', 'nature', 'natured', 'nay', 'near', 'nearly', 'neighbor', 'never', 'new', 'newest', 'next', 'nice', 'night', 'nimble', 'nobody', 'noise', 'not', 'nothing', 'notions', 'now', 'nowhere', 'oar', 'obliged', 'odious', 'off', 'offered', 'often', 'ointment', 'old', 'once', 'one', 'ones', 'only', 'open', 'opened', 'oranges', 'order', 'ordered', 'orders', 'ordinary', 'other', 'our', 'out', 'over', 'overtake', 'own', 'owned', 'pain', 'pains', 'pair', 'palace', 'pardon', 'part', 'passed', 'pasted', 'patches', 'patience', 'patiently', 'pattern', 'pay', 'pea', 'peace', 'people', 'pepper', 'perfectly', 'person', 'persons', 'pestle', 'petticoat', 'petticoats', 'piece', 'pieces', 'pinners', 'place', 'plaited', 'plan', 'plans', 'play', 'pleasant', 'please', 'pleased', 'pleasure', 'plight', 'poche', 'pocket', 'poor', 'position', 'possibly', 'pot', 'pounding', 'poured', 'presented', 'prettiest', 'pretty', 'prince', 'princess', 'princesses', 'proclaimed', 'profound', 'promise', 'promised', 'proposal', 'proposed', 'proudest', 'provided', 'pulled', 'pumpkin', 'punishment', 'purpose', 'put', 'putting', 'qualities', 'quality', 'quarters', 'queen', 'quickest', 'quickly', 'quietly', 'quite', 'rabbit', 'race', 'rafters', 'rags', 'rain', 'raised', 'ran', 'rat', 'rats', 'rattled', 'reached', 'real', 'receive', 'recovery', 'red', 'refusal', 'relieve', 'replied', 'rest', 'rested', 'return', 'returned', 'revenge', 'rewarded', 'rice', 'rich', 'richer', 'richly', 'rid', 'right', 'rind', 'rocked', 'rolled', 'room', 'rooms', 'rope', 'rose', 'round', 'rounds', 'row', 'rowed', 'rubbing', 'rude', 'ruffles', 'run', 'ruthless', 'sack', 'sacks', 'sad', 'sadly', 'said', 'same', 'sandals', 'sat', 'sauce', 'saw', 'saying', 'says', 'scalds', 'scarce', 'scarcely', 'scared', 'scooped', 'scoured', 'screaming', 'scrubbed', 'sea', 'seamed', 'seat', 'second', 'securely', 'see', 'seeing', 'seek', 'seemed', 'seen', 'sell', 'sensitive', 'sent', 'served', 'services', 'set', 'shall', 'shalt', 'shape', 'share', 'she', 'shoes', 'shore', 'shorewards', 'short', 'should', 'shouted', 'show', 'showed', 'showing', 'sigh', 'sight', 'silence', 'silly', 'silver', 'simple', 'since', 'singular', 'sinking', 'sister', 'sisters', 'sit', 'six', 'skin', 'skipped', 'sky', 'sleep', 'slender', 'slept', 'slipper', 'slippers', 'smartest', 'smell', 'smiling', 'smoke', 'smooth', 'sobbing', 'soften', 'softly', 'some', 'something', 'sometime', 'son', 'songs', 'soon', 'sooner', 'sore', 'sorry', 'sound', 'soup', 'speak', 'speeches', 'spent', 'spite', 'spoil', 'spoiled', 'sprang', 'spread', 'stand', 'standing', 'started', 'stay', 'stayed', 'stealing', 'steel', 'stepped', 'still', 'stolen', 'stomacher', 'stood', 'stop', 'stopped', 'store', 'storehouse', 'storm', 'story', 'straw', 'strength', 'stretching', 'strike', 'striking', 'strong', 'struck', 'succeeded', 'such', 'suddenly', 'suit', 'sunset', 'sunshine', 'supper', 'sure', 'surprised', 'sweet', 'sweetness', 'tables', 'take', 'taken', 'talked', 'tall', 'tap', 'tears', 'tell', 'telling', 'temper', 'terrible', 'terrified', 'than', 'thank', 'thanked', 'thankful', 'that', 'the', 'their', 'them', 'themselves', 'then', 'there', 'thereupon', 'these', 'they', 'thick', 'things', 'think', 'thinking', 'third', 'this', 'thither', 'those', 'thou', 'though', 'thought', 'thousand', 'three', 'threw', 'through', 'thrust', 'thunder', 'thus', 'tied', 'tightly', 'till', 'time', 'times', 'tiny', 'tire', 'tired', 'tiresome', 'toes', 'together', 'told', 'too', 'took', 'top', 'torrents', 'touched', 'towards', 'town', 'trap', 'trapdoor', 'traps', 'travelled', 'tray', 'treatment', 'trees', 'trial', 'trimming', 'trouble', 'true', 'trumpet', 'trusted', 'truth', 'try', 'trying', 'turned', 'twelve', 'twenty', 'two', 'unavenged', 'uncivil', 'under', 'undergo', 'understood', 'uneasy', 'unkind', 'unknown', 'unlucky', 'untie', 'untied', 'upon', 'upside', 'used', 'usual', 'vain', 'vegetables', 'velvet', 'veranda', 'very', 'violins', 'visit', 'voice', 'wailed', 'wait', 'waited', 'waiting', 'waked', 'wand', 'want', 'wanted', 'was', 'watching', 'water', 'watering', 'wax', 'way', 'wear', 'weary', 'weather', 'wedding', 'well', 'wench', 'went', 'were', 'what', 'whatever', 'when', 'where', 'whereof', 'whereupon', 'whether', 'which', 'while', 'whiskers', 'who', 'whole', 'whom', 'whose', 'why', 'wicked', 'widow', 'wife', 'will', 'willing', 'willingly', 'wily', 'wind', 'window', 'winter', 'wipe', 'wiping', 'wish', 'wishest', 'with', 'without', 'woke', 'woman', 'won', 'wonderful', 'wood', 'wooden', 'woods', 'work', 'worked', 'working', 'world', 'would', 'wouldst', 'wounds', 'wrath', 'wretched', 'wrinkles', 'yellow', 'yes', 'yet', 'you', 'young', 'youngest', 'your']\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "cind = re.findall(r'\\b[a-zA-Z][a-z]{2,9}\\b',cinderella)\n",
    "jack = re.findall(r'\\b[a-zA-Z][a-z]{2,9}\\b',jackandthebeanstalk)\n",
    "farm = re.findall(r'\\b[a-zA-Z][a-z]{2,9}\\b',thefarmerandthebadger)\n",
    "prince = re.findall(r'\\b[a-zA-Z][a-z]{2,9}\\b',theprincessandthepea)\n",
    "\n",
    "bag.extend(cind)\n",
    "bag.extend(jack)\n",
    "bag.extend(farm)\n",
    "bag.extend(prince)\n",
    "\n",
    "vals = list(set(bag))\n",
    "vals.sort()\n",
    "print(vals)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "80f70082",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cinderella</th>\n",
       "      <th>jackandthebeanstalk</th>\n",
       "      <th>thefarmerandthebadger</th>\n",
       "      <th>theprincessandthepea</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>able</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>about</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>above</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>abundantly</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>account</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>yet</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>you</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>young</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>youngest</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>your</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1126 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           cinderella jackandthebeanstalk thefarmerandthebadger  \\\n",
       "able              NaN                 NaN                   NaN   \n",
       "about             NaN                 NaN                   NaN   \n",
       "above             NaN                 NaN                   NaN   \n",
       "abundantly        NaN                 NaN                   NaN   \n",
       "account           NaN                 NaN                   NaN   \n",
       "...               ...                 ...                   ...   \n",
       "yet               NaN                 NaN                   NaN   \n",
       "you               NaN                 NaN                   NaN   \n",
       "young             NaN                 NaN                   NaN   \n",
       "youngest          NaN                 NaN                   NaN   \n",
       "your              NaN                 NaN                   NaN   \n",
       "\n",
       "           theprincessandthepea  \n",
       "able                        NaN  \n",
       "about                       NaN  \n",
       "above                       NaN  \n",
       "abundantly                  NaN  \n",
       "account                     NaN  \n",
       "...                         ...  \n",
       "yet                         NaN  \n",
       "you                         NaN  \n",
       "young                       NaN  \n",
       "youngest                    NaN  \n",
       "your                        NaN  \n",
       "\n",
       "[1126 rows x 4 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "termdf = pd.DataFrame(index = vals, columns = [\"cinderella\",\"jackandthebeanstalk\",\"thefarmerandthebadger\",\"theprincessandthepea\"])\n",
    "termdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "678171ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cinderella</th>\n",
       "      <th>jackandthebeanstalk</th>\n",
       "      <th>thefarmerandthebadger</th>\n",
       "      <th>theprincessandthepea</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>able</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>about</th>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>above</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>abundantly</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>account</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>yet</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>you</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>young</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>youngest</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>your</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1126 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            cinderella  jackandthebeanstalk  thefarmerandthebadger  \\\n",
       "able              True                False                   True   \n",
       "about            False                 True                   True   \n",
       "above             True                False                  False   \n",
       "abundantly        True                False                  False   \n",
       "account           True                False                   True   \n",
       "...                ...                  ...                    ...   \n",
       "yet              False                False                  False   \n",
       "you               True                 True                   True   \n",
       "young             True                False                  False   \n",
       "youngest          True                False                  False   \n",
       "your              True                 True                   True   \n",
       "\n",
       "            theprincessandthepea  \n",
       "able                       False  \n",
       "about                       True  \n",
       "above                      False  \n",
       "abundantly                 False  \n",
       "account                    False  \n",
       "...                          ...  \n",
       "yet                         True  \n",
       "you                        False  \n",
       "young                      False  \n",
       "youngest                   False  \n",
       "your                       False  \n",
       "\n",
       "[1126 rows x 4 columns]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for i, row in termdf.iterrows():\n",
    "    if i in cind:\n",
    "        row['cinderella']=True\n",
    "    if i in jack:\n",
    "        row['jackandthebeanstalk']=True\n",
    "    if i in farm:\n",
    "        row['thefarmerandthebadger']=True\n",
    "    if i in prince:\n",
    "        row['theprincessandthepea']=True\n",
    "        \n",
    "termdf.fillna(False, inplace = True)\n",
    "termdf"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fddf6a17",
   "metadata": {},
   "source": [
    "Perform the following Boolean operations and provide the answer\n",
    "\n",
    "animal AND beautiful"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8746f902",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "thefarmerandthebadger\n"
     ]
    }
   ],
   "source": [
    "columns = [\"cinderella\",\"jackandthebeanstalk\",\"thefarmerandthebadger\",\"theprincessandthepea\"]\n",
    "for i in columns:\n",
    "    if termdf.loc['animal', i] & termdf.loc['beautiful', i]:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c60f4ee",
   "metadata": {},
   "source": [
    "Perform the following Boolean operations and provide the answer\n",
    "\n",
    "badger AND NOT (animal OR country)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "57e5a095",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "cinderella               False\n",
       "jackandthebeanstalk      False\n",
       "thefarmerandthebadger    False\n",
       "theprincessandthepea     False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "termdf.loc['badger', :] & ~(termdf.loc['animal', :] | termdf.loc['country', :])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e592c325",
   "metadata": {},
   "source": [
    "Generate an Inverted Index of the document collection in a similar style, namely posting lists for vocabulary words."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "64bcd608",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cinderella</th>\n",
       "      <th>jackandthebeanstalk</th>\n",
       "      <th>thefarmerandthebadger</th>\n",
       "      <th>theprincessandthepea</th>\n",
       "      <th>postinglist</th>\n",
       "      <th>posting_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>able</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td></td>\n",
       "      <td>[cinderella, thefarmerandthebadger]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>about</th>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td></td>\n",
       "      <td>[jackandthebeanstalk, thefarmerandthebadger, t...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>above</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td></td>\n",
       "      <td>[cinderella]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>abundantly</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td></td>\n",
       "      <td>[cinderella]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>account</th>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td></td>\n",
       "      <td>[cinderella, thefarmerandthebadger]</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            cinderella  jackandthebeanstalk  thefarmerandthebadger  \\\n",
       "able              True                False                   True   \n",
       "about            False                 True                   True   \n",
       "above             True                False                  False   \n",
       "abundantly        True                False                  False   \n",
       "account           True                False                   True   \n",
       "\n",
       "            theprincessandthepea postinglist  \\\n",
       "able                       False               \n",
       "about                       True               \n",
       "above                      False               \n",
       "abundantly                 False               \n",
       "account                    False               \n",
       "\n",
       "                                                 posting_list  \n",
       "able                      [cinderella, thefarmerandthebadger]  \n",
       "about       [jackandthebeanstalk, thefarmerandthebadger, t...  \n",
       "above                                            [cinderella]  \n",
       "abundantly                                       [cinderella]  \n",
       "account                   [cinderella, thefarmerandthebadger]  "
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "termdf['posting_list']=termdf['posting_list'].astype(str)\n",
    "\n",
    "for i, row in termdf.iterrows():\n",
    "    termdf.at[i,'posting_list']=list(termdf.columns[(row ==True)])\n",
    "termdf.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b0c051a",
   "metadata": {},
   "source": [
    "Select appropriate elements which are part of the posting list for the word \"account\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "8542f660",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['cinderella', 'thefarmerandthebadger']"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "termdf.loc['account','posting_list']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa5a1504",
   "metadata": {},
   "source": [
    "Select appropriate elements which are part of the posting list for the word \"asked\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "4d186c20",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['cinderella',\n",
       " 'jackandthebeanstalk',\n",
       " 'thefarmerandthebadger',\n",
       " 'theprincessandthepea']"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "termdf.loc['asked','posting_list']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01fcc338",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
