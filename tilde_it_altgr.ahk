#Requires AutoHotkey v2.0

; Map AltGr + \ to print a backtick
<^>!\::
{
    Send("{``}")
    Return
}

; Map AltGr + | (Shift + \) to print a tilde
<^>!+\::
{
    Send("~")
    Return
}
