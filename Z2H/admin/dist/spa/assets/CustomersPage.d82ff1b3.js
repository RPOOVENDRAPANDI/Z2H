import{B as be,c as k,h as pe,E as Ve,b5 as De,by as Ne,A as w,ai as Be,bj as qe,_ as Le,r as o,w as ge,o as he,l as b,v as M,n as m,d as t,a8 as ce,q as v,t as Ue,u as Fe,aM as g,M as te,bn as Te,a9 as Ae,b as Pe,bo as $e,bb as Ie,aa as Re,ab as Ee,m as G,x as y,F as Qe,Q as O}from"./index.9310f85f.js";import{Q as W}from"./QTable.5f112812.js";import{Q as Oe}from"./QPagination.e3ae685e.js";import{Q as Me}from"./QTd.465b47f1.js";import{u as Ce,Q as ye}from"./QSpinnerFacebook.790b63a8.js";import{u as we}from"./axios.e06b1dc4.js";import{e as _e}from"./exportToExcel.602deb22.js";import{Q as je}from"./TouchPan.ae3eb169.js";import{Q as ve}from"./QSelect.b3938c45.js";import{Q as Ge}from"./QScrollArea.3b95b6af.js";import{Q as We}from"./QForm.af538d0b.js";import{u as ze}from"./general.92b80929.js";import"./QList.302166dc.js";import"./QMarkupTable.ddbc83e5.js";import"./format.556c102f.js";import"./touch.3df10340.js";import"./QResizeObserver.79cc6745.js";import"./QScrollObserver.a818bd3f.js";var Ke=be({name:"QBtnGroup",props:{unelevated:Boolean,outline:Boolean,flat:Boolean,rounded:Boolean,square:Boolean,push:Boolean,stretch:Boolean,glossy:Boolean,spread:Boolean},setup(r,{slots:s}){const h=k(()=>{const E=["unelevated","outline","flat","rounded","square","push","stretch","glossy"].filter(S=>r[S]===!0).map(S=>`q-btn-group--${S}`).join(" ");return`q-btn-group row no-wrap${E.length!==0?" "+E:""}`+(r.spread===!0?" q-btn-group--spread":" inline")});return()=>pe("div",{class:h.value},Ve(s.default))}}),Ze=be({name:"QBtnToggle",props:{...De,modelValue:{required:!0},options:{type:Array,required:!0,validator:r=>r.every(s=>("label"in s||"icon"in s||"slot"in s)&&"value"in s)},color:String,textColor:String,toggleColor:{type:String,default:"primary"},toggleTextColor:String,outline:Boolean,flat:Boolean,unelevated:Boolean,rounded:Boolean,push:Boolean,glossy:Boolean,size:String,padding:String,noCaps:Boolean,noWrap:Boolean,dense:Boolean,readonly:Boolean,disable:Boolean,stack:Boolean,stretch:Boolean,spread:Boolean,clearable:Boolean,ripple:{type:[Boolean,Object],default:!0}},emits:["update:modelValue","clear","click"],setup(r,{slots:s,emit:h}){const E=k(()=>r.options.find(c=>c.value===r.modelValue)!==void 0),S=k(()=>({type:"hidden",name:r.name,value:r.modelValue})),V=qe(S),I=k(()=>Ne(r)),L=k(()=>({rounded:r.rounded,dense:r.dense,...I.value})),U=k(()=>r.options.map((c,u)=>{const{attrs:D,value:N,slot:B,...p}=c;return{slot:B,props:{key:u,"aria-pressed":N===r.modelValue?"true":"false",...D,...p,...L.value,disable:r.disable===!0||p.disable===!0,color:N===r.modelValue?f(p,"toggleColor"):f(p,"color"),textColor:N===r.modelValue?f(p,"toggleTextColor"):f(p,"textColor"),noCaps:f(p,"noCaps")===!0,noWrap:f(p,"noWrap")===!0,size:f(p,"size"),padding:f(p,"padding"),ripple:f(p,"ripple"),stack:f(p,"stack")===!0,stretch:f(p,"stretch")===!0,onClick(A){F(N,c,A)}}}}));function F(c,u,D){r.readonly!==!0&&(r.modelValue===c?r.clearable===!0&&(h("update:modelValue",null,null),h("clear")):h("update:modelValue",c,u),h("click",D))}function f(c,u){return c[u]===void 0?r[u]:c[u]}function T(){const c=U.value.map(u=>pe(w,u.props,u.slot!==void 0?s[u.slot]:void 0));return r.name!==void 0&&r.disable!==!0&&E.value===!0&&V(c,"push"),Be(s.default,c)}return()=>pe(Ke,{class:"q-btn-toggle",...I.value,rounded:r.rounded,stretch:r.stretch,glossy:r.glossy,spread:r.spread},T)}});const x=r=>(Re("data-v-dd724c3c"),r=r(),Ee(),r),He=x(()=>v("div",{class:"text-h6 text-bold",style:{color:"#123499"}}," Edit Customer Details ",-1)),Je={class:"text-bold"},Xe={class:"text-green"},Ye=x(()=>v("div",{class:"text-bold q-mt-md"},"Name of the Bank",-1)),el=x(()=>v("div",{class:"text-bold q-mt-md"},"Bank Account Number",-1)),ll=x(()=>v("div",{class:"text-bold q-mt-md"},"Name as in Bank",-1)),tl=x(()=>v("div",{class:"text-bold q-mt-md"},"Bank Branch",-1)),al=x(()=>v("div",{class:"text-bold q-mt-md"},"IFSC Code",-1)),ol=x(()=>v("div",{class:"text-bold q-mt-md"},"City",-1)),nl=x(()=>v("div",{class:"text-bold q-mt-md"},"Town",-1)),rl=x(()=>v("div",{class:"text-bold q-mt-md"},"State",-1)),sl=x(()=>v("div",{class:"text-bold q-mt-md"},"District",-1)),dl=x(()=>v("div",{class:"text-bold q-mt-md"},"Address",-1)),il=x(()=>v("div",{class:"text-bold q-mt-md"},"Pin Code",-1)),ul=x(()=>v("div",{class:"text-bold q-mt-md"},"User Status",-1)),ml={__name:"editCustomerDetailsModal",props:{showEditCustomerPopup:{type:Boolean,required:!0,default:!1},closeEditCustomerPopup:{type:Function,required:!0},selectedData:{type:Object,required:!0}},setup(r){const s=r,h=ze(),E=we(),S=o(s.selectedData[0].account_number),V=o(s.selectedData[0].bank_branch),I=o(s.selectedData[0].ifsc_code),L=o(s.selectedData[0].name_of_bank),U=o(s.selectedData[0].name_as_in_bank),F=o(s.selectedData[0].city),f=o(s.selectedData[0].town),T=o(s.selectedData[0].address),c=o(s.selectedData[0].pin_code),u=o([]),D=o(s.selectedData[0].state),N=o([]),B=o(""),p=o(s.selectedData[0].user_status),A=Ce(),j=k({get:()=>s.showEditCustomerPopup,set:()=>s.closeEditCustomerPopup()}),z=k(()=>{var i;return(i=u.value)==null?void 0:i.map(a=>a.name)}),K=k(()=>{var i;return(i=N.value)==null?void 0:i.map(a=>a.name)}),Z=k(()=>["Active","Inactive"]),H=k(()=>{var a;return((a=u.value)==null?void 0:a.find(l=>l.name==D.value)).uid}),J=k(()=>{var a;return((a=N.value)==null?void 0:a.find(l=>l.name==B.value)).id}),X=k(()=>{let i=_(L.value),a=_(S.value),l=_(U.value),re=_(V.value),se=Y(I.value),ne=_(F.value),de=_(f.value),le=_(T.value),ie=ee(c.value);return!l||!re||!se||!ne||!de||!le||!ie||!a||!i}),ae=()=>{A.loading.show({spinner:ye,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},oe=()=>{A.loading.hide()},Y=i=>/^[A-Z]{4}0([A-Z0-9]{6})$/.test(i.toUpperCase()),ee=i=>i.toString().length==6,P=i=>{s.closeEditCustomerPopup(i)},Q=()=>{h.getAllStates().then(i=>{u.value=i.data,R()})},R=()=>{B.value="";let i={stateUid:H.value};h.getDistrictsForState(i).then(a=>{N.value=a.data,B.value=a.data[0].name})},_=i=>i.trim().length>2,$=()=>{ae();let i={customerUid:s.selectedData[0].customer_uid,bankName:L.value,bankAccountNumber:S.value,nameAsInBank:U.value,bankBranch:V.value,ifscCode:I.value,city:F.value,town:f.value,address:T.value,pinCode:c.value,userStatus:p.value,district:J.value};E.updateCustomerDetails(i).then(a=>{A.notify({message:"Customer Details Updated Successfully!!!",type:"positive",position:"top"}),P(!0)}).catch(a=>{A.notify({message:"Error in updating customer details. Please contact your admin!!!",type:"negative",position:"top"})}).finally(()=>{oe()})};return ge(D,i=>{R()}),he(()=>{Q()}),(i,a)=>(b(),M(Ie,{modelValue:te(j),"onUpdate:modelValue":a[12]||(a[12]=l=>Pe(j)?j.value=l:null),persistent:"",onKeydown:$e(P,["esc"])},{default:m(()=>[t(Ae,{class:"customer-modal q-pl-sm"},{default:m(()=>[t(ce,{class:"row items-center"},{default:m(()=>[He,t(je),t(w,{icon:"close",flat:"",round:"",onClick:P})]),_:1}),t(We,{onSubmit:$},{default:m(()=>[t(Ge,{style:{height:"calc(95vh - 170px)"}},{default:m(()=>[t(ce,null,{default:m(()=>[v("div",Je,[Ue(" Customer - "),v("span",Xe,Fe(`${s.selectedData[0].name} - ${s.selectedData[0].customer_number}`),1)]),Ye,t(g,{modelValue:L.value,"onUpdate:modelValue":a[0]||(a[0]=l=>L.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter name of the Bank",maxlength:"128",rules:[l=>_(l)||"Field is required!!!"]},null,8,["modelValue","rules"]),el,t(g,{modelValue:S.value,"onUpdate:modelValue":a[1]||(a[1]=l=>S.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter an account number",maxlength:"64",onkeypress:"return event.charCode >= 48 && event.charCode <= 57",rules:[l=>_(l)||"Field is required!!!"]},null,8,["modelValue","rules"]),ll,t(g,{modelValue:U.value,"onUpdate:modelValue":a[2]||(a[2]=l=>U.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter name as in bank",maxlength:"256",rules:[l=>_(l)||"Field is required!!!"]},null,8,["modelValue","rules"]),tl,t(g,{modelValue:V.value,"onUpdate:modelValue":a[3]||(a[3]=l=>V.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter a bank branch name",maxlength:"128",rules:[l=>_(l)||"Field is required!!!"]},null,8,["modelValue","rules"]),al,t(g,{modelValue:I.value,"onUpdate:modelValue":a[4]||(a[4]=l=>I.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter a IFSC code",maxlength:"11",rules:[l=>Y(l)||"Enter a Valid IFSC Code!!!"]},null,8,["modelValue","rules"]),ol,t(g,{modelValue:F.value,"onUpdate:modelValue":a[5]||(a[5]=l=>F.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter a City",maxlength:"128",rules:[l=>_(l)||"Field is required!!!"]},null,8,["modelValue","rules"]),nl,t(g,{modelValue:f.value,"onUpdate:modelValue":a[6]||(a[6]=l=>f.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter a Town",maxlength:"128",rules:[l=>_(l)||"Field is required!!!"]},null,8,["modelValue","rules"]),rl,t(ve,{style:{width:"350px"},filled:"",dense:"",modelValue:D.value,"onUpdate:modelValue":a[7]||(a[7]=l=>D.value=l),options:te(z)},null,8,["modelValue","options"]),sl,t(ve,{style:{width:"350px"},filled:"",dense:"",modelValue:B.value,"onUpdate:modelValue":a[8]||(a[8]=l=>B.value=l),options:te(K)},null,8,["modelValue","options"]),dl,t(g,{modelValue:T.value,"onUpdate:modelValue":a[9]||(a[9]=l=>T.value=l),type:"textarea",style:{width:"350px"},outlined:"",dense:"",autofocus:"",rows:"2","input-class":"textarea-input",placeholder:"Enter an Address",rules:[l=>_(l)||"Field is required!!!"]},null,8,["modelValue","rules"]),il,t(g,{modelValue:c.value,"onUpdate:modelValue":a[10]||(a[10]=l=>c.value=l),style:{"max-width":"350px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter the Pincode",maxlength:"6",onkeypress:"return event.charCode >= 48 && event.charCode <= 57",rules:[l=>ee(l)||"Enter a valid Pincode!!!"]},null,8,["modelValue","rules"]),ul,t(ve,{style:{width:"350px"},filled:"",dense:"",modelValue:p.value,"onUpdate:modelValue":a[11]||(a[11]=l=>p.value=l),options:te(Z)},null,8,["modelValue","options"])]),_:1})]),_:1}),t(ce,{class:"row justify-end"},{default:m(()=>[t(Te,{class:"q-px-none"},{default:m(()=>[t(w,{unelevated:"",color:"primary",label:"Save",disable:te(X),type:"submit","no-caps":""},null,8,["disable"])]),_:1})]),_:1})]),_:1})]),_:1})]),_:1},8,["modelValue","onKeydown"]))}};var cl=Le(ml,[["__scopeId","data-v-dd724c3c"]]);const vl={style:{"margin-top":"30px"},class:"q-ml-md q-mr-lg q-pa-md"},pl={key:0,style:{"margin-top":"30px"},class:"q-ml-md q-mr-lg q-pa-md"},fl={class:"row justify-start items-center"},_l=v("span",{class:"q-ml-sm"},null,-1),bl={class:"q-pa-lg flex flex-center"},gl={key:1,class:"q-ml-md q-mr-lg q-pa-md"},hl={key:2,class:"q-ml-md q-mr-lg q-pa-md"},Cl={key:3,class:"q-ml-md q-mr-lg q-pa-md"},yl={key:4,class:"q-ml-md q-mr-lg q-pa-md"},wl={key:5,style:{"margin-top":"30px"},class:"q-ml-md q-mr-lg q-pa-md"},kl={class:"row justify-start items-center"},xl=v("span",{class:"q-ml-sm"},null,-1),Ml={__name:"CustomersPage",setup(r){const s=we(),h=Ce();let E=[{name:"customerNumber",required:!0,label:"Customer Number",align:"left",field:d=>d.customer_number,format:d=>`${d}`,sortable:!0},{name:"name",label:"Customer Name",field:"name",align:"center"},{name:"dob",label:"Date of birth",field:"date_of_birth",align:"center"},{name:"emailAddress",label:"Email Address",field:"email_address",align:"center"},{name:"gender",label:"Gender",field:"gender",align:"center"},{name:"plan",label:"Plan Name",field:"plan",align:"center"},{name:"planStartDate",label:"Customer Registration Date",field:"plan_start_date",sortable:!0,align:"center"},{name:"mobileNumber",label:"Mobile Number",field:"mobile_number",align:"center"},{name:"nomineeName",label:"Nominee Name",field:"nominee_name",align:"center"},{name:"aadharNumber",label:"Aadhar Number",field:"aadhar_number",align:"center"},{name:"pan",label:"PAN",field:"pan",align:"center"},{name:"city",label:"City",field:"city",align:"center"},{name:"town",label:"Town",field:"town",align:"center"},{name:"district",label:"District",field:"district",sortable:!0,align:"center"},{name:"state",label:"State",field:"state",sortable:!0,align:"center"},{name:"address",label:"Address",field:"address",align:"center"},{name:"pinCode",label:"Pin Code",field:"pin_code",align:"center"},{name:"nameOfBank",label:"Name of Bank",field:"name_of_bank",align:"center"},{name:"nameAsInBank",label:"Name as in Bank",field:"name_as_in_bank",align:"center"},{name:"ifscCode",label:"IFSC Code",field:"ifsc_code",align:"center"},{name:"bankBranch",label:"Bank Branch",field:"bank_branch",align:"center"},{name:"accountNumber",label:"Account Number",field:"account_number",align:"center"},{name:"referrerId",label:"Referrrer Id",field:"referrer_id",align:"center"},{name:"referrerName",label:"Referrer Name",field:"referrer_name",align:"center"},{name:"orderNumber",label:"Order Number",field:"order_number",align:"center"},{name:"productName",label:"Product Name",field:"product_name",align:"center"},{name:"deliveryThrough",label:"Courier Name",field:"delivery_through",align:"center"},{name:"deliveryNumber",label:"Courier Number",field:"delivery_number",align:"center"},{name:"courierDate",label:"Courier Date",field:"courier_date",align:"center"},{name:"deliveryDate",label:"Delivery Date",field:"delivery_date",align:"center"},{name:"orderStatus",label:"Courier Status",field:"order_status",sortable:!0,align:"center"},{name:"paymentDate",label:"Payment Date",field:"payment_date",align:"center"},{name:"paymentMode",label:"Payment Mode",field:"payment_mode",align:"center"},{name:"paymentReference",label:"Payment Reference",field:"payment_reference",align:"center"},{name:"paymentStatus",label:"Payment Status",field:"payment_status",sortable:!0,align:"center"},{name:"levelOneCount",label:"Level One Count",field:"level_one_count",align:"center"},{name:"levelOneCompleted",label:"Level One Status",field:"level_one_completed",sortable:!0,align:"center"},{name:"levelOneCompletedDate",label:"Level One Completed Date",field:"level_one_completed_date",align:"center"},{name:"levelOneCommission",label:"Level One Commission",field:"level_one_commission_status",sortable:!0,align:"center"},{name:"levelTwoCount",label:"Level Two Count",field:"level_two_count",align:"center"},{name:"levelTwoCompleted",label:"Level Two Status",field:"level_two_completed",sortable:!0,align:"center"},{name:"levelTwoCompletedDate",label:"Level Two Completed Date",field:"level_two_completed_date",align:"center"},{name:"levelTwoCommission",label:"Level Two Commission",field:"level_two_commission_status",sortable:!0,align:"center"},{name:"levelThreeCount",label:"Level Three Count",field:"level_three_count",align:"center"},{name:"levelThreeCompleted",label:"Level Three Status",field:"level_three_completed",sortable:!0,align:"center"},{name:"levelThreeCompletedDate",label:"Level Three Completed Date",field:"level_three_completed_date",align:"center"},{name:"levelThreeCommission",label:"Level Three Commission",field:"level_three_commission_status",sortable:!0,align:"center"},{name:"levelFourCount",label:"Level Four Count",field:"level_four_count",align:"center"},{name:"levelFourCompleted",label:"Level Four Status",field:"level_four_completed",sortable:!0,align:"center"},{name:"levelFourCompletedDate",label:"Level Four Completed Date",field:"level_four_completed_date",align:"center"},{name:"levelFourCommission",label:"Level Four Commission",field:"level_four_commission_status",sortable:!0,align:"center"},{name:"userStatus",label:"User Status",field:"user_status",sortable:!0,align:"center"}],S=[{name:"name",required:!0,label:"name",align:"left",field:d=>d.name,format:d=>`${d}`,sortable:!0},{name:"registredDate",label:"Registered Date",field:"registered_date",align:"center"},{name:"dob",label:"Date of birth",field:"date_of_birth",align:"center"},{name:"gender",label:"Gender",field:"gender",align:"center"},{name:"mobileNumber",label:"Mobile Number",field:"mobile_number",align:"center"},{name:"nomineeName",label:"Nominee Name",field:"nominee_name",align:"center"},{name:"aadharNumber",label:"Aadhar Number",field:"aadhar_number",align:"center"},{name:"pan",label:"PAN",field:"pan",align:"center"},{name:"city",label:"City",field:"city",align:"center"},{name:"town",label:"Town",field:"town",align:"center"},{name:"district",label:"District",field:"district",sortable:!0,align:"center"},{name:"state",label:"State",field:"state",sortable:!0,align:"center"},{name:"address",label:"Address",field:"address",align:"center"},{name:"pinCode",label:"Pin Code",field:"pin_code",align:"center"},{name:"nameOfBank",label:"Name of Bank",field:"name_of_bank",align:"center"},{name:"nameAsInBank",label:"Name as in Bank",field:"name_as_in_bank",align:"center"},{name:"ifscCode",label:"IFSC Code",field:"ifsc_code",align:"center"},{name:"bankBranch",label:"Bank Branch",field:"bank_branch",align:"center"},{name:"accountNumber",label:"Account Number",field:"account_number",align:"center"},{name:"referrerId",label:"Referrrer Id",field:"referrer_id",align:"center"},{name:"referrerName",label:"Referrer Name",field:"referrer_name",align:"center"},{name:"actions",label:"Actions",field:"",align:"center"}];const V=o(E),I=o(S),L=o([]),U=o([]),F=o([]),f=o([]),T=o([]),c=o([]),u=o([]),D=o(""),N=o(""),B=o(""),p=o(""),A=o(""),j=o(""),z=o(!1),K=o(!1),Z=o(!1),H=o(!1),J=o(!1),X=o(!1),ae=o(""),oe=o(""),Y=o(""),ee=o(""),P=o(!1),Q=o(!1),R=o({page:1,rowsPerPage:5,rowsNumber:10,totalPages:30}),_=o([{label:"Customers",value:"customers"},{label:"Registered Users",value:"registeredUsers"}]),$=o("customers"),i=()=>{h.loading.show({spinner:ye,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},a=()=>{h.loading.hide()},l=()=>{Q.value=!0},re=d=>{Q.value=!1,d===!0&&(u.value=[],le())},se=d=>{let e={registerUserUid:d.row.uid};s.deleteRegisteredUser(e).then(n=>{ne(),h.notify({message:"Registered User Deleted Successfully!!!",type:"positive",position:"top"})}).catch(n=>{h.notify({message:"Something went Wrong. Please contact your admin!!!",type:"negative",position:"top"})}).finally(()=>{})},ne=()=>{i(),s.getRegisteredUsers().then(d=>{let e=d.data;U.value=e.data}).catch(d=>{console.log("err",d)}).finally(()=>{a()})},de=d=>{R.value.page=d,le()},le=()=>{let d={page:R.value.page,rowsPerPage:R.value.rowsPerPage};i(),s.getCustomersList(d).then(e=>{var fe;let n=(fe=e.data)==null?void 0:fe.data,ue=[];for(let me of n){let q=me.order_details[0],Se=q.order_items[0];delete me.order_details;let C={...me};C.order_number=q.order_number,C.delivery_through=q.delivery_through,C.delivery_number=q.delivery_number,C.courier_date=q.courier_date,C.delivery_date=q.delivery_date,C.order_status=q.order_status,C.payment_date=q.payment_date,C.payment_mode=q.payment_mode,C.payment_reference=q.payment_reference,C.payment_status=q.payment_status,C.product_name=Se.product_name,delete C.order_items,ue.push(C)}L.value=ue,ne()}).catch(e=>{console.log("errror",e)}).finally(()=>{a()})},ie=()=>{i();let d=u.value[0].customer_uid;ae.value=`First Level Customers Under ${u.value[0].name}`,oe.value=`Second Level Customers Under ${u.value[0].name}`,Y.value=`Third Level Customers Under ${u.value[0].name}`,ee.value=`Fourth Level Customers Under ${u.value[0].name}`,s.getCustomerDetails(d).then(e=>{let n=e.data;F.value=n.first_level_customers,f.value=n.second_level_customers,T.value=n.third_level_customers,c.value=n.fourth_level_customers,P.value=!0}).catch(e=>{console.log("error",e)}).finally(()=>{a()})},ke=()=>{let d=[];for(let e of L.value){let n={"Customer Name":e.name,"Customer Number":e.customer_number,"Date of Birth":e.date_of_birth,"Email Address":e.email_address,Gender:e.gender,"Plan Name":e.plan,"Customer Registration Date":e.plan_start_date,"Mobile Number":e.mobile_number,"Nominee Name":e.nominee_name,"Aadhar Name":e.aadhar_number,PAN:e.pan,City:e.city,Town:e.town,District:e.district,State:e.state,Address:e.address,"Pin Code":e.pin_code,"Name of Bank":e.name_of_bank,"Name as in Bank":e.name_as_in_bank,"IFSC Code":e.ifsc_code,"Bank Branch":e.bank_branch,"Account Number":e.account_number,"Referrer Id":e.referrer_id,"Referrer Name":e.referrer_name,"Order Number":e.order_number,"Product Name":e.product_name,"Courier Name":e.delivery_through,"Courier Number":e.delivery_number,"Courier Date":e.courier_date,"Delivery Date":e.delivery_date,"Courier Status":e.order_status,"Payment Date":e.payment_date,"Payment Mode":e.payment_mode,"Payment Reference":e.payment_reference,"Payment Status":e.payment_status,"Level One Count":e.level_one_count,"Level One Status":e.level_one_completed,"Level One Completed Date":e.level_one_completed_date,"Level One Commission":e.level_one_commission_status,"Level Two Count":e.level_two_count,"Level Tow Status":e.level_two_completed,"Level Two Completed Date":e.level_two_completed_date,"Level Two Commission":e.level_two_commission_status,"Level Three Count":e.level_three_count,"Level Three Status":e.level_three_completed,"Level Three Completed Date":e.level_three_completed_date,"Level Three Commission":e.level_three_commission_status,"Level Four Count":e.level_four_count,"Level Four Status":e.level_four_completed,"Level Four Completed Date":e.level_four_completed_date,"Level Four Commission":e.level_four_commission_status,"User Status":e.user_status};d.push(n)}_e(d,"Customers.xlsx")},xe=()=>{let d=[];for(let e of U.value){let n={"Register User Name":e.name,"Registered Date":e.registered_date,"Date of Birth":e.date_of_birth,Gender:e.gender,"Mobile Number":e.mobile_number,"Nominee Name":e.nominee_name,"Aadhar Name":e.aadhar_number,PAN:e.pan,City:e.city,Town:e.town,District:e.district,State:e.state,Address:e.address,"Pin Code":e.pin_code,"Name of Bank":e.name_of_bank,"Name as in Bank":e.name_as_in_bank,"IFSC Code":e.ifsc_code,"Bank Branch":e.bank_branch,"Account Number":e.account_number,"Referrer Id":e.referrer_id,"Referrer Name":e.referrer_name};d.push(n)}_e(d,"Registered_Users.xlsx")};return ge(u,d=>{d.length?ie():(F.value=[],f.value=[],T.value=[],c.value=[],P.value=!1)}),he(()=>{le()}),(d,e)=>(b(),G(Qe,null,[v("div",vl,[v("div",null,[t(Ze,{modelValue:$.value,"onUpdate:modelValue":e[0]||(e[0]=n=>$.value=n),push:"",glossy:"","toggle-color":"primary",options:_.value,"no-caps":""},null,8,["modelValue","options"])])]),$.value==="customers"?(b(),G("div",pl,[t(w,{color:"green",class:"q-mb-md",style:{width:"20px"},"no-caps":"",onClick:ke},{default:m(()=>[v("div",fl,[t(O,{name:"fas fa-file-excel"}),_l])]),_:1}),t(W,{class:"customers-table",flat:"",bordered:"",title:"Customers",rows:L.value,columns:V.value,"row-key":"customer_number",selection:"single",selected:u.value,"onUpdate:selected":e[3]||(e[3]=n=>u.value=n),filter:D.value},{"top-right":m(()=>[z.value?(b(),M(g,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:D.value,"onUpdate:modelValue":e[1]||(e[1]=n=>D.value=n),placeholder:"Search"},{append:m(()=>[t(O,{name:"search"})]),_:1},8,["modelValue"])):y("",!0),t(w,{class:"q-ml-sm",icon:"filter_list",onClick:e[2]||(e[2]=n=>z.value=!z.value),flat:""})]),_:1},8,["rows","columns","selected","filter"]),v("div",bl,[t(Oe,{modelValue:R.value.page,"onUpdate:modelValue":[e[4]||(e[4]=n=>R.value.page=n),de],max:R.value.totalPages,"max-pages":6,"boundary-numbers":!0,ellipses:!0},null,8,["modelValue","max"])]),t(w,{class:"q-mt-md",color:"primary",label:"Edit",disable:!u.value.length,onClick:l},null,8,["disable"])])):y("",!0),P.value&&$.value==="customers"?(b(),G("div",gl,[t(W,{class:"customers-table",flat:"",bordered:"",title:ae.value,rows:F.value,columns:V.value,"row-key":"name",filter:N.value},{"top-right":m(()=>[K.value?(b(),M(g,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:N.value,"onUpdate:modelValue":e[5]||(e[5]=n=>N.value=n),placeholder:"Search"},{append:m(()=>[t(O,{name:"search"})]),_:1},8,["modelValue"])):y("",!0),t(w,{class:"q-ml-sm",icon:"filter_list",onClick:e[6]||(e[6]=n=>K.value=!K.value),flat:""})]),_:1},8,["title","rows","columns","filter"])])):y("",!0),P.value&&$.value==="customers"?(b(),G("div",hl,[t(W,{class:"customers-table",flat:"",bordered:"",title:oe.value,rows:f.value,columns:V.value,"row-key":"name",filter:B.value},{"top-right":m(()=>[Z.value?(b(),M(g,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:B.value,"onUpdate:modelValue":e[7]||(e[7]=n=>B.value=n),placeholder:"Search"},{append:m(()=>[t(O,{name:"search"})]),_:1},8,["modelValue"])):y("",!0),t(w,{class:"q-ml-sm",icon:"filter_list",onClick:e[8]||(e[8]=n=>Z.value=!Z.value),flat:""})]),_:1},8,["title","rows","columns","filter"])])):y("",!0),P.value&&$.value==="customers"?(b(),G("div",Cl,[t(W,{class:"customers-table",flat:"",bordered:"",title:Y.value,rows:T.value,columns:V.value,"row-key":"name",filter:p.value},{"top-right":m(()=>[H.value?(b(),M(g,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:p.value,"onUpdate:modelValue":e[9]||(e[9]=n=>p.value=n),placeholder:"Search"},{append:m(()=>[t(O,{name:"search"})]),_:1},8,["modelValue"])):y("",!0),t(w,{class:"q-ml-sm",icon:"filter_list",onClick:e[10]||(e[10]=n=>H.value=!H.value),flat:""})]),_:1},8,["title","rows","columns","filter"])])):y("",!0),P.value&&$.value==="customers"?(b(),G("div",yl,[t(W,{class:"customers-table",flat:"",bordered:"",title:ee.value,rows:c.value,columns:V.value,"row-key":"name",filter:A.value},{"top-right":m(()=>[J.value?(b(),M(g,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:A.value,"onUpdate:modelValue":e[11]||(e[11]=n=>A.value=n),placeholder:"Search"},{append:m(()=>[t(O,{name:"search"})]),_:1},8,["modelValue"])):y("",!0),t(w,{class:"q-ml-sm",icon:"filter_list",onClick:e[12]||(e[12]=n=>J.value=!J.value),flat:""})]),_:1},8,["title","rows","columns","filter"])])):y("",!0),$.value==="registeredUsers"?(b(),G("div",wl,[t(w,{color:"green",class:"q-mb-md",style:{width:"20px"},"no-caps":"",onClick:xe},{default:m(()=>[v("div",kl,[t(O,{name:"fas fa-file-excel"}),xl])]),_:1}),t(W,{class:"registered-users-table",flat:"",bordered:"",title:"Registered Users",rows:U.value,columns:I.value,"row-key":"name",filter:j.value},{"top-right":m(()=>[X.value?(b(),M(g,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:j.value,"onUpdate:modelValue":e[13]||(e[13]=n=>j.value=n),placeholder:"Search"},{append:m(()=>[t(O,{name:"search"})]),_:1},8,["modelValue"])):y("",!0),t(w,{class:"q-ml-sm q-mr-sm",icon:"filter_list",onClick:e[14]||(e[14]=n=>X.value=!X.value),flat:""})]),"body-cell-actions":m(n=>[t(Me,{props:n},{default:m(()=>[t(w,{style:{color:"#990f02"},dense:"",round:"",flat:"",onClick:ue=>se(n),icon:"delete"},null,8,["onClick"])]),_:2},1032,["props"])]),_:1},8,["rows","columns","filter"])])):y("",!0),Q.value?(b(),M(cl,{key:6,modelValue:Q.value,"onUpdate:modelValue":e[15]||(e[15]=n=>Q.value=n),"show-edit-customer-popup":Q.value,"close-edit-customer-popup":re,"selected-data":u.value},null,8,["modelValue","show-edit-customer-popup","selected-data"])):y("",!0)],64))}};export{Ml as default};
