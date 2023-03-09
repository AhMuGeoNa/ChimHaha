import mecabYa from 'https://cdn.jsdelivr.net/npm/mecab-ya@0.1.1/+esm'
var text  = '아버지가방에들어가신다';

mecab.pos(text, function (err, result) {
	console.log(result);
});

mecab.morphs(text, function (err, result){
	console.log(result);
});

mecab.nouns(text, function (err, result){
	console.log(result);
});
