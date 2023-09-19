using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EsPar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            double numero = Convert.ToDouble(numericUpDown1.Value);

            bool EsPrimo(Double numero)
            {
            if (numero < 2)
            {
                return false;
            }

            for (int i = 2; i < numero; i++)
            {
                if (numero % i == 0)
                {
                    return false;
                }
            }
            // Si no es divisible por ningún número, entonces es primo
            return true;
            }

            MessageBox.Show($"El numero {numero}{(EsPrimo(numero) ? "" : "no")} es primo.");   
        }
    }
}
