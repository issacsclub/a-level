Module Module1

    Sub Main()
        ''Question 1 (a)
        Dim TheData(0 To 8) As Integer
        TheData(0) = 20
        TheData(1) = 3
        TheData(2) = 4
        TheData(3) = 8
        TheData(4) = 12
        TheData(5) = 99
        TheData(6) = 4
        TheData(7) = 26
        TheData(8) = 4

        PrintArray(TheData)


    End Sub
    Sub InsertionSort(ByRef TheData() As Integer)
        Dim NextValue As Integer
        For Count = 0 To TheData.Length - 1
            Dim DataToInsert As Integer = TheData(Count)
            Dim Inserted As Integer = 0
            NextValue = Count - 1
            While (NextValue >= 0 And Inserted <> 1)
                If (DataToInsert < TheData(NextValue)) Then
                    TheData(NextValue + 1) = TheData(NextValue)
                    NextValue = NextValue - 1
                    TheData(NextValue + 1) = DataToInsert
                Else
                    Inserted = 1
                End If
            End While
        Next
    End Sub

    Sub PrintArray(TheData() As Integer)
        For Count = 0 To 8
            Console.WriteLine(TheData(Count))
        Next
        Console.ReadKey()

    End Sub


End Module
