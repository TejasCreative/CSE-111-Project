DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS guild;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS punishments;
DROP TABLE IF EXISTS friends;
DROP TABLE IF EXISTS player_game;
DROP TABLE IF EXISTS duels;
DROP TABLE IF EXISTS bedwars;
DROP TABLE IF EXISTS skywars;


CREATE TABLE player (
    p_name char(50) not null,
    p_uuid char(100) not null,
    p_rank char(50) not null,
    p_joindate date not null,
    p_level decimal(10,0) not null
);

CREATE TABLE guild (
    g_name char(50) not null,
    g_uuid char(100) not null,
    g_members decimal(10,0) not null,
    g_level decimal(10,0) not null,
    g_creationdate date not null,
    g_tag char(10) not null
);

CREATE TABLE pets(
    pt_name char(50) not null,
    pt_level decimal(10,0) not null,
    pt_owner char(100) not null
);

CREATE TABLE friends (
    f_player char(100) not null,
    f_friend char(100) not null
);

CREATE TABLE punishments (
    pu_player char(100) not null,
    pu_duration decimal(10,0) not null,
    pu_type char(50) not null
    

);


CREATE TABLE playergame(
    pl_player char(100) not null,
    pl_gameUUID char(100) not null

);


CREATE TABLE duels(
    d_gameUUID char(100) not null,
    d_coins decimal(10,0) not null,
    d_level decimal(10,0) not null,
    d_kills decimal(10,0) not null,
    d_deaths decimal(10,0) not null,
    d_wins decimal(10,0) not null,
    d_prestige decimal(10,0) not null
);

CREATE TABLE bedwars(
    b_gameUUID char(100) not null,
    b_coins decimal(10,0) not null,
    b_level decimal(10,0) not null,
    b_kills decimal(10,0) not null,
    b_deaths decimal(10,0) not null,
    b_wins decimal(10,0) not null,
    b_prestige decimal(10,0) not null
);

CREATE TABLE skywars(
    s_gameUUID char(100) not null,
    s_coins decimal(10,0) not null,
    s_level decimal(10,0) not null,
    s_kills decimal(10,0) not null,
    s_deaths decimal(10,0) not null,
    s_wins decimal(10,0) not null,
    s_prestige decimal(10,0) not null
);