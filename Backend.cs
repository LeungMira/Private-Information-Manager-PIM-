using System;
using System.Collections.Generic;

namespace MyNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            // Your code here
        }
    }
    public class Personel
    {
        public string name{get; set;};
        public int SSN{get; set;};
        public string Location{get; set;};
         public int PhilHealthID{get; set;};
         public int JobID{get; set;};
         public string BirthPlacement{get; set;};
         public string height{get; set;};
         public string weight{get; set;};
         public string bloodType{get; set;};
         public int zipcode{get; set;};
         public string BirthDate {get;set;};
         public string gender {get; set;};
        
        public Personel (string name, int SSN, string Location, int PhilHealthID, int JobID, string BirthPlacement, string height, string weight, string bloodType, int zipcode, string bloodType, string BirthDate, string gender)
        {
            this.BirthPlacement = BirthPlacement;
            this.height = height;
            this.weight = weight;
            this.bloodType = bloodType;
            this.zipcode = zipcode;
            this.name = name;
            this.SSN = SSN;
            this.Location = Location;
            this.PhilHealthID = PhilHealthID;
            this.JobID = JobID;
            this.gender = gender;
            this.BirthDate = BirthDate;
            

        }
    }
    public static void CreateAppend(string name, int SSN, string Location, int PhilHealthID, int JobID, string BirthPlacement, string height, string weight, string bloodType, int zipcode, string BirthDate, string gender)
        {
            Personel personel = new Personel(name, SSN, Location, PhilHealthID, JobID, BirthPlacement, height, weight, bloodType, zipcode, BirthDate, gender);
            people.Add(personel);  // Append to the list
            Console.WriteLine($"Added {personel.name} to the list.");
        }
}