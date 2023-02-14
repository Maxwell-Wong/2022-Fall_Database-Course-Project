use Automobile;
-- 避免产生外键约束冲突，引用外键的表需要先于被引用的表删除

drop table sold;
drop table supply;
drop table vehicle;
drop table model;
drop table brand;
drop table supplier;
drop table customer;
drop table dealer;
drop table manufacturing_plant;
drop table options;


create table brand
    (brand_id     varchar(8),
     brand_name   varchar(20) not null,
      primary key (brand_id)
    );

create table model
    (model_id     varchar(8),
     brand_id     varchar(8),
     model_name   varchar(20) not null,
     body_style   varchar(20),
     primary key (model_id),
     foreign key (brand_id)   references brand (brand_id)
        on delete cascade
    );

create table options
    (option_id    varchar(8),
     color        varchar(20),
     engine       varchar(20),
     transmission varchar(20),
     primary key (option_id)
    );

create table dealer
    (dealer_id    varchar(8),
     dealer_name  varchar(20) not null,
     primary key (dealer_id)
    );

create table customer
    (customer_id      varchar(8),
     customer_name    varchar(20) not null,
     customer_address varchar(30),
     phone            varchar(20),
     gender           varchar(8),
     annual_income    numeric(8,2) check (annual_income >= 0),
     primary key (customer_id)
    );

create table manufacturing_plant
    (plant_id    varchar(8),
     plant_name  varchar(20) not null,
     part_name   varchar(20),
     assembler   bit,
     primary key (plant_id)
    );

create table supplier
    (supplier_id    varchar(8),
     supplier_name  varchar(20) not null,
     part_name      varchar(20),
     primary key (supplier_id)
    );

create table supply
    (supplier_id    varchar(8),
     model_id       varchar(8),
     primary key (supplier_id, model_id),
     foreign key (supplier_id) references supplier (supplier_id)
        on delete cascade,
     foreign key (model_id)   references model (model_id)
        on delete cascade
    );


create table vehicle
    (VIN        varchar(20),
     model_id   varchar(8),
     option_id  varchar(8),
     plant_id   varchar(8),
     dealer_id  varchar(8),
     price 	    numeric(8,2) check (price >= 0),
     stock_date date,
     primary key (VIN),
     foreign key (model_id)  references model (model_id)
        on delete cascade,
     foreign key (option_id) references options (option_id)
        on delete cascade,
     foreign key (plant_id)  references manufacturing_plant (plant_id)
        on delete cascade,
     foreign key (dealer_id) references dealer (dealer_id)
        on delete cascade
    );

    
create table sold
	(VIN              varchar(20),
     customer_id      varchar(8),
     sale_date        date,
	 primary key (VIN, customer_id),
     foreign key (customer_id) references customer (customer_id)
        on delete cascade,
	 foreign key (VIN) references vehicle (VIN)
        on delete cascade
    );


