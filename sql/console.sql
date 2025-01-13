--Создание таблицы - плохой дизайн без первичного ключа
create table users (
    first_name varchar(100),
    last_name varchar(100),
    age int,
    occupation text
);

--изменение структуры
alter table users add phone_number char(11);

--наполнение
insert into users (first_name, last_name, age, occupation, phone_number)
values ('nursultan', 'zhantuar', 18, 'IT student', '87083485021');

insert into users (first_name, last_name, age, occupation)
values ('lionel', 'messi', 38, 'Soccer player');

insert into users
values ('john', 'doe', 21, 'Architector', '8701XXXXXXX');

--выборка
select * from users;

--изменение данных
update users set phone_number='8701XXXXXXX'; --updates everything

update users set phone_number='87083485021'
             where first_name='nursultan'; --updates only me)


--Безусловное удаление на примере таблицы мусора
create table trash (
    type varchar(100),
    year int
);

insert into trash (type, year)
values ('old books', 2001), ('food leftovers', 2024), ('old pc', 1984);

delete from trash; --само удаление

select * from trash;

drop table trash; --удаление всееей таблицы

--Удаление с условием
select * from users;

delete from users where first_name = 'john'; --само удаление

--Важность Первичного ключа
drop table users;

create table users (
    id int primary key,
    first_name varchar(100),
    last_name varchar(100),
    age int,
    occupation text
);

alter table users add phone_number char(11);

insert into users (id, first_name, last_name, age, occupation, phone_number)
values (1, 'nursultan', 'zhantuar', 18, 'IT student', '87083485021');

insert into users (id, first_name, last_name, age, occupation)
values (2,'lionel', 'messi', 38, 'Soccer player');

select * from users;

insert into users (id, first_name, last_name, age, occupation)
values (3, 'hans', 'zimmer', 60, 'Composer');

insert into users (id, first_name, last_name, age, occupation)
values (4, 'hans', 'zimmer', 60, 'Tractor driver');

insert into users (id, first_name, last_name, age, occupation)
values (5, 'hans', 'zimmer', 60, 'Cook');

select * from users;

--непрофессиональное удаление)
delete from users
       where first_name = 'hans'
         and last_name = 'zimmer'
         and occupation != 'Composer';

--Select
select * from users;

--условия
select * from users where age > 30;

select * from users where (age > 30 and length(first_name) > 5) or (occupation = 'IT student');

--between
select * from users where age between 30 and 50;

--like
insert into users (id, first_name, last_name, age, occupation)
values (4, 'ludwig', 'van bethhoven', 50, 'Composer');


select * from users where first_name like 'l%';
select * from users where last_name like '%r';
select * from users where last_name like '%ar' or last_name like '%er';

insert into users (id, first_name, last_name, age, occupation)
values (5, 'henry', 'ford', 70, 'Engineer');

update users set age = 60 where id = 5;

select * from users where first_name like 'h___'; --only zimmer
select * from users where first_name like 'h%'; --zimmer and ford




--GROUP BY
select age, count(*) from users where age > 30 group by age;

select age, count(*) from users group by age having count(*) > 1;


--ORDER BY
insert into users (id, first_name, last_name, age, occupation)
values (6, 'john', 'ford', 20, 'Florist');

update users set phone_number = '87475164230' where id = 6;

select * from users order by last_name, age;

select * from users order by phone_number nulls last;