import{B as we,C as Ce,bz as Ve,D as Oe,c as s,r as p,w as de,bA as re,bB as Pe,aB as qe,h as X,aM as Q,g as Te,A as I,_ as ue,o as Ne,l as M,v as Y,n as f,d as r,a8 as Z,q as c,t as ie,u as ce,M as V,bn as me,a9 as ve,b as pe,bo as be,bb as fe,aa as ge,ab as _e,L as ke,m as oe,x as W,F as Ie,Q as te}from"./index.c822f9b0.js";import{Q as ye,j as Ue}from"./QSelect.30415dcc.js";import{Q as Fe}from"./QTd.97012c36.js";import{Q as ne}from"./QTable.c6a0c61c.js";import{c as Ae}from"./format.65b096e9.js";import{u as he,Q as Se}from"./QSpinnerFacebook.173d39e4.js";import{u as De}from"./general.63b38c23.js";import{e as $e}from"./exportToExcel.602deb22.js";import{Q as Be}from"./TouchPan.54530d87.js";import{Q as Me}from"./QScrollArea.fcae44dc.js";import{Q as Qe}from"./QForm.5279d460.js";import{Q as Re}from"./QFile.60e2c95e.js";import{_ as se}from"./CustomTooltip.085e5943.js";import"./QList.df78d7a2.js";import"./QMarkupTable.64b2e607.js";import"./axios.2c985eff.js";import"./touch.3df10340.js";import"./QResizeObserver.230413fd.js";import"./QScrollObserver.88406e47.js";function le(e,n){return[!0,!1].includes(e)?e:n}var Ee=we({name:"QPagination",props:{...Ce,modelValue:{type:Number,required:!0},min:{type:[Number,String],default:1},max:{type:[Number,String],required:!0},maxPages:{type:[Number,String],default:0,validator:e=>(typeof e=="string"?parseInt(e,10):e)>=0},inputStyle:[Array,String,Object],inputClass:[Array,String,Object],size:String,disable:Boolean,input:Boolean,iconPrev:String,iconNext:String,iconFirst:String,iconLast:String,toFn:Function,boundaryLinks:{type:Boolean,default:null},boundaryNumbers:{type:Boolean,default:null},directionLinks:{type:Boolean,default:null},ellipses:{type:Boolean,default:null},ripple:{type:[Boolean,Object],default:null},round:Boolean,rounded:Boolean,flat:Boolean,outline:Boolean,unelevated:Boolean,push:Boolean,glossy:Boolean,color:{type:String,default:"primary"},textColor:String,activeDesign:{type:String,default:"",values:e=>e===""||Ve.includes(e)},activeColor:String,activeTextColor:String,gutter:String,padding:{type:String,default:"3px 2px"}},emits:["update:modelValue"],setup(e,{emit:n}){const{proxy:y}=Te(),{$q:b}=y,h=Oe(e,b),m=s(()=>parseInt(e.min,10)),v=s(()=>parseInt(e.max,10)),g=s(()=>parseInt(e.maxPages,10)),O=s(()=>q.value+" / "+v.value),D=s(()=>le(e.boundaryLinks,e.input)),x=s(()=>le(e.boundaryNumbers,!e.input)),U=s(()=>le(e.directionLinks,e.input)),_=s(()=>le(e.ellipses,!e.input)),T=p(null),q=s({get:()=>e.modelValue,set:l=>{if(l=parseInt(l,10),e.disable||isNaN(l))return;const t=Ae(l,m.value,v.value);e.modelValue!==t&&n("update:modelValue",t)}});de(()=>`${m.value}|${v.value}`,()=>{q.value=e.modelValue});const F=s(()=>"q-pagination row no-wrap items-center"+(e.disable===!0?" disabled":"")),P=s(()=>e.gutter in re?`${re[e.gutter]}px`:e.gutter||null),N=s(()=>P.value!==null?`--q-pagination-gutter-parent:-${P.value};--q-pagination-gutter-child:${P.value}`:null),A=s(()=>{const l=[e.iconFirst||b.iconSet.pagination.first,e.iconPrev||b.iconSet.pagination.prev,e.iconNext||b.iconSet.pagination.next,e.iconLast||b.iconSet.pagination.last];return b.lang.rtl===!0?l.reverse():l}),H=s(()=>({"aria-disabled":e.disable===!0?"true":"false",role:"navigation"})),z=s(()=>Pe(e,"flat")),G=s(()=>({[z.value]:!0,round:e.round,rounded:e.rounded,padding:e.padding,color:e.color,textColor:e.textColor,size:e.size,ripple:e.ripple!==null?e.ripple:!0})),J=s(()=>{const l={[z.value]:!1};return e.activeDesign!==""&&(l[e.activeDesign]=!0),l}),R=s(()=>({...J.value,color:e.activeColor||e.color,textColor:e.activeTextColor||e.textColor})),w=s(()=>{let l=Math.max(g.value,1+(_.value?2:0)+(x.value?2:0));const t={pgFrom:m.value,pgTo:v.value,ellipsesStart:!1,ellipsesEnd:!1,boundaryStart:!1,boundaryEnd:!1,marginalStyle:{minWidth:`${Math.max(2,String(v.value).length)}em`}};return g.value&&l<v.value-m.value+1&&(l=1+Math.floor(l/2)*2,t.pgFrom=Math.max(m.value,Math.min(v.value-l+1,e.modelValue-Math.floor(l/2))),t.pgTo=Math.min(v.value,t.pgFrom+l-1),x.value&&(t.boundaryStart=!0,t.pgFrom++),_.value&&t.pgFrom>m.value+(x.value?1:0)&&(t.ellipsesStart=!0,t.pgFrom++),x.value&&(t.boundaryEnd=!0,t.pgTo--),_.value&&t.pgTo<v.value-(x.value?1:0)&&(t.ellipsesEnd=!0,t.pgTo--)),t});function $(l){q.value=l}function E(l){q.value=q.value+l}const L=s(()=>{function l(){q.value=T.value,T.value=null}return{"onUpdate:modelValue":t=>{T.value=t},onKeyup:t=>{qe(t,13)===!0&&l()},onBlur:l}});function d(l,t,k){const S={"aria-label":t,"aria-current":"false",...G.value,...l};return k===!0&&Object.assign(S,{"aria-current":"true",...R.value}),t!==void 0&&(e.toFn!==void 0?S.to=e.toFn(t):S.onClick=()=>{$(t)}),X(I,S)}return Object.assign(y,{set:$,setByOffset:E}),()=>{const l=[],t=[];let k;if(D.value===!0&&(l.push(d({key:"bls",disable:e.disable||e.modelValue<=m.value,icon:A.value[0]},m.value)),t.unshift(d({key:"ble",disable:e.disable||e.modelValue>=v.value,icon:A.value[3]},v.value))),U.value===!0&&(l.push(d({key:"bdp",disable:e.disable||e.modelValue<=m.value,icon:A.value[1]},e.modelValue-1)),t.unshift(d({key:"bdn",disable:e.disable||e.modelValue>=v.value,icon:A.value[2]},e.modelValue+1))),e.input!==!0){k=[];const{pgFrom:S,pgTo:j,marginalStyle:B}=w.value;if(w.value.boundaryStart===!0){const C=m.value===e.modelValue;l.push(d({key:"bns",style:B,disable:e.disable,label:m.value},m.value,C))}if(w.value.boundaryEnd===!0){const C=v.value===e.modelValue;t.unshift(d({key:"bne",style:B,disable:e.disable,label:v.value},v.value,C))}w.value.ellipsesStart===!0&&l.push(d({key:"bes",style:B,disable:e.disable,label:"\u2026",ripple:!1},S-1)),w.value.ellipsesEnd===!0&&t.unshift(d({key:"bee",style:B,disable:e.disable,label:"\u2026",ripple:!1},j+1));for(let C=S;C<=j;C++)k.push(d({key:`bpg${C}`,style:B,disable:e.disable,label:C},C,C===e.modelValue))}return X("div",{class:F.value,...H.value},[X("div",{class:"q-pagination__content row no-wrap items-center",style:N.value},[...l,e.input===!0?X(Q,{class:"inline",style:{width:`${O.value.length/1.5}em`},type:"number",dense:!0,value:T.value,disable:e.disable,dark:h.value,borderless:!0,inputClass:e.inputClass,inputStyle:e.inputStyle,placeholder:O.value,min:m.value,max:v.value,...L.value}):X("div",{class:"q-pagination__middle row justify-center"},k),...t])])}}});const K=e=>(ge("data-v-5b758faf"),e=e(),_e(),e),Ge=K(()=>c("div",{class:"text-h6 text-bold",style:{color:"#123499"}}," Edit Order Details ",-1)),Le={class:"text-bold"},je={class:"text-green"},Ye=K(()=>c("div",{class:"text-bold q-mt-md"},"Delivery Date",-1)),Ke=K(()=>c("div",{class:"text-bold q-mt-md"},"Courier Date",-1)),ze=K(()=>c("div",{class:"text-bold q-mt-md"},"Courier Tracking Number",-1)),We=K(()=>c("div",{class:"text-bold q-mt-xs"},"Name of the Courier",-1)),He=K(()=>c("div",{class:"text-bold q-mt-xs"},"Delivery Address",-1)),Je=K(()=>c("div",{class:"text-bold q-mt-xs"},"Order Status",-1)),Xe={__name:"editOrderDetailsModal",props:{showNewUserPopup:{type:Boolean,required:!0,default:!1},closeNewUserPopup:{type:Function,required:!0},selectedData:{type:Object,required:!0}},setup(e){const n=e,y=De(),b=he(),h=p(""),m=p(""),v=p(n.selectedData[0].delivery_number),g=p(n.selectedData[0].customer_name),O=p(n.selectedData[0].delivery_through),D=p(""),x=p(n.selectedData[0].order_status);let U=[{label:"yet_to_be_couriered",name:"Yet to be Couriered"},{label:"in_transit",name:"In Transit"},{label:"delivered",name:"Delivered"},{label:"cancelled",name:"Cancelled"}];const _=s({get:()=>n.showNewUserPopup,set:()=>n.closeNewUserPopup()}),T=s(()=>U.map(d=>d.name)),q=s(()=>["Yet to be Couriered","Delivered","Cancelled"].includes(n.selectedData[0].order_status)),F=s(()=>n.selectedData[0].order_status!=="Yet to be Couriered"),P=s(()=>n.selectedData[0].order_status==="In Transit"),N=s(()=>n.selectedData[0].order_status==="In Transit"),A=s(()=>n.selectedData[0].order_status==="In Transit"),H=s(()=>U.find(l=>l.name===x.value).label),z=s(()=>{let d=w(v.value),l=w(O.value),t=w(D.value),k=x.value==="Yet to be Couriered",S=x.value==="In Transit",j=x.value==="Delivered",B=S&&m.value,C=j&&h.value;return m.value&&h.value&&m.value>h.value||n.selectedData[0].order_status==="In Transit"&&!h.value||S&&h.value?!0:j?!C:!d||!l||!t||k||!B}),G=()=>{b.loading.show({spinner:Se,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},J=()=>{b.loading.hide()},R=(d=!1)=>{n.closeNewUserPopup(d)},w=d=>d&&d.toString().trim().length>0,$=()=>{let d=n.selectedData[0].order_status;d!=="Yet to be Couriered"&&(d==="In Transit"?U=[{label:"delivered",name:"Delivered"},{label:"cancelled",name:"Cancelled"}]:(d==="Delivered"||d==="Cancelled")&&(U=[]))},E=d=>{const[l,t,k]=d.split("-");return`${k}-${t}-${l}`},L=()=>{var l;G();let d={delivery_date:(l=h.value)!=null?l:null,courier_date:m.value,delivery_details:{delivery_through:O.value,delivery_number:v.value,delivery_address:D.value},order_status:H.value};y.updateOrders(d,n.selectedData[0].uid).then(t=>{R(!0),b.notify({message:"Order Details Updated Successfully!!!",type:"positive",position:"top"})}).catch(t=>{b.notify({message:"Something went Wrong. Please contact your admin!!!",type:"negative",position:"top"})}).finally(()=>{J()})};return Ne(()=>{n.selectedData[0].courier_date&&(m.value=E(n.selectedData[0].courier_date)),n.selectedData[0].delivery_date&&(h.value=E(n.selectedData[0].delivery_date)),n.selectedData[0].delivery_address||(D.value=n.selectedData[0].customer_address),$()}),(d,l)=>(M(),Y(fe,{modelValue:V(_),"onUpdate:modelValue":l[6]||(l[6]=t=>pe(_)?_.value=t:null),persistent:"",onKeydown:be(R,["esc"])},{default:f(()=>[r(ve,{class:"order-modal"},{default:f(()=>[r(Z,{class:"row items-center"},{default:f(()=>[Ge,r(Be),r(I,{icon:"close",flat:"",round:"",onClick:R})]),_:1}),r(Qe,{onSubmit:L},{default:f(()=>[r(Me,{style:{height:"calc(75vh - 170px)"}},{default:f(()=>[r(Z,null,{default:f(()=>[c("div",Le,[ie(" Customer - "),c("span",je,ce(g.value),1)]),Ye,r(Q,{modelValue:h.value,"onUpdate:modelValue":l[0]||(l[0]=t=>h.value=t),style:{"max-width":"200px"},outlined:"",dense:"",autofocus:"",type:"date",disable:V(q)},null,8,["modelValue","disable"]),Ke,r(Q,{modelValue:m.value,"onUpdate:modelValue":l[1]||(l[1]=t=>m.value=t),style:{"max-width":"200px"},outlined:"",dense:"",autofocus:"",type:"date",disable:V(F)},null,8,["modelValue","disable"]),ze,r(Q,{modelValue:v.value,"onUpdate:modelValue":l[2]||(l[2]=t=>v.value=t),style:{"max-width":"400px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter a Courier Tracking Number",maxlength:"128",rules:[t=>w(t)||"Field is required!!!"],disable:V(P)},null,8,["modelValue","rules","disable"]),We,r(Q,{modelValue:O.value,"onUpdate:modelValue":l[3]||(l[3]=t=>O.value=t),style:{"max-width":"400px"},outlined:"",dense:"",autofocus:"",placeholder:"Enter a Name of the Courier",maxlength:"128",rules:[t=>w(t)||"Field is required!!!"],disable:V(N)},null,8,["modelValue","rules","disable"]),He,r(Q,{modelValue:D.value,"onUpdate:modelValue":l[4]||(l[4]=t=>D.value=t),type:"textarea",style:{width:"400px"},outlined:"",dense:"",autofocus:"",rows:"2",placeholder:"Enter Delivery address.","input-class":"textarea-input",rules:[t=>w(t)||"Field is required!!!"],disable:V(A)},null,8,["modelValue","rules","disable"]),Je,r(ye,{style:{width:"320px"},filled:"",modelValue:x.value,"onUpdate:modelValue":l[5]||(l[5]=t=>x.value=t),options:V(T)},null,8,["modelValue","options"])]),_:1})]),_:1}),r(Z,{class:"row justify-end"},{default:f(()=>[r(me,{class:"q-px-none"},{default:f(()=>[r(I,{unelevated:"",color:"primary",label:"Save",type:"submit","no-caps":"",disable:V(z)},null,8,["disable"])]),_:1})]),_:1})]),_:1})]),_:1})]),_:1},8,["modelValue","onKeydown"]))}};var Ze=ue(Xe,[["__scopeId","data-v-5b758faf"]]);const et=e=>(ge("data-v-5f7d7a00"),e=e(),_e(),e),tt=et(()=>c("div",{class:"text-h6 text-bold text-center q-mt-lg q-pb-lg",style:{color:"#123499"}}," Orders File Upload ",-1)),lt={style:{height:"50px"}},at={__name:"openOrdersFileUploadModal",props:{showOrdersFileUploadPopup:{type:Boolean,required:!0,default:!1},closeOrdersFileUploadPopup:{type:Function,required:!0}},setup(e){const n=e,y=p(null),b=s({get:()=>n.showOrdersFileUploadPopup,set:()=>n.closeOrdersFileUploadPopup()}),h=s(()=>!y.value),m=()=>{let v=y.value&&y.value.length;n.closeOrdersFileUploadPopup(v)};return(v,g)=>(M(),Y(fe,{modelValue:V(b),"onUpdate:modelValue":g[1]||(g[1]=O=>pe(b)?b.value=O:null),persistent:"",onKeydown:be(m,["esc"])},{default:f(()=>[r(ve,{class:"orders-file-upload-modal"},{default:f(()=>[r(Z,{class:"items-center"},{default:f(()=>[r(I,{icon:"close",class:"float-right",flat:"",round:"",onClick:m}),tt,c("div",lt,[r(Re,{outlined:"",modelValue:y.value,"onUpdate:modelValue":g[0]||(g[0]=O=>y.value=O),accept:".csv",label:"Upload File",class:"q-px-lg"},null,8,["modelValue"])])]),_:1}),r(Z,{class:"row justify-end"},{default:f(()=>[r(me,{class:"q-px-none"},{default:f(()=>[r(I,{unelevated:"",color:"primary",label:"Upload",disable:V(h),type:"submit","no-caps":""},null,8,["disable"])]),_:1})]),_:1})]),_:1})]),_:1},8,["modelValue","onKeydown"]))}};var rt=ue(at,[["__scopeId","data-v-5f7d7a00"]]);const ot={class:"row q-pt-md q-ml-lg"},nt={class:"col-2"},st=c("p",{style:{color:"#123499"},class:"text-bold"},"Order From Date",-1),dt={class:"col-2"},ut=c("p",{style:{color:"#123499"},class:"text-bold"},"Order To Date",-1),it={class:"col-2"},ct=c("p",{style:{color:"#123499"},class:"text-bold"},"Courier Status",-1),mt={class:"col-2 q-ml-lg q-mt-lg"},vt={class:"q-ml-md q-mt-lg q-mr-lg q-pa-md"},pt={class:"row justify-start items-center"},bt=c("span",{class:"q-ml-sm"},null,-1),ft={class:"row justify-start items-center"},gt=c("span",{class:"q-ml-sm"},null,-1),_t={class:"row justify-start items-center"},yt=c("span",{class:"q-ml-sm"},null,-1),ht={class:"q-pa-lg flex flex-center"},St={key:0,class:"q-ml-md q-mt-sm q-mr-lg q-pa-md"},Rt={__name:"OrdersPage",setup(e){const n=De(),y=p(!1),b=p(!1),{orders:h}=ke(n);let m=[{name:"orderId",required:!0,label:"Order Id",align:"left",field:o=>o.order_id,format:o=>`${o}`,sortable:!0},{name:"orderDate",label:"Order Date",field:"order_date",sortable:!0,align:"center"},{name:"customerName",label:"Customer Name",field:"customer_name",align:"center"},{name:"mobileNumber",label:"Mobile Number",field:"mobile_number",align:"center"},{name:"referrerId",label:"Referrer Id",field:"referrer_id",align:"center"},{name:"referrerName",label:"Referrer Name",field:"referrer_name",align:"center"},{name:"referrerMobileNumber",label:"Referrer Mobile Number",field:"referrer_mobile_number",align:"center"},{name:"totalProductPrice",label:"Total Product Price",field:"total_product_price",align:"center"},{name:"cgst",label:"CGST Amount",field:"order_cgst_amount",align:"center"},{name:"sgst",label:"SGST Amount",field:"order_sgst_amount",align:"center"},{name:"igst",label:"IGST Amount",field:"order_igst_amount",align:"center"},{name:"gstTotal",label:"GST Total Amount",field:"order_gst_total_amount",align:"center"},{name:"orderTotal",label:"Order Total Amount",field:"order_total_amount",align:"center"},{name:"orderStatus",label:"Order Status",field:"order_status",align:"center"},{name:"courierDate",label:"Courier Date",field:"courier_date",align:"center"},{name:"deliveryThrough",label:"Courier Company Name",field:"delivery_through",align:"center"},{name:"deliveryNumber",label:"Courier Tracking Number",field:"delivery_number",align:"center"},{name:"deliveryAddress",label:"Delivery Address",field:"delivery_address",align:"center"},{name:"deliveryDate",label:"Delivery Date",field:"delivery_date",align:"center"},{name:"paymentMode",label:"Payment Mode",field:"payment_mode",align:"center"},{name:"paymentStatus",label:"Payment Status",field:"payment_status",align:"center"},{name:"paymentDate",label:"Payment Date",field:"payment_date",align:"center"},{name:"paymentReference",label:"Payment Reference",field:"payment_reference",align:"center"}],v=[{name:"uid",required:!0,label:"Order Item Id",align:"left",field:o=>o.order_item_number,format:o=>`${o}`,sortable:!0},{name:"productName",label:"Product Name",field:"product_name",align:"center"},{name:"quantity",label:"Quantity",field:"quantity",align:"center"},{name:"hsnCode",label:"HSN Code",field:"hsn_code",align:"center"},{name:"price",label:"Price (INR)",field:"price",align:"center"},{name:"cgstPercentage",label:"CGST (%)",field:"cgst_percentage",align:"center"},{name:"cgstAmount",label:"CGST Amount (INR)",field:"cgst_amount",align:"center"},{name:"sgstPercentage",label:"SGST (%)",field:"sgst_percentage",align:"center"},{name:"sgstAmount",label:"SGST Amount (INR)",field:"sgst_amount",align:"center"},{name:"igstPercentage",label:"IGST (%)",field:"igst_percentage",align:"center"},{name:"igstAmount",label:"IGST Amount (INR)",field:"igst_amount",align:"center"},{name:"gstTotalAmount",label:"GST Total (INR)",field:"gst_total_amount",align:"center"},{name:"totalAmount",label:"Total (INR)",field:"total_amount",align:"center"}];const g=p({page:1,rowsPerPage:10,rowsNumber:10,totalPages:0}),O=p(m),D=p([]),x=p(v),U=p([]),_=p([]),T=p(""),q=p(!1),F=p("All"),P=p(""),N=p("");let A=[{label:"all",name:"All"},{label:"yet_to_be_couriered",name:"Yet to be Couriered"},{label:"in_transit",name:"In transit"},{label:"delivered",name:"Delivered"},{label:"cancelled",name:"Cancelled"}];const H=p("Orders Template Download"),z=p("Orders Data Upload"),G=he(),J=s(()=>A.map(o=>o.name)),R=s(()=>A.find(a=>a.name===F.value).label),w=o=>{g.value.page=o,S()},$=s(()=>!P.value||!N.value),E=()=>{G.loading.show({spinner:Se,spinnerColor:"light-blue",messageColor:"white",backgroundColor:"light-blue",message:""})},L=()=>{G.loading.hide()},d=(o=!1)=>{y.value=!1,o===!0&&(_.value=[],S())},l=(o=!1)=>{b.value=!1,o===!0&&S()},t=()=>{y.value=!0},k=o=>o==="Yet to be Couriered"?"orange":o==="In Transit"?"purple":o==="Delivered"?"green":"red",S=()=>{E();let o={fromDate:P.value,toDate:N.value,orderStatus:R.value,page:g.value.page,rowsPerPage:10};n.getOrders(o).then(a=>{var u,i,ee;console.log("res",g.value),h.value=(u=a.data)==null?void 0:u.data,D.value=[...(i=a.data)==null?void 0:i.data],g.value.totalPages=(ee=a.data)==null?void 0:ee.total_page_count}).catch(a=>{console.log("errror",a)}).finally(()=>{L()})},j=o=>{n.searchOrderNumber(o.filter).then(a=>{D.value=a.data}).catch(a=>{console.log("err",a)}),console.log(o)},B=()=>{let o=h.value.find(a=>a.order_id===_.value[0].order_id).order_items;U.value=o},C=()=>{if(N.value<P.value){G.notify({message:"Order From Date should be less than or equal to Order To Date!!!",type:"warning",position:"top"});return}_.value=[],S()},ae=()=>{E();let o={fromDate:P.value,toDate:N.value,orderStatus:R.value};n.getOrdersCsvTemplate(o).then(a=>{let u=window.URL.createObjectURL(new Blob([a.data])),i=document.createElement("a");i.href=u,i.setAttribute("download","Yet_To_Be_Couriered_Orders.csv"),document.body.appendChild(i),i.click(),i.remove()}).catch(a=>{console.log("err",a)}).finally(()=>{L()})},xe=()=>{E();let o=F.value.replace(/ /g,"_"),a="Registration_Payments_All.xlsx";$.value||(a=`Registration_Payments_${o}_from_${P.value}_to_${N.value}.xlsx`);let u=[];for(let i of D.value){let ee={"Order Id":i.order_id,"Order Date":i.order_date,"Customer Name":i.customer_name,"Mobile Number":i.mobile_number,"Referrer Id":i.referrer_id,"Referrer Name":i.referrer_name,"Referrer Mobile Number":i.referrer_mobile_number,"Total Product Price":i.total_product_price,"CGST Amount":i.order_cgst_amount,"SGST Amount":i.order_sgst_amount,"IGST Amount":i.order_igst_amount,"GST Total Amount":i.order_gst_total_amount,"Order Total Amount":i.order_total_amount,"Order Status":i.order_status,"Courier Date":i.courier_date,"Courier Company Name":i.delivery_through,"Courier Tracking Number":i.delivery_number,"Delivery Address":i.delivery_address,"Delivery Date":i.delivery_date,"Payment Mode":i.payment_mode,"Payment Status":i.payment_status,"Payment Date":i.payment_date};u.push(ee)}$e(u,a),L()};return de(_,o=>{o.length?B():U.value=[]}),(o,a)=>(M(),oe(Ie,null,[c("div",ot,[c("div",nt,[st,r(Q,{modelValue:P.value,"onUpdate:modelValue":a[0]||(a[0]=u=>P.value=u),style:{"max-width":"150px"},outlined:"",dense:"",autofocus:"",type:"date"},null,8,["modelValue"])]),c("div",dt,[ut,r(Q,{modelValue:N.value,"onUpdate:modelValue":a[1]||(a[1]=u=>N.value=u),style:{"max-width":"150px"},outlined:"",dense:"",autofocus:"",type:"date"},null,8,["modelValue"])]),c("div",it,[ct,r(ye,{filled:"",dense:"",style:{width:"200px","max-height":"100px"},modelValue:F.value,"onUpdate:modelValue":a[2]||(a[2]=u=>F.value=u),options:V(J)},null,8,["modelValue","options"])]),c("div",mt,[r(I,{unelevated:"",color:"primary",label:"Search","no-caps":"",disable:V($),onClick:C},null,8,["disable"])])]),c("div",vt,[c("div",null,[r(I,{color:"green",class:"q-mb-md",style:{width:"20px"},"no-caps":"",onClick:xe},{default:f(()=>[c("div",pt,[r(te,{name:"fas fa-file-excel"}),bt])]),_:1}),F.value==="Yet to be Couriered"?(M(),Y(I,{key:0,color:"primary",class:"q-mb-md float-right",style:{width:"20px"},"no-caps":"",disable:V($)||!D.value.length,onClick:a[3]||(a[3]=u=>b.value=!0)},{default:f(()=>[r(se,{content:z.value,"max-width":"20rem"},null,8,["content"]),c("div",ft,[r(te,{name:"fas fa-upload"}),gt])]),_:1},8,["disable"])):W("",!0),F.value==="Yet to be Couriered"?(M(),Y(I,{key:1,color:"primary",class:"q-mb-md float-right q-mr-md",style:{width:"20px"},"no-caps":"",disable:V($)||!D.value.length,onClick:ae},{default:f(()=>[r(se,{content:H.value,"max-width":"20rem"},null,8,["content"]),c("div",_t,[r(te,{name:"fas fa-download"}),yt])]),_:1},8,["disable"])):W("",!0)]),r(ne,{ref:o.orderTable,class:"orders-table",flat:"",bordered:"",title:"Orders",rows:D.value,columns:O.value,pagination:g.value,"onUpdate:pagination":a[6]||(a[6]=u=>g.value=u),"row-key":"order_id",onRequest:j,selected:_.value,"onUpdate:selected":a[7]||(a[7]=u=>_.value=u),filter:T.value},{"top-right":f(()=>[q.value?(M(),Y(Q,{key:0,filled:"",borderless:"",dense:"",debounce:"300",modelValue:T.value,"onUpdate:modelValue":a[4]||(a[4]=u=>T.value=u),placeholder:"Search"},{append:f(()=>[r(te,{name:"search"})]),_:1},8,["modelValue"])):W("",!0),r(I,{class:"q-ml-sm",icon:"filter_list",onClick:a[5]||(a[5]=u=>q.value=!q.value),flat:""})]),"body-cell-orderStatus":f(u=>[r(Fe,{props:u},{default:f(()=>[r(Ue,{color:k(u.row.order_status),"text-color":"white",dense:"",class:"text-weight-bolder",square:""},{default:f(()=>[ie(ce(u.row.order_status),1)]),_:2},1032,["color"])]),_:2},1032,["props"])]),_:1},8,["rows","columns","pagination","selected","filter"]),c("div",ht,[r(Ee,{modelValue:g.value.page,"onUpdate:modelValue":[a[8]||(a[8]=u=>g.value.page=u),w],max:g.value.totalPages,"max-pages":6,"boundary-numbers":!0,ellipses:!0},null,8,["modelValue","max"])]),r(I,{class:"q-mt-md",color:"primary",label:"Edit",disable:!_.value.length||_.value[0].order_status==="Delivered",onClick:t},null,8,["disable"])]),_.value.length?(M(),oe("div",St,[r(ne,{class:"orders-table",flat:"",bordered:"",title:"Order Items",rows:U.value,columns:x.value,"row-key":"order_id",filter:T.value},null,8,["rows","columns","filter"])])):W("",!0),y.value?(M(),Y(Ze,{key:1,modelValue:y.value,"onUpdate:modelValue":a[9]||(a[9]=u=>y.value=u),"show-new-user-popup":y.value,"close-new-user-popup":d,"selected-data":_.value},null,8,["modelValue","show-new-user-popup","selected-data"])):W("",!0),b.value?(M(),Y(rt,{key:2,modelValue:b.value,"onUpdate:modelValue":a[10]||(a[10]=u=>b.value=u),"show-orders-file-upload-popup":b.value,"close-orders-file-upload-popup":l},null,8,["modelValue","show-orders-file-upload-popup"])):W("",!0)],64))}};export{Rt as default};