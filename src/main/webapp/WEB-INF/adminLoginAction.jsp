<%
String username1=request.getParameter("username");
String password1=request.getParameter("password");

if(username1.equalsIgnoreCase("shiva") && password1.equalsIgnoreCase("1234"))
{
	response.sendRedirect("adminHome.jsp");
}
else
	response.sendRedirect("errorAdminLogin.html");
%>