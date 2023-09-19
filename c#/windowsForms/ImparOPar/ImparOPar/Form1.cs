using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ImparOPar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double numero = Convert.ToDouble(numericUpDown1.Value);
            string tipo;

            if (numero % 2 == 0)
            {
                tipo = "par";
            }
            else
            {
                tipo = "impar";
            }

            MessageBox.Show($"El número {numero} es {tipo}.");
        }
    }
}
