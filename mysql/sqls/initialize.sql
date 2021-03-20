CREATE DATABASE anime_recommender;
USE anime_recommender

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `session_id` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



DROP TABLE IF EXISTS `anime_data`;
CREATE TABLE `anime_data` (
  `anime_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `image` varchar(127),
  `description` text NOT NULL,
  `year` varchar(127) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `company` varchar(255) NOT NULL,
  PRIMARY KEY (`anime_id`),
  UNIQUE KEY `anime_id` (`anime_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `anime_data` WRITE;
/*!40000 ALTER TABLE `anime_data` DISABLE KEYS */;
INSERT INTO `anime_data` VALUES (1,'アーヤと魔女','NULL','ダイアナ・ウィン・ジョーンズによるファンタジー小説、またそれを原作としたスタジオジブリ制作のアニメーション作品。','2020','ファンタジー','スタジオジブリ'),(2,'五等分の花嫁','gotoubunn.jpg','春場ねぎによる日本の漫画作品。','2019','ラブコメディ','	手塚プロダクション'),(3,'PSYCHO-PASS サイコパス 3','psychopass3.jpeg','Production I.G制作による日本のオリジナルテレビアニメ作品、および、これを原作としたメディアミックス作品。','2019秋','SF アクション クライムサスペンス','ProductionI.G'),(4,'鬼滅の刃','kimetsunoyaiba.png','大正時代を舞台に主人公が鬼と化した妹を人間に戻す方法を探すために戦う姿を描く和風剣戟奇譚。','2019','剣劇 ダーク・ファンタジー','ufotable'),(5,'呪術廻戦','jujutukaisen.jpeg','人間の負の感情から生まれる化け物・呪霊を呪術を使って祓う呪術師の闘いを描いた、ダークファンタジー・バトル漫画。','2020秋','ダーク・ファンタジー','MAPPA'),(6,'進撃の巨人','shingeki.png','圧倒的な力を持つ巨人とそれに抗う人間達との戦いを描いたダーク・ファンタジー漫画。','2017','ダークファンタジー アクション','MAPPA'),(7,'ノラと皇女と野良猫ハート','noratokoujoto.jpg','日本のアダルトゲームブランドであるHARUKAZEより2016年2月26日に発売された成人向け美少女ゲーム原作。地上世界に住むごく普通の少年・ノラが、冥界の皇女・パトリシアの魔法によって猫の姿にされてしまうというファンタジー作品。','2017夏','恋愛 学園 ファンタジー','ダブトゥーンスタジオ'),(8,'京都寺町三条のホームズ','kyototeramachisanjo.png','京都へ移り住んで半年になる女子高生の真城葵は、とある事情により亡き祖父の骨董品を鑑定してもらうべく、寺町三条商店街にポツリと佇む骨董品店『蔵』を訪れる。しかしそこで出逢った鑑定士の家頭清貴は美形で上品で柔らかな物腰でありながら、実は「ホームズ」の異名で呼ばれるほど怖ろしく鋭い人物で、葵が骨董品を家族に内緒でこっそり持ち出してきたことをその場で見抜いてしまう。どうしてもお金が必要だった葵に、清貴は『蔵』でアルバイトをしてはどうかと持ち掛け、その日から葵は彼と共に骨董品と京都にまつわる様々な出来事に遭遇していくことに。','2018夏','ミステリー','アニメーションスタジオ・セブン'),(9,'SSSS.GRIDMAN','gridman.jpg','響裕太はある日、クラスメイトの宝多六花の家の前で倒れ、自分の名前を含むすべての記憶を思いだせない状態で目覚める。混乱する裕太は、六花の家が営むジャンクショップに置かれていた古いパソコンから呼びかけて来るハイパーエージェントグリッドマンから、自身の使命を果たすように諭される。裕太は戸惑いながらも日常生活に戻るが、街に謎の怪獣が現れたとき、グリッドマンに導かれるまま彼と合体して怪獣を撃破する。かくして裕太は、六花や友人の内海将とグリッドマン同盟を結成し、怪獣の脅威に立ち向かう。','2018秋','SF','TRIGGER'),(10,'ゴールデンカムイ','goldenkamui.jpg','明治末期、日露戦争終結直後[注 4][注 7] の北海道周辺を舞台とした、金塊をめぐるサバイバルバトル漫画。また戊辰戦争・日露戦争・ロシア革命などの歴史ロマン要素のほか、狩猟・グルメ要素、アイヌなどの民俗文化の紹介要素も併せ持つ。','2018/2020','冒険 歴史 青年漫画','ジェノスタジオ');
/*!40000 ALTER TABLE `anime_data` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `likeunlike`;
CREATE TABLE `likeunlike` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `anime_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `likeunlike` WRITE;
/*!40000 ALTER TABLE `likeunlike` DISABLE KEYS */;
INSERT INTO `likeunlike` VALUES (1,1,1,0,'2021-03-19 22:48:57','2021-03-19 22:49:36'),(2,1,2,2,'2021-03-19 22:48:57','2021-03-19 22:49:36'),(3,1,3,1,'2021-03-19 22:48:57','2021-03-19 22:49:36'),(4,2,2,1,'2021-03-19 22:48:57','2021-03-19 22:49:36'),(5,2,1,1,'2021-03-19 22:48:57','2021-03-19 22:49:36');
/*!40000 ALTER TABLE `likeunlike` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `recommended`;
CREATE TABLE `recommended` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `anime_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `recommended` WRITE;
/*!40000 ALTER TABLE `recommended` DISABLE KEYS */;
INSERT INTO `recommended` VALUES (1,1,3,'2021-03-20 16:36:02','2021-03-20 16:36:02'),(2,1,2,'2021-03-20 16:36:16','2021-03-20 16:36:16'),(3,1,5,'2021-03-20 16:36:22','2021-03-20 16:36:22'),(4,2,2,'2021-03-20 16:36:25','2021-03-20 16:36:25'),(5,2,7,'2021-03-20 16:36:29','2021-03-20 16:36:29');
/*!40000 ALTER TABLE `recommended` ENABLE KEYS */;
UNLOCK TABLES;
