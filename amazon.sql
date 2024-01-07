create database amazon;
use amazon;
drop table User_details;
show tables;
create table User_details(
name varchar(10),
password varchar(20),
mail varchar(40),
phone varchar(50),
address varchar(50));
insert into User_details (name, password, mail, phone, address)
values ("Anish","Anish123","anish22@gmail.com","12345","Chennai"),
("Vinu","Vinu123","vinu@gmail.com","09876","Trichy");
select *
from User_details;
create table e_items(
ename varchar(100), 
price int) ;
insert into e_items(ename,price)
values("Gaming Laptops", 75000),
("Mobile phones", 50000),
("Headsets",15000);
select *
from e_items;
create table orderdetails(
name varchar(50),
item varchar(50),
totalcost int);
select *
from orderdetails;