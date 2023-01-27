## SQL odev 8

1-  test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.

    `CREATE TABLE employee(
        id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        birthdate DATE,
        email VARCHAR(100)
    ); `

2-  Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.

    `
    insert into employee (name, email, birthday) values ('Harrietta Hans', 'hhans0@digg.com', '1950-11-30');
insert into employee (name, email, birthday) values ('Andria Dablin', 'adablin1@mozilla.com', '1976-09-05');
insert into employee (name, email, birthday) values ('Ware Aveling', 'waveling2@europa.eu', '1969-04-15');
insert into employee (name, email, birthday) values ('Lucas Gwinnel', null, '1994-01-22');
insert into employee (name, email, birthday) values ('Nichole Bompass', 'nbompass4@home.pl', '1994-03-07');
insert into employee (name, email, birthday) values ('Meryl Varnes', 'mvarnes5@infoseek.co.jp', '1983-09-24');
insert into employee (name, email, birthday) values ('Giraud Pottes', 'gpottes6@businessweek.com', '1952-02-02');
insert into employee (name, email, birthday) values ('Timmie Matyatin', 'tmatyatin7@sina.com.cn', '1978-11-17');
insert into employee (name, email, birthday) values ('Minne Haskur', 'mhaskur8@mozilla.org', '1941-11-11');
insert into employee (name, email, birthday) values ('Cull Jankovsky', 'cjankovsky9@amazon.de', '1987-05-22');
insert into employee (name, email, birthday) values ('Shandee Cecere', null, '1947-09-20');
insert into employee (name, email, birthday) values ('Darline Duesberry', 'dduesberryb@ehow.com', '1957-04-02');
insert into employee (name, email, birthday) values ('Andra Hattrick', 'ahattrickc@washington.edu', '1963-12-17');
insert into employee (name, email, birthday) values ('Zitella Belson', 'zbelsond@narod.ru', '1967-06-21');
insert into employee (name, email, birthday) values ('Cornie Thornton', 'cthorntone@gmpg.org', '1975-06-23');
insert into employee (name, email, birthday) values ('Edgardo Crandon', 'ecrandonf@ifeng.com', '1992-12-27');
insert into employee (name, email, birthday) values ('Heinrick Ewence', 'hewenceg@t.co', '1987-12-20');
insert into employee (name, email, birthday) values ('Sinclare Tabour', null, '1958-09-10');
insert into employee (name, email, birthday) values ('Lita Yelding', 'lyeldingi@tamu.edu', '1955-06-22');
insert into employee (name, email, birthday) values ('Thibaud Runnalls', 'trunnallsj@freewebs.com', '1955-10-17');
insert into employee (name, email, birthday) values ('Lilas Bedford', 'lbedfordk@howstuffworks.com', '1956-10-11');
insert into employee (name, email, birthday) values ('Theobald Klemke', 'tklemkel@list-manage.com', '1946-06-18');
insert into employee (name, email, birthday) values ('Grady Blooman', 'gbloomanm@smh.com.au', '1959-07-05');
insert into employee (name, email, birthday) values ('Thatcher Pond', 'tpondn@youtu.be', '1974-08-18');
insert into employee (name, email, birthday) values ('Lexi Peepall', null, null);
insert into employee (name, email, birthday) values ('Brant Mulvagh', 'bmulvaghp@live.com', '1952-06-22');
insert into employee (name, email, birthday) values ('Freeland Gryglewski', 'fgryglewskiq@purevolume.com', '1975-06-11');
insert into employee (name, email, birthday) values ('Babbette Linneman', 'blinnemanr@columbia.edu', '1945-04-18');
insert into employee (name, email, birthday) values ('Ephrayim Leather', 'eleathers@pagesperso-orange.fr', '1967-12-15');
insert into employee (name, email, birthday) values ('Derrek Bubbings', 'dbubbingst@de.vu', '1979-12-06');
insert into employee (name, email, birthday) values ('Arden Kingswood', null, '1967-02-22');
insert into employee (name, email, birthday) values ('Malissa Bottoner', 'mbottonerv@phoca.cz', '1971-04-12');
insert into employee (name, email, birthday) values ('Anet Egle of Germany', 'aeglew@typepad.com', '1946-01-16');
insert into employee (name, email, birthday) values ('Matias Ertelt', 'merteltx@tripod.com', '1970-12-31');
insert into employee (name, email, birthday) values ('Ruby Tookill', null, '1948-12-10');
insert into employee (name, email, birthday) values ('Gunner Moppett', 'gmoppettz@is.gd', '1974-07-02');
insert into employee (name, email, birthday) values ('Michal Pechell', 'mpechell10@umich.edu', '1990-08-14');
insert into employee (name, email, birthday) values ('Kayle Carnall', 'kcarnall11@dot.gov', '1941-10-15');
insert into employee (name, email, birthday) values ('Laurence Whereat', 'lwhereat12@google.es', '1954-08-23');
insert into employee (name, email, birthday) values ('Mano Reely', 'mreely13@telegraph.co.uk', '1972-01-30');
insert into employee (name, email, birthday) values ('Brett Brownhall', 'bbrownhall14@cbsnews.com', '1954-09-04');
insert into employee (name, email, birthday) values ('Ford Witheford', 'fwitheford15@rambler.ru', '1953-07-09');
insert into employee (name, email, birthday) values ('Laurianne Grissett', null, '1958-10-26');
insert into employee (name, email, birthday) values ('Nadeen Durnford', 'ndurnford17@whitehouse.gov', '1998-03-25');
insert into employee (name, email, birthday) values ('Pippa Eneas', 'peneas18@imgur.com', '1961-01-31');
insert into employee (name, email, birthday) values ('Fayette Cowdery', 'fcowdery19@biglobe.ne.jp', '1992-03-22');
insert into employee (name, email, birthday) values ('Aylmer Belfit', 'abelfit1a@themeforest.net', '1956-07-07');
insert into employee (name, email, birthday) values ('Matthaeus Billanie', 'mbillanie1b@tuttocitta.it', '1957-07-17');
insert into employee (name, email, birthday) values ('Heinrick Swaden', 'hswaden1c@t.co', '1974-07-19');
insert into employee (name, email, birthday) values ('Alexandra Jaouen', 'ajaouen1d@jigsy.com', '1943-03-05');
`

3-  Sütunların her birine göre diğer sütunları güncelleyecek 1 adet UPDATE işlemi yapalım.
    
    UPDATE employee
    SET name = 'ali veli',
        birthday = '1995-01-11',
        email = 'ali@veli.com'
    WHERE id =1;

4-  Sütunların her birine göre ilgili satırı silecek 1 adet DELETE işlemi yapalım.

    DELETE FROM employee
    WHERE id > 15;