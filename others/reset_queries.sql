delete from public.user_registeruser where id > 1;
delete from public.user_z2hcustomers where id > 1;
delete from public.app_z2horderitems where id > 0;
delete from public.app_z2horders where id > 0;
delete from public.authtoken_token where user_id > 1;
delete from public.user_z2huser where id > 1;
delete from public.app_z2hproducts where id > 0;
delete from public.app_z2hproductimages where id > 0;
delete from public.app_z2hproductsubcategories where id > 0;
delete from public.app_z2hproductcategories where id > 0;
delete from public.app_z2hproductsreturned where id > 0;


alter sequence user_registeruser_id_seq restart with 2;
alter sequence user_z2hcustomers_id_seq restart with 2;
alter sequence app_z2horderitems_id_seq restart with 1;
alter sequence app_z2horders_id_seq restart with 1;
alter sequence user_z2huser_id_seq restart with 2;
alter sequence app_z2hproducts_id_seq restart with 1;
alter sequence app_z2hproductimages_id_seq restart with 1;
alter sequence app_z2hproductsubcategories_id_seq restart with 1;
alter sequence app_z2hproductcategories_id_seq restart with 1;
alter sequence app_z2hproductsreturned_id_seq restart with 1;


update public.utils_z2hsettings set value = '1' where name in (
	'order_number_sequence','order_item_number_sequence', 'product_category_sequence', 'product_sub_category_sequence', 'prod_code_sequence'
);
update public.utils_z2hsettings set value = '101' where name = 'customer_number_value';

update public.user_z2hcustomers 
	set is_level_one_completed = false,
		is_level_two_completed = false,
		is_level_three_completed = false,
		is_level_four_completed = false,
		is_level_one_commission_paid = false,
		is_level_two_commission_paid = false,
		is_level_three_commission_paid = false,
		is_level_four_commission_paid = false,
		level_one_commission_details = '{}',
		level_two_commission_details = '{}',
		level_three_commission_details = '{}',
		level_four_commission_details = '{}',
		level_one_completed_date = null,
		level_two_completed_date = null,
		level_three_completed_date = null,
		level_four_completed_date = null,
		level_one_commission_paid_date = null,
		level_two_commission_paid_date = null,
		level_three_commission_paid_date = null,
		level_four_commission_paid_date = null
where
	id = 1;