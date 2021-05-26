<%@page import="project.ConnectionProvider" %>
<%@page import="java.sql.*" %>
<%
String rollNo=request.getParameter("rollNo");
String m1=request.getParameter("m1");
String m2=request.getParameter("m2");
String m3=request.getParameter("m3");
String m4=request.getParameter("m4");
String m5=request.getParameter("m5");
try
{
	Connection con=ConnectionProvider.getCon();
	Statement st=con.createStatement();
	st.executeUpdate("insert into attandence values('"+rollNo+"','"+m1+"','"+m2+"','"+m3+"','"+m4+"','"+m5+"')");
	response.sendRedirect("adminHome.jsp");
}
catch(Exception e)
{
	out.println(e);
}

%>