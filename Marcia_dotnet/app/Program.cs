using System;
using System.Collections;
using System.Collections.Generic;

namespace app
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList l = new ArrayList();

            l.Add("manga");
            l.Add("banana");
            l.Add("melão");
            l.Add("melancia");
            l.Add("ata");
            l.Add("siriguela");
            l.Add("tangerina");
            l.Add("abacate");
            l.Add("abacaxi");
            l.Add("caju");
            l.Add("laranja");
            l.Add("murici");
            l.Add("goiaba");
            l.Add("mamão");
            l.Add("uva");

            Console.WriteLine("Lista:\n");
            for (int i = 0; i < l.Count; i++)
            {
                Console.WriteLine(l[i]);

            }

            Dictionary<string, int> d = new Dictionary<string, int>();
            d.Add("manga", 50);
            d.Add("banana", 100);
            d.Add("melão", 5);
            d.Add("melancia", 5);
            d.Add("ata", 100);
            d.Add("siriguela", 200);
            d.Add("tangerina", 50);
            d.Add("abacate", 10);
            d.Add("abacaxi", 15);
            d.Add("caju", 25);
            d.Add("laranja", 50);
            d.Add("murici", 150);
            d.Add("goiaba", 4);
            d.Add("mamão", 4);
            d.Add("uva", 250);
            Console.WriteLine("\nDicionário:\n");
            foreach (KeyValuePair<string, int> va in d)
            {
                Console.WriteLine("{0}, {1}", va.Key, va.Value);
            }
        }
    }
}
