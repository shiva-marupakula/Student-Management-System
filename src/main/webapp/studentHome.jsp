<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*" %>
<%
try
{
	String rollNo=request.getParameter("rollNo");
	String password=request.getParameter("password");
	Connection con=ConnectionProvider.getCon();
	Statement st=con.createStatement();
	//ResultSet rs=st.executeQuery("select *from student inner join result where student.rollNo=result.rollNo and student.rollNo='"+rollNo+"'");
	ResultSet rs=st.executeQuery("select * from student where rollNo='"+rollNo+"' and password='"+password+"'");
	if(rs.next()){
%>
<img src="gd1.jpg"  align="left"width="150" height="150">
<center><img src="sms_logo1.JPG" width="150" height="150">
<img src="apj sir.png" align="right"  width="150" height="150"></center>
  <hr class="new1">

<style>
table{
  width:100%;
  table-layout: fixed;
}
th{
  padding: 20px 15px;
  text-align: left;
  font-weight: 500;
  font-size: 12px;
  color: #fff;
  text-transform: uppercase;
 border: 2px solid rgba(255,255,255,0.3);
}


/* demo styles */

@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300,700);
body{
  background: -webkit-linear-gradient(left, #25c481, #25b7c4);
  background: linear-gradient(to right, #25c481, #25b7c4);
  font-family: 'Roboto', sans-serif;
}

</style>
  <!--for demo wrap-->
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>institution Name: UoCI</th>
          <th>Course Name:<%=rs.getString(1)%></th>
          <th>Branch Name: <%=rs.getString(2)%></th>
          <th><center>RollNo: <%=rs.getString(3)%></center></th>
        </tr>
      </thead>
      <thead>
        <tr>
          <th>Name: <%=rs.getString(4)%></th>
          <th>Father Name: <%=rs.getString(5)%></th>
          <th>Gender: <%=rs.getString(6)%></th>
          <th><a href="dgiOneView.html"><center><img src="log-out-hi.png" width="100" height="18"></center></a></th>
        </tr>
      </thead>
    </table>
  </div>
  <div>
  	
  		<center><a href="resultHome.html"><input type="submit" name="submit" value="View Results"></a></center>
  
  </div>
<div class="w3-container">
<!-- View Attendance -->
  <div id="india" class="w3-container w3-border city">
  <br>
   <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Fonts -->
    <link rel="dns-prefetch" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Raleway:300,400,600" rel="stylesheet" type="text/css">



    <link rel="icon" href="Favicon.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
</head>
<body>
<main class="my-form">
    <div class="cotainer">
        <div class="row justify-content-center">
            <div class="col-md-8">
                    <div class="card">
                        <center><div class="card-header">Your Attendance</div></center>
                        <div class="card-body">
                            
<%@page import="project.ConnectionProvider" %>
		<%@page import="java.sql.*" %>
		<%
		try
		{
		Connection mcon=ConnectionProvider.getCon();
		Statement sst=mcon.createStatement();
		ResultSet sps=sst.executeQuery("select * from attandence where rollNo='"+rollNo+"'");
		//response.sendRedirect("studentHome.jsp");
		if(sps.next()){
		%>
  <!--for demo wrap-->
<style>
html {
  font-family:arial;
  font-size: 25px;
}

td {
  border: 2px solid #726E6D;
  padding: 15px;
  color:black;
  text-align:center;
}

thead{
  font-weight:bold;
  text-align:center;
  background: #625D5D;
  color:white;
}

table {
  border-collapse: collapse;
}

.footer {
  text-align:right;
  font-weight:bold;
}

tbody >tr:nth-child(odd) {
  background: #D1D0CE;
}

</style>
<head>
</head>
<body>
  <table>
    <thead>
      <tr>
        <td>Month</td>
        <td>Working Days</td>
        <td>Attended Days</td>
        <td>Percentage</td>        
      </tr>

    </thead>
    <tbody>
      <tr>
        <td>January</td>
        <td >24 </td>
        <td><%=sps.getString(2)%></td>
        <td><%out.println((sps.getInt(2)*100)/24);%></td>
      </tr>
      <tr>
        <td>February</td>
        <td>24 </td>
        <td><%=sps.getString(3)%></td>
        <td><%out.println((sps.getInt(3)*100)/24);%></td>

      </tr>
      <tr>
        <td>March</td>
        <td>24 </td>
        <td><%=sps.getString(4)%></td>
        <td><%out.println((sps.getInt(4)*100)/24);%></td>>
       
      </tr>
      <tr>
       <td>April</td>
        <td>24 </td>
        <td><%=sps.getString(5)%></td>
        <td><%out.println((sps.getInt(5)*100)/24);%></td>
 
      </tr>
      <tr>
        <td>May</td>
        <td>24 </td>
        <td><%=sps.getString(6)%></td>
        <td><%out.println((sps.getInt(6)*100)/24);%></td>
       
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td colspan="1" class="footer">Total</td>
        <td>120</td>
        <td><%int sum=sps.getInt(2)+sps.getInt(3)+sps.getInt(4)+sps.getInt(5)+sps.getInt(6); out.println(sum);%></td>
        <td><%out.println((sum*100)/120);%></td>
      </tr>
  </table>
</body>

<%}
else
{

}
}
catch(Exception e)
{}
%>
                        </div>
                    </div>
            </div>
        </div>
    </div>
</main>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
  </div>



</div>
    <hr class="new1">
  <center><h6>Note: If you found Any errors in your Details or Marks, Consult your respective faculty.
  </h6>
  <h6>Contact us: team.sms@gmail.com</h6></center>
  <hr class="new1">
<center><h6>All Right Reserved @ Team Student Management system::2021</h6></center> 
  <hr class="new1">
</body>

<%}
else
{
	response.sendRedirect("errorDgiOneView.html");
}
}
catch(Exception e)
{}
%>


