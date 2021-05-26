<%
String username1=request.getParameter("username");
String password1=request.getParameter("password");

if((username1.equalsIgnoreCase("shiva") && password1.equalsIgnoreCase("shiva.sms"))||(username1.equalsIgnoreCase("sushmita") && password1.equalsIgnoreCase("sushmita.sms"))||(username1.equalsIgnoreCase("pavani") && password1.equalsIgnoreCase("pavani.sms"))||(username1.equalsIgnoreCase("harika") && password1.equalsIgnoreCase("harika.sms"))||(username1.equalsIgnoreCase("harsha") && password1.equalsIgnoreCase("harsha.sms"))  )
{
	response.sendRedirect("adminHome.jsp");
}
else
	response.sendRedirect("errorAdminLogin.html");
%>