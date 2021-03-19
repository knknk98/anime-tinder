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
INSERT INTO `anime_data` VALUES (1,'アーヤと魔女','NULL','ダイアナ・ウィン・ジョーンズによるファンタジー小説、またそれを原作としたスタジオジブリ制作のアニメーション作品。','2020','ファンタジー','スタジオジブリ'),(2,'五等分の花嫁','gotoubunn.jpeg','春場ねぎによる日本の漫画作品。','2019','ラブコメディ','	手塚プロダクション'),(3,'PSYCHO-PASS サイコパス 3','psychopass3.jpeg','Production I.G制作による日本のオリジナルテレビアニメ作品、および、これを原作としたメディアミックス作品。','2019秋','SF アクション クライムサスペンス','ProductionI.G'),(4,'鬼滅の刃','kimetsunoyaiba.png','大正時代を舞台に主人公が鬼と化した妹を人間に戻す方法を探すために戦う姿を描く和風剣戟奇譚。','2019','剣劇 ダーク・ファンタジー','ufotable'),(5,'呪術廻戦','jujutukaisen.jpeg','人間の負の感情から生まれる化け物・呪霊を呪術を使って祓う呪術師の闘いを描いた、ダークファンタジー・バトル漫画。','2020秋','ダーク・ファンタジー','MAPPA');
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
